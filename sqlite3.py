import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd
# connect the databse to the factbook
con = sq3.Connection('factbook.db') #path

# enitre facts
query = """
SELECT *
FROM facts;
"""
observations = pd.read_sql(query,con)
print(observations)

# reads in all data from the table sqlite_master
tables = pd.read_sql('SELECT * FROM sqlite_master', con)
print(tables)

# Min and max of population/ growth
query2 = """
SELECT MIN(population) AS min_pop,
       MAX(population) AS max_pop,
       MIN(population_growth) AS min_pop_growth,
       MAX(population_growth) max_pop_growth 
  FROM facts;
"""
print(pd.read_sql(query2,con))

# Outlier
query3 = """
SELECT *
  FROM facts
 WHERE population == (SELECT MIN(population)
                        FROM facts
                     );
"""
print(pd.read_sql(query3,con)) # min

query4 = """
SELECT *
  FROM facts
 WHERE population == (SELECT MIN(population)
                        FROM facts
                     );
"""
print(pd.read_sql(query4,con)) # max

#densely populated countries where pop abover avg and area under avg without outlier world
query5 = """
SELECT *
  FROM facts
 WHERE population > (SELECT AVG(population)
                       FROM facts
                      WHERE name <> 'World'
                    )
   AND area < (SELECT AVG(area)
                 FROM facts
                WHERE name <> 'World'
);
"""
print(pd.read_sql(query4,con))

