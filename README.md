# Data Script with Databricks

![example workflow](https://github.com/nogibjj/Zijing-codespcase/actions/workflows/main.yml/badge.svg)

This is Zijing's project 1 repo, which contains a big data script that use Databricks API and Streamlit app to show word cloud for job salary analysis. 

Demo link: https://github.com/nogibjj/Zijing-codespcase/blob/main/video3571322614.mp4

Dataset: https://www.kaggle.com/code/raghurayirath/plotly-data-science-job-salary-dataset-eda/data

## Project Structure
![image](https://github.com/nogibjj/Zijing-codespcase/blob/main/structure.jpg)

## Test CLI
```linux
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```

## CLI Query 
  `query-job-avg-salary`  Find job average salary

  `query-most-n`    --n      Find N most pay job, default=5

```linux
chmod +x query.py
./query.py query-most-n --n 5 
./query.py query-job-avg-salary
```

## Microservice
```linux
streamlit run app.py --server.enableCORS=false
```
