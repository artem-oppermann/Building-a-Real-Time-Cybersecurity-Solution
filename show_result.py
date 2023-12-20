import psycopg2

conn = psycopg2.connect(host="localhost", port=4566, user="root", dbname="dev")


conn.autocommit = True 

with conn.cursor() as cur:
    cur.execute("""
 SELECT * FROM anomaly_detection_by_error_status; """) # Execute the query.
    
    # Fetch all rows from the executed query.
    rows = cur.fetchall()
    
    # Iterate through the rows and print each one.
    for row in rows:
        print(row)

conn.close() 
