import json
from google.cloud import pubsub_v1

# TODO(developer)
project_id = "testinglab3"
topic_id = "my-topic"
json_file = "combined_data.json"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

# read and parse json file
with open(json_file,"r") as f:
    data_list = json.load(f)

# publish each record
for i, record in enumerate(data_list,start=1):
    data_str = json.dumps(record)
    data = data_str.encode("utf-8")
    future = publisher.publish(topic_path,data)
    print(f"Published message {1}: {future.result()}")

print(f"Published {len(data_list)} messages to {topic_path}.")