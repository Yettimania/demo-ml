# etl example

This `main.py` is designed as an ETL to process the sample `data.csv` file with the end destination being the MySQL database that was configured in the `../infrastructure` folder.

The transform creates two new fields from the base record which are `get_fullname` and `get_domain`. These are simple transorms to the data which reflect the potential for more advanced feature engineering. 

Logs for the `main.py` are stored in the `/logs`.

## Future Work

- Utilize IP address to capture geographic location

# Prerequisites

`direnv` is used to set environemtnal variables that are used in the `main.py` in order to make the database connection.

- `direnv`: Extensions of the shell to provide directory based environmental variables. [Link](https://direnv.net/)

# Usage

Create a virtual env using the `just venv` command.

Activate the virtual env with `source ./venv/bin/activate`

The `just install` command will install all the requirements into the virtual environment.

`just run` will execute the python script and record a timestamped log into the logs folder.
