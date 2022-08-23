"""This is an example of a simple ETL pipeline and it omits many best practices (e.g. logging, error handling,
parameterizatin + config files, etc.) due to time constraints
"""

from api_data import api_data
from db_queries import create_covid_data_table, insert_covid_data_table
from db import db

def main():
    apidata = api_data(ENDPOINT)
    database = db()
    database.setup()
    queries = [insert_covid_data_table.format((result)) for result in apidata.final_data()]
    query_to_execute = "BEGIN; \n" + '\n'.join(queries) + "\nCOMMIT;"
    db.execute_query(query_to_execute)

if __name__ == "__main__":
        main()