import json

def load_config():
  with open("data/config.json") as f:
    return json.load(f)