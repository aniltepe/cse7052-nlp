import os
import json

FOLDER_NAME = "TrainingSet"

json_data = []
for path, dirs, files in os.walk(f"./{FOLDER_NAME}"):
    for file in files:
        if file.endswith(".json"):
            f = open(os.path.join(path, file), encoding="utf-8-sig")
            json_data.append(json.load(f))
            f.close()
        # print(os.path.join(path, file))
        
print(len(json_data))