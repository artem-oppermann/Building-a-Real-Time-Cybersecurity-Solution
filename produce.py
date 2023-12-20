import json
from confluent_kafka import Producer

# Configuration for connecting to Kafka
config = {
    'bootstrap.servers': 'localhost:9093',  # Replace with your Kafka server address
}

# Create a producer instance
producer = Producer(config)

# Topic to produce to
topic_name = 'log_data'


# Callback function to check if message delivery was successful
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Function to produce messages
def produce_message(data):
    # Trigger any available delivery report callbacks from previous produce() calls
    producer.poll(0)

    # Asynchronously produce a message, the delivery report callback will be triggered once the message has been successfully produced or failed
    producer.produce(topic=topic_name, value=json.dumps(data), callback=delivery_report)

# Produce messages from the data file
def produce_data_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            record = json.loads(line.strip())
            produce_message(record)

    # Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered
    producer.flush()

# Path to your data file
file_path = 'synthetic_log_data.json'  # Replace with your actual file path

# Start producing data to Kakfa topic
produce_data_from_file(file_path)
