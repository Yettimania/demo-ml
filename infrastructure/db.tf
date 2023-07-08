# Configure DB within MySQL Instance

resource "mysql_database" "demo_etl" {
    name = "demo_etl"
}

# Create a user within the database
# TODO: Best practice is to use more secure password method.
resource "mysql_user" "ksnyder" {
    user = "ksnyder"
    host = "localhost"
    plaintext_password = "password"
}

# Grant privileges to the user
# TODO: Best practice 'Practice of Least Privelages' giving
# user only necessary privileges versus 'ALL'
resource "mysql_grant" "ksnyder" {
    user = "${mysql_user.ksnyder.user}"
    host = "${mysql_user.ksnyder.host}"
    database = "demo_etl"
    privileges = ["ALL"]
}
