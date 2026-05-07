from pyspark.sql import SparkSession
from utils import get_logger,check_file_exists

logger = get_logger(__name__)

spark = SparkSession.builder\
                     .appName("EcommerceOrdersPipeline")\
                     .getOrCreate()

def read_orders_data(path):
    try:
        if check_file_exists(path,logger):
            df = spark.read.csv(
                path,
                header= True,
                inferSchema= True
            )
            logger.info(f"Successfully loaded file: {path}")
            return df
        else:
            logger.error(f"File  not found {path}")

    except Exception as e:
          logger.error(f"Error while reading file : {e}")

df = read_orders_data("data/raw/orders.csv")

df.show()
