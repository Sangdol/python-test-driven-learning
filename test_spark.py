"""

https://spark.apache.org/docs/2.2.0/api/python/pyspark.sql.html#pyspark.sql.DataFrame.write

"""
from pyspark.sql import *
from pyspark.sql.functions import col
from pyspark.sql.functions import rand

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.format("csv").options(header='true', delimiter=',').load('stub/test_spark.csv')


def test_spark():
    pandas_df = df.toPandas()
    assert len(pandas_df) == 4


# https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=save#pyspark.sql.DataFrame
# & | - https://stackoverflow.com/questions/37707305/pyspark-multiple-conditions-in-when-clause
def test_filter():
    cats_df = df.filter(((col('cat') == 'true') | (col('height') > 170)))
    assert len(cats_df.collect()) == 3

    old_df = df.filter((col('age') > 30) & (col('height') > 170))
    assert len(old_df.collect()) == 1


# https://stackoverflow.com/questions/39344769/spark-dataframe-select-n-random-rows
def test_sample():
    sample_df = df.sample(False, 0.5)

    assert len(sample_df.collect()) == 2
    assert len(sample_df.limit(1).collect()) == 1

    sample_df = df.orderBy(rand()).limit(2)
    assert len(sample_df.collect()) == 2


# https://stackoverflow.com/questions/38063657/pyspark-merge-outer-join-two-data-frames
def test_merge():
    sex_df = spark.read.format("csv").options(header='true', delimiter=',').load('stub/test_spark_join.csv')
    joined_df = df.join(sex_df, on=['name'], how='inner')

    assert len(joined_df.collect()) == 2
    assert joined_df.schema.names == ['name', 'age', 'height', 'cat', 'sex', 'age']

    # distinguish column names
    # https://stackoverflow.com/questions/33778664/spark-dataframe-distinguish-columns-with-duplicated-name
    # https://stackoverflow.com/questions/34077353/how-to-change-dataframe-column-names-in-pyspark
    joined_df = df.join(sex_df.selectExpr('name as name', 'age as age1'), on=['name'], how='inner')

    assert joined_df.schema.names == ['name', 'age', 'height', 'cat', 'age1']
