from logging import error
from multiprocessing.context import set_spawning_popen
import os
from sre_parse import State
import boto3, json
import hashlib
from botocore.exceptions import ClientError
import pandas as pd

# Step 1: Create JSON file from CSV
def create_json_file():
    df = pd.read_csv('ds_salaries.csv')
    df.to_json('data.json')

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Step 2: Create table
def create_table():
    table = dynamodb.create_table(
        TableName='salaries',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='salaries')

# Step 3: Load data into table
def load_data():
    table = dynamodb.Table('salaries')
    print(table.table_status)
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data['id']:
            id = data['id'][p]
            employment_type = data['employment_type'][p]
            title = data['job_title'][p]
            location = data['company_location'][p]
            salary = data['salary'][p]
            company_size = data['company_size'][p]
            print("Adding data:", id, employment_type, title, location, salary, company_size)
            table.put_item(
                Item={
                    'id': id,
                    'employment_type': employment_type,
                    'title': title,
                    'location': location,
                    'salary': salary,
                    'company_size': company_size,
                }
            )


create_json_file()
create_table()
load_data()

# Step 4: Query data
session = boto3.session.Session()
client = session.client('dynamodb', region_name='us-east-1')

## Query 1: Get first 5 items
def query_first_five():
    response = client.execute_statement(
        Statement='SELECT * FROM salaries where id < 5',
    )
    # convert response to dataframe
    df = pd.DataFrame(response['Items'])
    print("Query 1: Get first 5 items")
    print(df)
## Query 2: Find jobs that pay more than $4000,000
def query_salary():
    response = client.execute_statement(
        Statement='SELECT title, salary FROM salaries where salary > 4000000',
    )
    # convert response to dataframe
    df = pd.DataFrame(response['Items'])
    print("Query 2: Find jobs that pay more than $4000,000")
    print(df)

## Query 3: Find data scientist job in DE
def query_data_scientist_DE():
    title = "Data Scientist"
    location = "DE"
    response = client.execute_statement(
        Statement= 'SELECT * FROM salaries WHERE title = ? AND location = ?',
        Parameters= [{"S": title}, {"S": location}]
    )
    # convert response to dataframe
    df = pd.DataFrame(response['Items'])
    print("Query 3: Find data scientist job in DE")
    print(df)

## Query 4: Find job in small company
def query_small_company():
    size = "S"
    response = client.execute_statement(
        Statement='SELECT title, salary FROM salaries where company_size = ?',
        Parameters= [{"S": size}]
    )
    # convert response to dataframe
    df = pd.DataFrame(response['Items'])
    print("Query 4: Find job in small company")
    print(df)

## Query 5: Find job salary between $100,000 and $200,000
def query_salary_range():
    response = client.execute_statement(
        Statement='SELECT title, salary FROM salaries where salary between 100000 and 200000',
    )
    # convert response to dataframe
    df = pd.DataFrame(response['Items'])
    print("Query 5: Find job salary between $100,000 and $200,000")
    print(df)

query_first_five()
query_salary()
query_data_scientist_DE()
query_small_company()
query_salary_range()
