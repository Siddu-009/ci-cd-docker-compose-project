import json
import os

config_file = "config.json"

if os.path.exists(config_file):
    with open(config_file) as f:
        json.load(f)
    print("Configuration file is valid.")
else:
    print("No configuration file found. Skipping validation.")