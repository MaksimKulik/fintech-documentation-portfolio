# Configure Payment Routing

Payment routing determines which service processes an order. A routing schema evaluates order attributes, follows the first matching branch, and applies that branch's selection strategy.

!!! info "Before you begin"
    Confirm that every service included in the schema supports the payment method, currency, and country used by the incoming order.

## How routing is evaluated

The following schema sends USD orders through two services in priority order. Orders in other currencies follow the fallback branch and go directly to a third service.

<div class="routing-map" role="img" aria-label="A payment order is evaluated by a currency criterion. USD orders use an ordered strategy with two services. Other currencies use a direct strategy with one service.">
  <div class="routing-map__track">
    <div class="routing-map__node"><strong>Payment order</strong><span>amount, currency, method</span></div>
    <span class="routing-map__arrow" aria-hidden="true">&#8594;</span>
    <div class="routing-map__node routing-map__node--criterion"><strong>Currency criterion</strong><span>currency = USD?</span></div>
  </div>
  <div class="routing-map__branches">
    <div class="routing-map__branch">
      <div class="routing-map__node"><strong>USD branch</strong><span>condition matched</span></div>
      <span class="routing-map__arrow" aria-hidden="true">&#8594;</span>
      <div class="routing-map__node routing-map__node--strategy"><strong>By order</strong><span>Service A, then B</span></div>
    </div>
    <div class="routing-map__branch routing-map__branch--fallback">
      <div class="routing-map__node"><strong>Fallback branch</strong><span>all other values</span></div>
      <span class="routing-map__arrow" aria-hidden="true">&#8594;</span>
      <div class="routing-map__node routing-map__node--strategy"><strong>Direct</strong><span>Service C</span></div>
    </div>
  </div>
  <p class="routing-map__caption">A branch may contain another criterion when a second decision is required.</p>
</div>

Routing proceeds from the root of the schema to a terminal strategy:

1. The platform reads the order attributes required by the first criterion.
2. It follows the first matching branch. If none matches, it uses the fallback branch.
3. It applies the branch strategy to select an eligible service.
4. If the strategy supports failover, it tries the next eligible service after a retriable failure.

!!! warning "Always define a fallback"
    Without a fallback branch, an unexpected value can leave an otherwise valid order without a route. Treat the fallback as an explicit operational decision, not a catch-all added at the end.

## Build the schema

<div class="step-list">
  <div class="step-list__item">
    <strong>Add the root criterion</strong>
    <p>Choose an attribute that reliably separates the main processing paths, such as currency, country, amount range, or payment method.</p>
  </div>
  <div class="step-list__item">
    <strong>Define branches</strong>
    <p>Enter the values or ranges handled by each branch, then add one fallback branch for all remaining values.</p>
  </div>
  <div class="step-list__item">
    <strong>Assign a strategy</strong>
    <p>Select how the platform chooses between eligible services and arrange the services in the intended processing order.</p>
  </div>
  <div class="step-list__item">
    <strong>Validate with representative orders</strong>
    <p>Test the common path, every explicit branch, the fallback, and at least one failover scenario before activation.</p>
  </div>
</div>

## Strategy reference

| Strategy | Selection behavior | Best used when |
| --- | --- | --- |
| `DIRECT` | Sends every matching order to one service. | A route has one required processor. |
| `BY_ORDER` | Tries eligible services in configured priority order. | Stable preference and controlled failover are required. |
| `RANDOM` | Selects from eligible services without a fixed priority. | Traffic may be distributed across equivalent services. |

!!! example "Worked check"
    An order with `currency = USD` reaches the USD branch. The `BY_ORDER` strategy first tries Service A. If Service A returns a configured retriable failure, the platform tries Service B. A EUR order skips this branch and uses the fallback route to Service C.

## Review before activation

- Every branch ends in a strategy.
- A fallback exists at each criterion level.
- Service capabilities match the branch conditions.
- Failover includes only failures that are safe to retry.
- A test order reaches every terminal service at least once.

{{ api_page_link(
  title="Create a payment through the API",
  href="../../api/create-payment/",
  icon="card",
  description="See how the selected route is invoked from an endpoint."
) }}

