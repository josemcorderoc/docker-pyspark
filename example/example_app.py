import logging
from pyspark.sql import SparkSession
from pyspark.sql.pandas.functions import pandas_udf
from pyspark.sql.types import StringType
from pyspark.sql.functions import col
import pandas as pd

logging.basicConfig(format='[%(asctime)s] - %(name)s - %(levelname)s : %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

spark = SparkSession.builder.appName("example-app").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

log.info(f"Spark version = {spark.version}")
log.info(f"Hadoop version = {spark.sparkContext._jvm.org.apache.hadoop.util.VersionInfo.getVersion()}")

log.info('Spark processing example')


@pandas_udf(StringType())
def custom_processing(s: pd.Series) -> pd.Series:
    return s.apply(lambda x: f"This value is {x}")


df = spark.read.format('csv').options(header=True).load('example_data.csv')  # It could be an S3a path
df.show()
df = df.select('*', custom_processing(col('column1')).alias('new_column'))
df.show()
