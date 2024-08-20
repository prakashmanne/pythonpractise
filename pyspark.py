from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data
data = [("Alice", 1), ("Bob", 2)]
columns = ["name", "id"]

# Create DataFrame
df = spark.createDataFrame(data, columns)
