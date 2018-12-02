from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


def test_spark():
    df = spark.read.format("csv").options(header='true', delimiter='~').load('stub/test_panda.csv').toPandas()
    assert len(df) == 2

