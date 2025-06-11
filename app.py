import json

with open("package.json") as f:
    data = json.load(f)
    print(f"Running Python app version {data['version']}")
