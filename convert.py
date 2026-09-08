import yaml
import json

with open("gateway-config.yaml") as f:
    data = yaml.safe_load(f)

with open("config.json", "w") as f:
    json.dump(data, f, indent=2)

print("config.json created")
