from sqlalchemy import create_engine
from Gendata import *

# Database connection parameters
db_user = 'postgres'
db_password = 'manager'
db_host = 'localhost'
db_port = '5432'
db_name = 'rstore_dw'

# Create database connection
#engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')



# Load data into PostgreSQL
def load_data_to_postgres(df, table_name):
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# Load each table
load_data_to_postgres(products_df, 'products')
load_data_to_postgres(customers_df, 'customers')
load_data_to_postgres(stores_df, 'stores')
load_data_to_postgres(sales_df, 'sales')
load_data_to_postgres(time_df, 'time')
