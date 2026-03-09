print("Sample Databricks ETL script")
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("AzureDataEngineeringPipeline").getOrCreate()

# Read raw data
df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)

# Basic transformation
clean_df = df.filter(col("amount") > 0)

# Show result
clean_df.show()

# Write processed data
clean_df.write.mode("overwrite").parquet("data/processed_sales")
