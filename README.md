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
![Code5](/images/code5.png)

Climate Analysis: Obtain the last 12 months of precipitation data, convert into a data frame, and plot a bar chart.
![Code2](/images/code2.png)

![Precipitation](/images/precip.png)


Station Analysis: Calculate the total number of stations, find the most active stations by the highest number of observations, obtain the last 12 months of temperature data for the most active station, convert to a data frame and plot a histogram.
![Code3](/images/code3.png)

![Temperature](/images/temp.png)

## Flask API Design

Design a Flask API based on the queries that were developed during the climate analysis.

NOTE: dependencies and set-up were identical to the climate analysis overview except for the engine and session creation.
![Flask](/images/flask.png)
