import stix2viz
import json

with open("test.json", "r") as f:
	data = json.load(f)
print(data)
#stix2viz.display(data)

