# import requests
import requests
import json

# get url
car1 = "https://busdata.cs.pdx.edu/api/getBreadCrumbs?vehicle_id=2905"
car2 = "https://busdata.cs.pdx.edu/api/getBreadCrumbs?vehicle_id=2907"
# get request
response = requests.get(car1)
response2 = requests.get(car2)

data1 = response.json()
data2 = response2.json()

# 
combined_data = {
    "car1": data1,
    "car2": data2
}
# write the .json files
with open("combined_data.json","w") as f:
    json.dump(combined_data,f,indent=2)