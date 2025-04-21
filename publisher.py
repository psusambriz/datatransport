import json
from google.cloud import pubsub_v1
import time

# TODO(developer)
project_id = "testinglab3"
topic_id = "my-topic"
json_file = "bcsample.json"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

# read and parse json file
with open("bcsample.json","r") as f:
    breadcrumbs = json.load(f)

# publish each record
for crumb in breadcrumbs:
    message = json.dumps(crumb).encode("utf-8")
    future = publisher.publish(topic_path,message)
    print(f"Published message ID: {future.result}")
    time.sleep(0.1)

print(f"Total messages sent: {len(breadcrumbs)}")

from datetime import datetime

# Helper: parse ISO 8601 timestamp to datetime object
def parse_time(entry):
    return datetime.fromisoformat(entry["timestamp"])
