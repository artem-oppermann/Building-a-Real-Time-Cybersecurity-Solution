import psycopg2

conn = psycopg2.connect(host="localhost", port=4566, user="root", dbname="dev")


conn.autocommit = True # Set queries to be automatically committed.

with conn.cursor() as cur:
    cur.execute("""
CREATE SOURCE IF NOT EXISTS log_data2 (
 timestamp varchar,
 ip_address varchar,
 user varchar,
 action varchar,
 resource varchar,
 status_code varchar
 )
WITH (
 connector='kafka',
 topic='log_data',
 properties.bootstrap.server='localhost:9093',
 scan.startup.mode='earliest'
 ) FORMAT PLAIN ENCODE JSON;""") # Execute the query.

conn.close() # Close the connection.
