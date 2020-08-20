import logging
from pyspark.sql import SparkSession

logging.basicConfig(format='[%(asctime)s] - %(name)s - %(levelname)s : %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

spark = SparkSession.builder.appName("example-app").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

log.info(f"Spark version = {spark.version}")
log.info(f"Hadoop version = {spark.sparkContext._jvm.org.apache.hadoop.util.VersionInfo.getVersion()}")

