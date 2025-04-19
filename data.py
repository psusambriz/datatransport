# import requests
import requests
import json

vehicle_ids = [2905,2908]
all_data = []

for vid in vehicle_ids:
    response = requests.get(f"https://busdata.cs.pdx.edu/api/getBreadCrumbs?vehicle_id={vid}")
    if response.status_code == 200:
        all_data.extend(response.json())
    else:
        print(f"Failed to get data for vehicle ID {vid}")

with open("bcsample.json","w") as f:
    json.dump(all_data,f,indent=2)