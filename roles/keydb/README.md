# keydb

This role deploys KeyDB using the official Helm chart from the [Enapter charts repository](https://github.com/enapter/charts). KeyDB is used for token storage in the metal-stack-cloud api-server.

## Variables

| Name                  | Mandatory | Description                                       |
| --------------------- | --------- | ------------------------------------------------- |
| `keydb_namespace`     |           | Kubernetes namespace for KeyDB deployment         |
| `keydb_chart_repo`    |           | Helm chart repository URL (default: Enapter repo) |
| `keydb_chart_version` |           | Helm chart version                                |
| `keydb_nodes`         |           | Number of KeyDB cluster nodes (default: `3`)      |
| `keydb_password`      |           | Password for KeyDB authentication                 |
| `keydb_size`          |           | Persistent volume size per node (default: `10Gi`) |
