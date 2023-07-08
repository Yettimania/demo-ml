# demo-ml

Demo repo highlighting practices of DE/DS

'infrastructure' - Terraform for managing MySQL instance.
'etl' - Python script to extract, transform and load data into the MySQL database.
'api' - ML Model Deployment using the Iris dataset

See the specific `README.md` within the respective directory.

## Prerequisites

These are the recommended prerequisites to work within the `demo-ml` monorepo.

- `just` - (Suggested) Command line runner for project specific commands. One of my favorite tools. This is not required and if not installed, the equivalent cli commands can be found in the `justfile` [just repo](https://github.com/casey/just)
- `direnv` - Set local environmental variables based on path. Great for monorepo or isolated directories as such in this demo repo. [direnv](https://direnv.net/)
- `terraform` - Manage DB through Infrastructure as Code
