
import json


FILENAME = "input.json"
def task() -> float:
    with open(FILENAME, encoding='utf-8') as f:
        json_data = json.load(f)

        list_values = sum([item["score"] * item["weight"] for item in json_data])
    return round(list_values, 3)

print(task())