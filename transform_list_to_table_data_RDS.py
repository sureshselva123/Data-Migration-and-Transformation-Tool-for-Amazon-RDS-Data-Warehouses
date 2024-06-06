import pandas as pd
import boto3
import json
import pymysql
import mysql.connector
from sqlalchemy import create_engine 
from sqlalchemy import text 

# Replace the placeholders with your AWS credentials
aws_access_key_id = "AKIA4MTWLZQBMV4UCEUF"
aws_secret_access_key = "NPXsG/1px+eNcb6kpKQM+dw6c9b8572JHRPrwelD"
bucket_name = "datamigrationaws"
folder_name = "data/"

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Initialize an empty list to store dictionaries
data_list = []

# Iterate through the objects in the specified folder in S3
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
for obj in response['Contents']:
    file_key = obj['Key']
    response = s3.get_object(Bucket=bucket_name, Key=file_key)

    try:
        data = json.loads(response['Body'].read().decode('utf-8'))
        data_list.append(data)
    except Exception as e:
        print(f"Error processing file {file_key}: {e}")

# Flatten the nested structure of the JSON data
flattened_data = []
for data in data_list:
    flattened_data.append({
        'cik': data['cik'],
        'entityType': data['entityType'],
        'sic': data['sic'],
        'sicDescription': data['sicDescription'],
        'insiderTransactionForOwnerExists': data['insiderTransactionForOwnerExists'],
        'insiderTransactionForIssuerExists': data['insiderTransactionForIssuerExists'],
        'name': data['name'],
        'street1': data['addresses']['business']['street1'],
        'street2': data['addresses']['business']['street2'],
        'city': data['addresses']['business']['city'],
        'stateOrCountry': data['addresses']['business']['stateOrCountry'],
        'zipCode': data['addresses']['business']['zipCode'],
        'stateOrCountryDescription': data['addresses']['business']['stateOrCountryDescription']
    })

# Create a DataFrame from the flattened data
df = pd.DataFrame(flattened_data)

# Replace the placeholders with your MySQL connection details
# Step 4: Load Data into Amazon RDS
# Connect to your Amazon RDS instance
connection = mysql.connector.connect(
    host="swathidb1.c3gy2i8oqu9v.us-west-2.rds.amazonaws.com",
    username="admin",
    password="Suresh123",
    database="mydatabase",
    port="3306"
)
cursor = connection.cursor()

# Create the connection string
#connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

# Create the SQLAlchemy engine
#engine = create_engine(connection_string)

# Replace "table_name" with the name of the table you want to insert the data into
table_name = "url_data"
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    cik VARCHAR(255),
    entityType VARCHAR(255),
    sic VARCHAR(255),
    sicDescription VARCHAR(255),
    insiderTransactionForOwnerExists VARCHAR(255),
    insiderTransactionForIssuerExists VARCHAR(255),
    name VARCHAR(255),
    street1 VARCHAR(255),
    street2 VARCHAR(255),
    city VARCHAR(255),
    stateOrCountry VARCHAR(255),
    zipCode VARCHAR(255),
    stateOrCountryDescription VARCHAR(255)
);
"""


# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Commit the changes
connection.commit()

# Insert data into the table
for index, row in df.iterrows():
    insert_query = '''
        INSERT INTO url_data (cik, entityType, sic, sicDescription,
       insiderTransactionForOwnerExists, insiderTransactionForIssuerExists,
       name, street1, street2, city, stateOrCountry, zipCode,
       stateOrCountryDescription)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    '''
    # Execute the INSERT INTO query
    cursor.execute(insert_query, (row['cik'], row['entityType'], row['sic'],row['sicDescription'], row['insiderTransactionForOwnerExists'], row['insiderTransactionForIssuerExists'], row['name'], row['street1'], row['street2'], row['city'], row['stateOrCountry'],row['zipCode'], row['stateOrCountryDescription']))

# Commit the changes
connection.commit()

# Close cursor and database connection
cursor.close()
connection.close()
