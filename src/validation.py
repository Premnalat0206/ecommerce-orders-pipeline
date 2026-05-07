from pyspark.sql.functions import *

def check_null_customer(df):
      null_customer = df.filter(col("customer_id").isNull())
      return null_customer	

def check_negative_amount(df):	
     negative_amount = df.filter(col("amount")<= 0)
     return negative_amount


def check_invalid_timestamp(df):
      invalid_timestamp = df.filter(col("order_time").isNull())
      return invalid_timestamp