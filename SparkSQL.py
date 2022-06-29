from pyspark.sql import SQLContext

sqlCtx = SQLContext(sc)

df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')
