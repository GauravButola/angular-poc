### Prerequisite
Postgres, python, npm

### Steps to run

```
pip install -r requirements.txt

# Load CSV into db
DB_NAME=<db_name> DB_USER=<user> python csv_to_sql.py

# Run API server
cd web && DB_NAME=<db_name> DB_USER=<user> python app.py

# Run ng server
npm install
ng serve
```
