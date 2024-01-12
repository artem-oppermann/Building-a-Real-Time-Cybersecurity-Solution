import psycopg2

conn = psycopg2.connect(host="localhost", port=4566, user="root", dbname="dev")

conn.autocommit = True 

with conn.cursor() as cur:
    cur.execute("""
        CREATE SINK send_data_to_kafka FROM anomaly_detection_by_error_status
        WITH (
        connector='kafka',
        properties.bootstrap.server='localhost:9093',
        topic='anomalies'
        ) FORMAT PLAIN ENCODE JSON (
        force_append_only='true',
        );""") # Execute the query
            
conn.close() 
