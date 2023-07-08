# MySQL Terraform Provider https://registry.terraform.io/providers/nkhanal0/mysql/latest/docs

terraform {
    required_providers {
        mysql = {
            source = "nkhanal0/mysql"
            version = "2.0.3"
        }
    }
}

# DB endpoint
# TODO: Secrets manager or env variables for "username" & "password" 
provider "mysql" {
    endpoint = "localhost:3306"
    username = "root"
    password = "PASSWORD"
}
