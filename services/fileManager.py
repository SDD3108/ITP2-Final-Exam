import json
from pathlib import Path
from utils.decorators import safe_file

@safe_file
def read_json(path):
    with open(path,"r",encoding="utf-8") as file:
        return json.load(file)

def write_json(path,data):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)

    with open(path,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=2)