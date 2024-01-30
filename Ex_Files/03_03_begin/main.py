import csv
import json #far more popular than csv in modern python development
from pprint import pprint #pretty print, making outputs improved

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) #creaing a string for the json
back_to_dict = json.loads(einstein_json) #converting the string back to json
print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as f: #'f' here is the file object
    reader = csv.DictReader(f)
    laureates = list(reader)


with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
