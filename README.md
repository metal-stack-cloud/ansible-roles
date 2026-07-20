# metal-stack-cloud-ansible-roles

This repository contains Ansible roles for deploying [metal-stack-cloud](https://github.com/metal-stack/metal-stack-cloud). It does not contain any specific playbooks.

The roles in this repository are used to deploy the various microservices of the metal-stack-cloud platform onto a Kubernetes cluster:

- [defaults](roles/defaults) - Global default variables for all roles (image mappings, global settings)
- [accounting](roles/accounting) - NSQ-based accounting service for usage tracking and reporting
- [api-server](roles/api-server) - Core REST API server with authentication, billing, and token management
- [console](roles/console) - Web-based user interface for managing Kubernetes clusters, ...
- [keydb](roles/keydb) - KeyDB (Redis-compatible) deployment for token storage
- [status](roles/status) - Status/health dashboard service

## Releases & Ansible Role Dependencies

metalstack.cloud relies on a release vector for resolving image versions at runtime. The setup is documented in the [metal-stack deployment guide](https://metal-stack.io/docs/deployment-guide#releases-and-ansible-role-dependencies).

Since it is assumed metal-stack is deployed alongside metalstack.cloud, the release vector mapping is shared between both projects.

## Variables

There are [global defaults](./roles/defaults/defaults/main/) for all roles of this project defined.

| Name                                     | Mandatory | Description                                   |
| ---------------------------------------- | --------- | --------------------------------------------- |
| `metal_stack_cloud_namespace`            |           | The Kubernetes namespace for deployment       |
| `metal_stack_cloud_ingress_dns`          |           | The base DNS name used for all ingress routes |
| `metal_stack_cloud_stripe_private_token` |           | Stripe private API key                        |
| `metal_stack_cloud_stripe_public_token`  |           | Stripe public API key                         |
| `metal_stack_cloud_user_admittance`      |           | Whether user registration is enabled          |
| `metal_stack_cloud_disable_billing`      |           | Whether billing functionality is disabled     |
