# accounting

This role deploys the accounting stack for metal-stack-cloud. It includes NSQ (message queue) deployment and the accounting service itself, which handles usage tracking and reporting.

## Variables

| Name                                                           | Mandatory | Description                                                        |
| -------------------------------------------------------------- | --------- | ------------------------------------------------------------------ |
| `accounting_namespace`                                         |           | Kubernetes namespace for accounting deployment                     |
| `accounting_log_level`                                         |           | Log level (default: `info`)                                        |
| `accounting_log_only`                                          |           | If true, only log usage records without sending them (for testing) |
| `accounting_deployment_admin_token`                            |           |                                                                    |
| `accounting_metal_apiserver_url`                               |           | URL of the metal-apiserver endpoint                                |
| `accounting_metal_apiserver_token_expiration`                  |           | The token expiration of the metal-apiserver token                  |
| `accounting_metal_apiserver_token_permissions`                 |           | The token permissions of the metal-apiserver token                 |
| `accounting_metal_apiserver_token_refresher_image_name`        |           | The metal-token-refresher image name                               |
| `accounting_metal_apiserver_token_refresher_image_tag`         |           | The metal-token-refresher image tag                                |
| `accounting_metal_apiserver_token_refresher_image_pull_policy` |           | The metal-token-refresher pull policy                              |
| `accounting_metal_apiserver_token_refresher_resources`         |           | The metal-token-refresher resources                                |
| `accounting_metal_apiserver_token_refresher_schedule`          |           | The metal-token-refresher cronjob schedule                         |
| `accounting_api_url`                                           |           | URL of the api-server instance                                     |
| `accounting_api_token`                                         |           | Token for authenticating with the api-server                       |
| `accounting_tenant_apiserver_url`                              |           | Url of the tenant-apiserver                                        |
| `accounting_stripe_private_token`                              |           | Stripe private token for accounting sender                         |
| `accounting_nsqd_address`                                      |           | NSQ daemon address                                                 |
| `accounting_nsq_set_resource_limits`                           |           | Whether to set resource limits for NSQ pods                        |
| `accounting_nsq_nsqd_resources`                                |           | Resource requests/limits for nsqd pods                             |
| `accounting_nsq_log_level`                                     |           | NSQ log level                                                      |
| `accounting_nsq_nsqd_data_size`                                |           | Data size for nsqd disk storage                                    |
| `accounting_nsq_image_pull_policy`                             |           | Image pull policy for NSQ containers                               |
