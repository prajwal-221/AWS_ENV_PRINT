# update_version.py

import os
import json

with open("package.json", "r") as f:
    data = json.load(f)

major = os.environ.get("MAJOR", "0")
minor = os.environ.get("MINOR", "0")
patch = os.environ.get("PATCH", "0")

data["version"] = f"{major}.{minor}.{patch}"

with open("package.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"✅ package.json version set to {data['version']}")
