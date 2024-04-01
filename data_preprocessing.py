import snowflake.connector
import pandas as pd

def preprocess_sales_data():
    # Connect to Snowflake
    # Fill in credentials of your account

    conn = snowflake.connector.connect(
        user='****',
        password='****',
        account='****',
        warehouse='COMPUTE_WH',
        database='E_COMMERCE_DATABASE',
        schema='PUBLIC',
        role='ACCOUNTADMIN'
    )

    # Execute a SQL query to retrieve data
    query = "SELECT USERID, PRODUCTID, RATING, TIMESTAMP FROM SALES_DATA"
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch data into a DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    # Close connection
    conn.close()

    # Data Preprocessing
    # Drop any duplicate rows if present
    df.drop_duplicates(inplace=True)

    # Convert TIMESTAMP column to datetime format
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'], unit='s')

    return df
