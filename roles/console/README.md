# console

This role deploys the console (web UI) for metal-stack-cloud. It deploys a Kubernetes Deployment and Service for the console frontend.

## Variables

| Name                                   | Mandatory | Description                                                         |
| -------------------------------------- | --------- | ------------------------------------------------------------------- |
| `console_namespace`                    |           | Kubernetes namespace for console deployment                         |
| `console_replicas`                     |           | Number of console replicas (default: `3`)                           |
| `console_api_url`                      |           | URL of the api-server instance                                      |
| `console_api_auth_callback_url`        |           | OAuth callback URL for api authentication                           |
| `console_api_auth_test_callback_url`   |           | OAuth test callback URL                                             |
| `console_stripe_public_key`            |           | Stripe public API key                                               |
| `console_open_auth_test`               |           | Enable open auth mode for testing (default: `false`)                |
| `console_show_azure_login`             |           | Show Azure login button (default: `false`)                          |
| `console_show_google_login`            |           | Show Google login button (default: `false`)                         |
| `console_show_oidc_provider_login`     |           | Show OIDC login button (default: `false`)                           |
| `console_debug_mode`                   |           | Enable debug mode (default: `true`)                                 |
| `console_email_consent`                |           | Require email consent (default: `false`)                            |
| `console_show_outage_banner`           |           | Show outage banner (default: `false`)                               |
| `console_show_survey`                  |           | Show survey prompt (default: `false`)                               |
| `console_ingress_dns`                  |           | DNS name for the console ingress                                    |
| `console_httproute_parent_refs`        |           | List of `parentRefs` (Gateways) the console's HTTPRoute attaches to |
| `metal_stack_cloud_console_image_name` |           | Image name for console container                                    |
| `metal_stack_cloud_console_image_tag`  |           | Image tag for console container                                     |
| `metal_stack_cloud_user_admittance`    |           | Enable/disable user registration                                    |
| `metal_stack_cloud_disable_billing`    |           | Enable/disable billing functionality                                |
