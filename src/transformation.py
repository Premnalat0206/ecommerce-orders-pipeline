from pyspark.sql.functions import * 

def standardize_category(df):
    transform_df = df.withColumn("category",initcap(col("category")))
    return transform_df

def remove_duplicates(df):
    duplicates_df = df.dropDuplicates(["order_id"])
    return duplicates_df

def convert_order_timestamp(df):
    transformed_df = df.withColumn("order_time",to_timestamp(col("order_time")))
    return transformed_df