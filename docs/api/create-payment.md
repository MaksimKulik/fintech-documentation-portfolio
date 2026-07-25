---
hide:
  - toc
---

# Create a Payment

Creates a payment and returns the URL where the customer completes the payment flow.

!!! warning "Use a stable idempotency key"
    Send one unique `Idempotency-Key` for each intended payment. Reuse the same key when retrying after a timeout, but generate a new key for a new payment.

## Endpoint

<span class="api-method post">POST</span> `/api/v1/payments`

{% call api_request_code_group(method="POST", path="/api/v1/payments", default_label="HTTP", aside=True) %}

{% call api_code_option(label="HTTP", language="http", active=True) %}
{% raw %}
POST /api/v1/payments HTTP/1.1
Host: api.example-payments.com
X-Api-Key-Id: 7d9181bd-5442-4ea7-9ad8-85e74a82f3d2
X-Signature: 79d965cd4e62967a...
X-Timestamp: 1784894400
Idempotency-Key: payment-checkout-1042
Content-Type: application/json

{
  "reference_id": "checkout-1042",
  "amount": 129.5,
  "currency": "EUR",
  "payment_method_id": "ee8d8b23-2f27-47a5-93dc-bbf96ab352de",
  "customer": {
    "id": "customer-778",
    "email": "alex@example.com"
  },
  "callback_url": "https://merchant.example/webhooks/payments",
  "return_urls": {
    "success": "https://merchant.example/checkout/success",
    "failure": "https://merchant.example/checkout/failure"
  }
}
{% endraw %}
{% endcall %}

{% call api_code_option(label="cURL", language="bash") %}
{% raw %}
curl --request POST 'https://api.example-payments.com/api/v1/payments' \
  --header 'X-Api-Key-Id: 7d9181bd-5442-4ea7-9ad8-85e74a82f3d2' \
  --header 'X-Signature: 79d965cd4e62967a...' \
  --header 'X-Timestamp: 1784894400' \
  --header 'Idempotency-Key: payment-checkout-1042' \
  --header 'Content-Type: application/json' \
  --data '{
    "reference_id": "checkout-1042",
    "amount": 129.5,
    "currency": "EUR",
    "payment_method_id": "ee8d8b23-2f27-47a5-93dc-bbf96ab352de",
    "customer": {"id": "customer-778", "email": "alex@example.com"},
    "callback_url": "https://merchant.example/webhooks/payments",
    "return_urls": {
      "success": "https://merchant.example/checkout/success",
      "failure": "https://merchant.example/checkout/failure"
    }
  }'
{% endraw %}
{% endcall %}

{% endcall %}

{% call api_response_code_group(default_status="201", default_text="Created. Payment created successfully.", default_content_type="application/json", aside=True) %}

{% call api_code_option(label="201", language="json", active=True, status=201, status_text="Created. Payment created successfully.", content_type="application/json") %}
{% raw %}
{
  "id": "6c959fed-0e69-4d8c-b0c1-0c9f343f6d8f",
  "reference_id": "checkout-1042",
  "status": "CREATED",
  "amount": 129.5,
  "currency": "EUR",
  "checkout_url": "https://pay.example-payments.com/p/6c959fed",
  "created_at": "2026-07-24T12:00:00Z",
  "updated_at": "2026-07-24T12:00:00Z"
}
{% endraw %}
{% endcall %}

{% call api_code_option(label="409", language="json", status=409, status_text="Conflict. The idempotency key has already been used with different data.", content_type="application/json") %}
{% raw %}
{
  "error": {
    "code": "IDEMPOTENCY_CONFLICT",
    "message": "The idempotency key belongs to a different request.",
    "request_id": "req_01J3MYNQ7J5A5ZA3M6YCTK84RG"
  }
}
{% endraw %}
{% endcall %}

{% endcall %}

{{ api_required_headers() }}

{% call api_parameters("Additional header") %}
{{ api_param(name="Idempotency-Key", field_type="string", requirement="required", description="Merchant-generated key that makes retries safe.", constraints="1-64 printable ASCII characters") }}
{% endcall %}

{% call api_schema(title="Request body", content_type="application/json", description="Payment details and merchant callback destinations.") %}

{{ api_field(name="reference_id", field_type="string", requirement="required", description="Payment identifier in the merchant system.", constraints="1-64 characters") }}
{{ api_field(name="amount", field_type="number", format="decimal", requirement="required", description="Amount charged to the customer.", constraints="Greater than 0; maximum 2 decimal places") }}
{{ api_field(name="currency", field_type="string", format="enum", requirement="required", description="Three-letter ISO 4217 payment currency.", enum=["EUR", "GBP", "USD"]) }}
{{ api_field(name="payment_method_id", field_type="string", format="uuid", requirement="required", description="Enabled payment method used to route the payment.") }}

{% call api_object(name="customer", requirement="required", description="Customer details used for risk checks and payment processing.", open=False) %}
{{ api_field(name="id", field_type="string", requirement="required", description="Stable customer identifier in the merchant system.") }}
{{ api_field(name="email", field_type="string", format="email", requirement="required", description="Customer email address.") }}
{% endcall %}

{{ api_field(name="callback_url", field_type="string", format="uri", requirement="required", description="HTTPS endpoint that receives payment status webhooks.") }}

{% call api_object(name="return_urls", requirement="required", description="Merchant pages used after the hosted payment flow.", open=False) %}
{{ api_field(name="success", field_type="string", format="uri", requirement="required", description="Destination after a successful customer flow.") }}
{{ api_field(name="failure", field_type="string", format="uri", requirement="required", description="Destination after a failed or cancelled customer flow.") }}
{% endcall %}

{% endcall %}

{% call api_responses() %}

{% call api_response(status=201, description="Created. Payment created successfully.", content_type="application/json", open=False) %}
{{ api_response_description("Returns the payment resource and its hosted checkout URL.") }}
{{ api_field(name="id", field_type="string", format="uuid", requirement="", description="Platform-generated payment identifier.") }}
{{ api_field(name="reference_id", field_type="string", requirement="", description="Merchant payment identifier supplied in the request.") }}
{{ api_field(name="status", field_type="string", format="enum", requirement="", description="Current payment state.", enum=["CREATED", "PROCESSING", "SUCCEEDED", "FAILED"]) }}
{{ api_field(name="amount", field_type="number", format="decimal", requirement="", description="Payment amount.") }}
{{ api_field(name="currency", field_type="string", requirement="", description="Payment currency.") }}
{{ api_field(name="checkout_url", field_type="string", format="uri", requirement="", description="Hosted page where the customer completes the payment.") }}
{{ api_field(name="created_at", field_type="string", format="date-time", requirement="", description="Creation time in UTC using ISO 8601.") }}
{{ api_field(name="updated_at", field_type="string", format="date-time", requirement="", description="Most recent update time in UTC using ISO 8601.") }}
{% endcall %}

{% call api_response(status=409, description="Conflict. Idempotency key reused with different request data.", content_type="application/json") %}
{{ api_response_description("Returns a structured error with a stable code and request identifier.") }}
{% endcall %}

{% endcall %}

{{ api_page_link(title="Authentication and webhook verification", href="../authentication-webhooks/", icon="authentication", description="Generate request signatures and process status updates safely.") }}

<div class="api-reference-clear"></div>
