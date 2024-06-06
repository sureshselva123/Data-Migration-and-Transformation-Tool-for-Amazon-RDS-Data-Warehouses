# Data-Migration-and-Transformation-Tool-for-Amazon-RDS-Data-Warehouses
Data Migration and Transformation Tool for Amazon RDS Data Warehouses

You have a URL that points to a zip file. The zip file contains multiple JSON files. The JSON files contain multiple documents with various data structures. Your goal is to download the zip file from the URL, extract the data from the JSON files, store it in Amazon S3, and load it into Amazon RDS. You want to use Python or PySpark to perform these tasks. You may use any libraries or tools that are necessary to complete the task.
Approach:
To extract the data from a zip file that is available at a URL and load it into Amazon S3 and Amazon RDS (NoSQL), you can follow these steps: 
Use the requests library to download the zip file from the URL.
Use the zipfile module to extract the data from the zip file.
Use the boto3 library or PySpark to store the data in Amazon S3.
Use the pandas library and sqlalchemy or PySpark to load the data from S3 into Amazon RDS (NoSQL).

