from ingestion import read_orders_data
from transformation import standardize_category,remove_duplicates,convert_order_timestamp
from validation import check_invalid_timestamp,check_negative_amount,check_null_customer
from utils import get_logger,check_file_exists

logger = get_logger(__name__)

try:

    # Read raw data
    orders_df = read_orders_data("data/raw/orders.csv")

    logger.info("Raw data loaded successfully")


    # -----------------------------
    # Transformations
    # -----------------------------

    orders_df = standardize_category(orders_df)

    logger.info("Category standardization completed")


    orders_df = remove_duplicates(orders_df)

    logger.info("Duplicate removal completed")


    orders_df = convert_order_timestamp(orders_df)

    logger.info("Timestamp conversion completed")


    # -----------------------------
    # Validations
    # -----------------------------

    null_customer_df = check_null_customer(orders_df)

    negative_amount_df = check_negative_amount(orders_df)

    invalid_timestamp_df = check_invalid_timestamp(orders_df)


    # -----------------------------
    # Combine bad records
    # -----------------------------

    bad_records_df = (
        null_customer_df
        .union(negative_amount_df)
        .union(invalid_timestamp_df)
        .dropDuplicates()
    )


    logger.info("Bad records separated successfully")


    # -----------------------------
    # Create clean records
    # -----------------------------

    clean_orders_df = orders_df.subtract(bad_records_df)


    logger.info("Clean records created successfully")


    # -----------------------------
    # Preview outputs
    # -----------------------------

    print("CLEAN RECORDS")
    clean_orders_df.show()


    print("BAD RECORDS")
    bad_records_df.show()


except Exception as e:

    logger.error(f"Pipeline failed : {e}")