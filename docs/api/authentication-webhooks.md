# Authentication & Webhooks

Every API request is signed with a merchant secret. Webhooks use a separate secret so receiving systems can verify that status updates were sent by the payment platform.

## Request signing

Build the signature input from the uppercase HTTP method, request path without the query string, Unix timestamp, and exact request body. Join the values with newline characters in this order:

{% call api_code_block(title="Signature input", language="text") %}
POST
/api/v1/payments
1784894400
{"reference_id":"checkout-1042","amount":129.5,"currency":"EUR"}
{% endcall %}

Compute an HMAC-SHA256 digest with the API secret and send the lowercase hexadecimal digest in `X-Signature`.

{% call api_code_tabs() %}

{% call api_code_tab(label="Python", title="Generate a request signature", language="python", active=True) %}
import hashlib
import hmac
import json
import os
import time

api_secret = os.environ["API_SECRET"]
method = "POST"
path = "/api/v1/payments"
timestamp = str(int(time.time()))
payload = {
    "reference_id": "checkout-1042",
    "amount": 129.5,
    "currency": "EUR",
}

body = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
signing_input = "\n".join([method, path, timestamp, body])
signature = hmac.new(api_secret.encode(), signing_input.encode(), hashlib.sha256).hexdigest()
{% endcall %}

{% call api_code_tab(label="JavaScript", title="Generate a request signature", language="javascript") %}
import { createHmac } from "node:crypto";

const method = "POST";
const path = "/api/v1/payments";
const timestamp = Math.floor(Date.now() / 1000).toString();
const apiSecret = process.env.API_SECRET;

if (!apiSecret) throw new Error("API_SECRET is not set");

const body = JSON.stringify({
  reference_id: "checkout-1042",
  amount: 129.5,
  currency: "EUR",
});

const signingInput = [method, path, timestamp, body].join("\n");
const signature = createHmac("sha256", apiSecret)
  .update(signingInput, "utf8")
  .digest("hex");
{% endcall %}

{% endcall %}

!!! danger "Sign the exact bytes you send"
    Serializing the JSON body again can change spaces, escaped characters, or field order. Generate the signature from the final request body, then send those same bytes without modification.

## Webhook flow

The platform sends a webhook after a payment changes state. A fast acknowledgement keeps delivery reliable; business processing can continue asynchronously.

<div class="sequence" role="img" aria-label="The platform sends a signed webhook. The merchant verifies the raw body and timestamp, stores the event, and returns a successful response.">
  <div class="sequence__node"><strong>Platform</strong><span>sign event</span></div>
  <span class="sequence__arrow" aria-hidden="true">&#8594;</span>
  <div class="sequence__node"><strong>Webhook endpoint</strong><span>verify signature</span></div>
  <span class="sequence__arrow" aria-hidden="true">&#8594;</span>
  <div class="sequence__node"><strong>Event store</strong><span>deduplicate by ID</span></div>
  <span class="sequence__arrow" aria-hidden="true">&#8594;</span>
  <div class="sequence__node"><strong>HTTP 204</strong><span>acknowledge delivery</span></div>
</div>

{% call api_code_block(title="Payment status event", language="http") %}
POST /webhooks/payments HTTP/1.1
X-Webhook-Id: evt_01J3N0BA56K1DQP9HV2WDMGMR8
X-Webhook-Timestamp: 1784894460
X-Webhook-Signature: 1e7b8d928f82a41b...
Content-Type: application/json

{
  "id": "evt_01J3N0BA56K1DQP9HV2WDMGMR8",
  "type": "payment.succeeded",
  "created_at": "2026-07-24T12:01:00Z",
  "data": {
    "payment_id": "6c959fed-0e69-4d8c-b0c1-0c9f343f6d8f",
    "reference_id": "checkout-1042",
    "status": "SUCCEEDED",
    "amount": 129.5,
    "currency": "EUR"
  }
}
{% endcall %}

### Verify a webhook

1. Read the raw request body before parsing JSON.
2. Reject timestamps outside a five-minute tolerance window.
3. Compute HMAC-SHA256 over `<timestamp>.<raw_body>` with the webhook secret.
4. Compare signatures with a constant-time function.
5. Store the event ID before starting business processing.
6. Return any `2xx` response after the event is durably accepted.

!!! important "Protect against replay"
    Validate both the timestamp and event ID. Signature verification proves authenticity; timestamp tolerance and deduplication prevent an authentic event from being processed repeatedly.

## Delivery behavior

| Endpoint response | Platform behavior | Merchant action |
| --- | --- | --- |
| `2xx` | Delivery is accepted. | Process the stored event once. |
| `4xx` | Delivery may stop because the endpoint rejected the event. | Correct credentials, validation, or endpoint configuration. |
| `5xx` or timeout | Delivery is retried with backoff. | Return quickly and move slow work to a queue. |

!!! tip "Operational logging"
    Log the event ID, payment ID, signature result, response code, and processing outcome. Never log secrets or full customer payloads.

{{ api_page_link(title="Create a payment", href="../create-payment/", icon="card", description="Return to the endpoint that uses these headers and callbacks.") }}
