from databricks import sql
import os


def querydb(query):
    with sql.connect(
        server_hostname=os.getenv("DATABRICK_HOST"),
        http_path=os.getenv("DATABRICK_HTTP_PATH"),
        access_token=os.getenv("DATABRICK_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result


def find_N_most_pay(N):
    query = f"select salary, job_title from ds_salaries order by int(salary) desc limit {N};"
    return querydb(query)


def find_job_avg_salary():
    query = "select distinct AVG(int(salary)) over (partition  by job_title) as avg_salary, job_title from ds_salaries order by avg_salary desc;"
    return querydb(query)
