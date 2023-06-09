# Importing Libraries
from pandasql import sqldf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Read Cleaned Data
data = pd.read_csv('cleaned_data.csv')


# Data Analysis
pysqldf = lambda q: sqldf(q, globals())

# Q1. Top 3 Highest Selling Players
query = 'SELECT TEAM, PLAYER, NATIONALITY, TYPE, PRICE_PAID FROM data ORDER BY PRICE_PAID DESC LIMIT 3'
print(pysqldf(query))

# Q2. Spendings of Teams
query = 'SELECT TEAM, SUM(PRICE_PAID)/10e6 AS SPENDATURE_IN_CR FROM data GROUP BY TEAM ORDER BY SUM(PRICE_PAID) DESC'
print(pysqldf(query))

# Q3. Highest Selling Player From Each Type
query = 'SELECT TEAM, PLAYER, NATIONALITY, TYPE, PRICE_PAID FROM data WHERE (TYPE, PRICE_PAID) IN (SELECT TYPE, MAX(PRICE_PAID) AS PRICE_PAID FROM data GROUP BY TYPE)'
print(pysqldf(query))

# Q4. % Of Price Paid For Indian vs Overseas
query = 'SELECT NATIONALITY, ROUND(CAST(SUM(PRICE_PAID) AS FLOAT)*100/(SELECT SUM(PRICE_PAID) FROM data), 2) AS PERCENT_SPENDATURE FROM data GROUP BY NATIONALITY'
print(pysqldf(query))

# Q5. Top 3 Highest Selling Indian Players
query = 'SELECT * FROM (SELECT TEAM, PLAYER, NATIONALITY, TYPE, PRICE_PAID, RANK() OVER(PARTITION BY NATIONALITY ORDER BY PRICE_PAID DESC) AS RANK FROM data) WHERE RANK < 4'
print(pysqldf(query))

# Q6. Total Amount Spent
query = 'SELECT SUM(PRICE_PAID) AS TOTAL_SPENDATURE FROM data'
print(pysqldf(query))

# Q7. Number Of Player Brought By Each Team
query = 'SELECT TEAM, COUNT(PLAYER) AS NUM_BOUGHT FROM data GROUP BY TEAM'
print(pysqldf(query))