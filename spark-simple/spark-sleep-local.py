from pyspark.sql import SparkSession
from time import sleep

# Start local Spark instance - no session context provided
spark = SparkSession.builder.appName("spark-python-sleep").getOrCreate()

# Wait 5 minutes
minutes = 5
print("=====> Start: Sleep for (%i) minutes. <=====" % minutes)
sleep(minutes * 60)
print("=====> Stop: Sleep for (%i) minutes. <=====" % minutes)

# Stop local Spark instance
spark.stop()
