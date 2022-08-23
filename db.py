import psycopg2
from db_queries import create_covid_data_table
class db:

    def __init__(self):
        self._conn = psycopg2.connect(host="::1",dbname="ARC_insights_dp",user="postgres",password="1234")
        self._conn.autocommit = True
        self._cur = self._conn.cursor()

    def execute_query(self, query):
        self._cur.execute(query)

    def setup(self):
        self.execute_query(create_covid_data_table)



