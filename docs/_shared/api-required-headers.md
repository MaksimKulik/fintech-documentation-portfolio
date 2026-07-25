<!--
Standard API request headers shared by endpoint pages.

Pages render this file through {{ api_required_headers() }}.
To update standard headers everywhere that uses this shared component, edit the table below.

Table rules:
- Keep the columns in this exact order: name, type, format, requirement, description.
- Leave the format cell empty when a header has no format.
- Use requirement values such as required or optional.
- Do not remove the table header row or separator row.
-->

| name | type | format | requirement | description |
| --- | --- | --- | --- | --- |
| X-Api-Key-Id | string | uuid | required | API key identifier issued for the merchant integration. |
| X-Signature | string |  | required | Request signature generated from the HTTP method, request path without query string, raw request body, and timestamp. |
| X-Timestamp | integer | int64 | required | Unix epoch timestamp in seconds used in the signature base string. |
