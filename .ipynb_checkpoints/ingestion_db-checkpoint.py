import pandas as pd
import os
import time
import logging

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

logging.basicConfig(
    filename="logs/vendor_analysis.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def get_engine():
    return create_engine(
        "mysql+mysqlconnector://root:monika@127.0.0.1:3306/vendor_analysis"
    )

def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''

    try:

        # clean column names
        df.columns = df.columns.str.replace(
            '[^A-Za-z0-9_]',
            '',
            regex=True
        )

        # load into mysql
        with engine.begin() as conn:

            df.to_sql(
                table_name,
                con=conn,
                if_exists='replace',
                index=False,
                chunksize=1000
            )

        logging.info(f"{table_name} loaded successfully")
        print(f"{table_name} loaded successfully")

    except SQLAlchemyError as e:

        logging.error(f"Failed loading {table_name}")
        logging.error(e)

        print(f"Failed loading {table_name}")
        print(e)

def load_raw_data():
    '''this function will load the CSVs as dataframe and ingest into db'''

    start = time.time()

    # create engine once
    engine = get_engine()

    try:

        for file in os.listdir('data'):

            if file.endswith('.csv'):

                df = pd.read_csv('data/' + file)

                logging.info(f'Ingesting {file} in db')

                ingest_db(df, file[:-4], engine)

        logging.info('---------------------Ingestion Complete----------------------')

    except Exception as e:

        logging.error(e)
        print(e)

    finally:

        end = time.time()

        total_time = (end - start) / 60

        logging.info(f'Total Time Taken: {total_time:.2f} minutes')

        # close connection
        engine.dispose()

if __name__ == '__main__':
    load_raw_data()