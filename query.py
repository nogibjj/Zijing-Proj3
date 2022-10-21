#!/usr/bin/env python

import click
from dblib.querydb import find_N_most_pay, find_job_avg_salary

# build a click group
@click.group()
def cli():
    pass


# build a click command
@click.command()
@click.option("--n", default=5, help="Most N paid job, default 5")
def query_most_N(n):
    """Find N most pay job"""
    find_N_most_pay(n)


@click.command()
def query_job_avg_salary():
    """Find job average salary"""
    find_job_avg_salary()


# run the command
if __name__ == "__main__":
    cli.add_command(query_most_N)
    cli.add_command(query_job_avg_salary)
    cli()
