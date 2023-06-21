from pyspark.sql import *
from pyspark.sql import SparkSession as ss
from pyspark.sql.functions import *

spark = ss.builder.appName("firstApp").master("local[*]").getOrCreate()
data = 'orgs.csv'
df = spark.read.format("CSV").option("header","true").load(data)
# df.show()
#process sql friendly
df.createOrReplaceTempView("tab")
#ur giving one name to the dataframe called tab... with the help of createOrReplaceTempView ... u can run any sql queries on top of dataframe

#res=spark.sql("select * from tab where city='blr' and age<30")
res=spark.sql("select Name,Website,Founded from tab group by Founded")
res.show()
