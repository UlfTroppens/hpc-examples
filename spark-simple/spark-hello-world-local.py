# Derived from Spark Quickstart Guide
# https://spark.apache.org/docs/latest/quick-start.html#self-contained-applications
from pyspark.sql import SparkSession
from time import sleep

# Textfile that exists on your server
myFile = "/hpclab/users/ulf/hpc-examples/README.md"

# Start local Spark instance - no session context provided
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

# Load text file
myData = spark.read.text(myFile).cache()

# Analyze text file
numAs = myData.filter(myData.value.contains('a')).count()
numBs = myData.filter(myData.value.contains('b')).count()
print("=====> Lines with a: %i, lines with b: %i <=====" % (numAs, numBs))

# Wait 5 minutes
minutes = 5
print("=====> Start: Sleep for (%i) minutes. <=====" % minutes)
sleep(minutes * 60)
print("=====> Stop: Sleep for (%i) minutes. <=====" % minutes)

# Stop local Spark instance
spark.stop()
