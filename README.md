# SQL Script

![example workflow](https://github.com/nogibjj/Zijing-codespcase/actions/workflows/main.yml/badge.svg)

This is Zijing's project 3 repo, which contains a sql script with 5 queries built and connect to AWS Dynamodb database. Pandas library is also used in order to transform csv file in to the table in the database.

Demo link: https://github.com/nogibjj/Zijing-codespcase/blob/main/video3571322614.mp4

Dataset: https://www.kaggle.com/code/raghurayirath/plotly-data-science-job-salary-dataset-eda/data

## Project Structure
![image](https://github.com/nogibjj/Zijing-Proj3/blob/main/Structure.jpg)


## Main Feature
### Convert CSV file to json file
Convert ds_salaries.csv from Kaggle to json file to load into Dynamodb
### Create Table in Dynamodb
Create table salaries with schema
### Insert data into Dynamodb
Insert items into table
### Database Query 
- Query 1: Get first 5 items
- Query 2: Find jobs that pay more than $4000,000
- Query 3: Find data scientist job in DE
- Query 4: Find job in small company
- Query 5: Find job salary between $100,000 and $200,000

