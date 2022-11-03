import pandas as pd
import sqlite3

# load the data into a Pandas DataFrame
def load_write_data(database_name, routes_csv, cities_csv):
    conn = sqlite3.connect(database_name)
    routes_db = pd.read_csv(routes_csv)
    cities_db = pd.read_csv(cities_csv)
    # write the data to a sqlite table
    routes_db.to_sql(routes_csv, conn, if_exists='replace', index = False)
    cities_db.to_sql(cities_csv, conn, if_exists='replace', index = False)
