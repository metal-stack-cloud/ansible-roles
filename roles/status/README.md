# status

This role deploys the status/health dashboard for metal-stack-cloud. It provides a public-facing status page showing the health of the platform.

## Variables

| Name                           | Mandatory | Description                                                                  |
| ------------------------------ | --------- | ---------------------------------------------------------------------------- |
| `status_namespace`             |           | Kubernetes namespace for status deployment                                   |
| `status_replicas`              |           | Number of status replicas (default: `2`)                                     |
| `status_api_url`               |           | URL of the api-server instance                                               |
| `status_api_token`             |           | API token for status dashboard authentication                                |
| `status_server_url`            |           | Public URL for the status page                                               |
| `status_log_level`             |           | Log level (default: `info`)                                                  |
| `status_schedule`              |           | Planned maintenance schedule                                                 |
| `status_ingress_dns`           |           | DNS name for the status ingress                                              |
| `status_httproute_parent_refs` |           | List of `parentRefs` (Gateways) the status dashboard's HTTPRoute attaches to |
| `status_chat_channel_id`       |           | Slack channel ID for status notifications (via env `SLACK_CHANNEL_ID`)       |
| `status_chat_token`            |           | Slack API token for status notifications (via env `SLACK_TOKEN`)             |
