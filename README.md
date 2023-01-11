# Data Exploration using SQLAlchemy and Flask

## Background

Use Python and SQLAlchemy to do basic climate analysis and data exploration of a Hawaii climate database that contains precipitation and temperature observations across 9 stations. Once the analysis is complete, design a Flask API based on SQLAlchemy ORM queries.

## Purpose

- Python and SQLAlcemy were used to explore the data and do temperature and precipitation analysis.
- The precipitation and temperature data was collected using monitoring stations in Hawaii and stored in a SQLite database.

## Data Source

[hawaii.sqlite](/hawaii.sqlite)

## Tools

Python: SQLAlchemy ORM Queries, Pandas, and Matplotlib libraries; APIs; Flask
The Flask applicaiton was created so that the climate data can be accessible via API calls.

## Data Analysis and Exploration

First, set up base, create classes for each table, and connect to the sqlite database.
![Code1](/images/code1.png)

Climate Analysis: Obtain the last 12 months of precipitation data, convert into a data frame, and plot a bar chart.
![Code2](/images/code2.png)

![Precipitation](/images/precip.png)


![Temperature](/images/temp.png)
