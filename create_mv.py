import psycopg2

conn = psycopg2.connect(host="localhost", port=4566, user="root", dbname="dev")

conn.autocommit = True # Set queries to be automatically committed.

with conn.cursor() as cur:
    cur.execute("""
    CREATE MATERIALIZED VIEW anomaly_detection_by_error_status AS
    SELECT 
        ip_address, 
        COUNT(*) AS error_count
    FROM 
        log_data
    WHERE 
        status_code::integer >= 400
    GROUP BY 
        ip_address
    HAVING 
        COUNT(*) > 3; -- Threshold for error occurrences


 """) # Execute the query.

conn.close() # Close the connection.
