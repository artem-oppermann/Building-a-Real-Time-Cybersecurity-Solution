import json
import random
from datetime import datetime

def generate_synthetic_log_entry():
    # Define a set of fake IP addresses to simulate network traffic
    ip_addresses = ["192.168.1.{}".format(i) for i in range(1, 101)]

    # Define a set of usernames
    users = ["user{}".format(i) for i in range(1, 21)]

    # Define a set of actions
    actions = ["login", "logout", "access", "modify", "delete"]

    # Define a set of resources
    resources = ["/api/data", "/api/user", "/api/admin", "/api/settings", "/api/info"]

    # Define a set of status codes
    status_codes = [200, 301, 400, 401, 404, 500]

    # Generate a random log entry
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip_address": random.choice(ip_addresses),
        "user": random.choice(users),
        "action": random.choice(actions),
        "resource": random.choice(resources),
        "status_code": random.choice(status_codes)
    }
    return log_entry

# File to save the synthetic log entries in JSON format
json_file_path = 'synthetic_log_data.json'

# Generate and save synthetic log entries
with open(json_file_path, 'w') as file:
    for _ in range(100):
        log_entry = generate_synthetic_log_entry()
        file.write(json.dumps(log_entry) + '\n')  # Write each JSON object in one line


json_file_path
