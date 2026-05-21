import json
from utils.decorators import safe_file

@safe_file
def read_json(path):
    with open(path,"r",encoding="utf-8") as file:
        return json.load(file)