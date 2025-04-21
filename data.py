# import requests
import requests
import json
from values import ids_array

# vehicle_ids = [2905,2908]
all_data = []

for vid in ids_array:
    response = requests.get(f"https://busdata.cs.pdx.edu/api/getBreadCrumbs?vehicle_id={vid}")
    if response.status_code == 200:
        all_data.extend(response.json())
    else:
        print(f"Failed to get data for vehicle ID {vid}. Error: {response.status_code}")

with open("bcsample.json","w") as f:
    json.dump(all_data,f,indent=2)