
from faker import Faker
import random
import pandas as pd
#import psycopg2
#import postgreconn


fake = Faker()
#conn = psycopg2.connect("dbname= rstore_dw user=manager password=manager")
# conn = psycopg2.connect(dbname = "rstore_dw", 
#                         user = "postgres", 
#                         password = "manager",
#                         host = "localhost",
#                         port = "5432")

#cur = conn.cursor()



# for _ in range(100):
#     cur.execute("INSERT INTO product_dim (product_name, category, price) VALUES (%s, %s, %s)",
#             (fake.word(), fake.word(), round(random.uniform(10.0, 1000.0), 2)))
    
# for _ in range(10):
#     cur.execute("INSERT INTO store_dim (store_name, location) VALUES (%s, %s)",
#                 (fake.company(), fake.city()))

# for _ in range(5):
#     cur.execute("INSERT INTO customer_dim (customer_name, email, phone) VALUES (%s, %s, %s)",
#                 (fake.name(), fake.email(), fake.phone_number()))
    
# for _ in range(500):
#     cur.execute("INSERT INTO sales_fact (date_key, store_id, product_id, customer_id, quantity, total_amount) VALUES (%s, %s, %s, %s, %s, %s)",
#                 (fake.date_this_year(), random.randint(1, 4), random.randint(1, 5), random.randint(1, 4), random.randint(1, 10), round(random.uniform(10.0, 1000.0), 2)))





def generate_products(num_products):
    products = []
    for _ in range(num_products):
        product = {
            'product_id': _ + 1,
            'product_name': fake.word().capitalize(),
            'category': fake.word().capitalize()
        }
        products.append(product)
    return pd.DataFrame(products)

products_df = generate_products(50)
print(products_df.head())


def generate_customers(num_customers):
    customers = []
    for _ in range(num_customers):
        customer = {
            'customer_id': _ + 1,
            'customer_name': fake.name(),
            'email': fake.email()
        }
        customers.append(customer)
    return pd.DataFrame(customers)

customers_df = generate_customers(100)
print(customers_df.head())


def generate_stores(num_stores):
    stores = []
    for _ in range(num_stores):
        store = {
            'store_id': _ + 1,
            'store_name': fake.company(),
            'location': fake.city()
        }
        stores.append(store)
    return pd.DataFrame(stores)

stores_df = generate_stores(10)
print(stores_df.head())


def generate_time_series(start_date, end_date):
    dates = pd.date_range(start=start_date, end=end_date).to_pydatetime().tolist()
    time_data = []
    for date in dates:
        time_data.append({
            'date': date.date(),
            'year': date.year,
            'month': date.month,
            'day': date.day
        })
    return pd.DataFrame(time_data)

time_df = generate_time_series('2023-01-01', '2023-12-31')
print(time_df.head())






def generate_sales(num_sales, products_df, customers_df, stores_df, time_df):
    sales = []
    for _ in range(num_sales):
        sale = {
            'sale_id': _ + 1,
            'product_id': random.choice(products_df['product_id']),
            'customer_id': random.choice(customers_df['customer_id']),
            'store_id': random.choice(stores_df['store_id']),
            'sale_date': random.choice(time_df['date']),
            'amount': round(random.uniform(10.0, 500.0), 2),
            'quantity': random.randint(1, 10)
        }
        sales.append(sale)
    return pd.DataFrame(sales)

sales_df = generate_sales(500, products_df, customers_df, stores_df, time_df)
print(sales_df.head())










# conn.commit()
# cur.close()
# conn.close()

#-----------------------------------------------------------------------------------------
# from sqlalchemy import create_engine

# # Database connection parameters
# db_user = 'your_user'
# db_password = 'your_password'
# db_host = 'localhost'
# db_port = '5432'
# db_name = 'retail_sales'

# # Create database connection
# engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# # Load data into PostgreSQL
# def load_data_to_postgres(df, table_name):
#     df.to_sql(table_name, engine, if_exists='replace', index=False)

# # Load each table
# load_data_to_postgres(products_df, 'products')
# load_data_to_postgres(customers_df, 'customers')
# load_data_to_postgres(stores_df, 'stores')
# load_data_to_postgres(time_df, 'time')
# load_data_to_postgres(sales_df, 'sales')

#-------------------------------------------------------------------------------------------------