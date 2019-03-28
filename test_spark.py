"""

https://spark.apache.org/docs/2.2.0/api/python/pyspark.sql.html

"""
from pyspark.sql import *
from pyspark.sql.functions import col
from pyspark.sql.functions import rand
from pyspark.sql.functions import lit

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.format("csv").options(
    header='true', delimiter=',').load('stub/test_spark.csv')


def test_to_pandas():
    pandas_df = df.toPandas()
    assert len(pandas_df) == 4


# https://docs.databricks.com/spark/latest/faq/append-a-row-to-rdd-or-dataframe.html
def test_dataframe_append():
    X = spark.range(3).toDF('no')
    Y = spark.range(3).toDF('no')

    assert X.union(Y).count() == 6


# You cannot add an arbitrary column to a DataFrame in Spark.
# https://stackoverflow.com/questions/33681487/how-do-i-add-a-new-column-to-a-spark-dataframe-using-pyspark
# https://stackoverflow.com/questions/32788322/how-to-add-a-constant-column-in-a-spark-dataframe
def test_add_literal_column():
    X = spark.createDataFrame([[1, 2], [3, 4]], ['a', 'b'])
    X = X.withColumn('c', lit(0))
    assert X.schema.names == ['a', 'b', 'c']

    column_c_values = [row[0] for row in X.select('c').collect()]
    assert column_c_values == [0, 0]


def test_create_dataframe():
    X = spark.createDataFrame([[1, 2], [3, 4]], ['a', 'b'])
    assert X.count() == 2

    # https://stackoverflow.com/questions/38610559/convert-spark-dataframe-column-to-python-list
    column_a_values = [row[0] for row in X.select('a').collect()]
    assert column_a_values == [1, 3]


# https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=save#pyspark.sql.DataFrame
# & | - https://stackoverflow.com/questions/37707305/pyspark-multiple-conditions-in-when-clause
def test_filter():
    cats_df = df.filter(((col('cat') == 'true') | (col('height') > 170)))
    assert cats_df.count() == 3

    old_df = df.filter((col('age') > 30) & (col('height') > 170))
    assert old_df.count() == 1


# https://stackoverflow.com/questions/39344769/spark-dataframe-select-n-random-rows
def test_sample():
    sample_df = df.sample(False, 0.5)  # it doesn't guarantee exact 0.5.

    assert sample_df.count() >= 0
    assert sample_df.limit(1).count() < 2

    sample_df = df.orderBy(rand()).limit(2)
    assert sample_df.count() == 2


# https://stackoverflow.com/questions/38063657/pyspark-merge-outer-join-two-data-frames
def test_merge():
    sex_df = spark.read.format("csv").options(
        header='true', delimiter=',').load('stub/test_spark_join.csv')
    joined_df = df.join(sex_df, on=['name'], how='inner')

    assert joined_df.count() == 2
    assert joined_df.schema.names == [
        'name', 'age', 'height', 'cat', 'sex', 'age'
    ]

    # distinguish column names
    # https://stackoverflow.com/questions/33778664/spark-dataframe-distinguish-columns-with-duplicated-name
    # https://stackoverflow.com/questions/34077353/how-to-change-dataframe-column-names-in-pyspark
    joined_df = df.join(
        sex_df.selectExpr('name as name', 'age as age1'),
        on=['name'],
        how='inner')

    assert joined_df.schema.names == ['name', 'age', 'height', 'cat', 'age1']
