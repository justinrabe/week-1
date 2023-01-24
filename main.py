import pandas as pd
import argparse
import requests
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
import io





def main(params):
    print(params)
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = 'ny_taxi'
    df =  pd.read_csv('taxi+_zone_lookup.csv', nrows=100)
    ##table_name = params.table_name
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')

    args = parser.parse_args()

    main(args)