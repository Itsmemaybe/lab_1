import json
# TODO решите задачу
def task() -> float:
    result = 0.0
    file_path = "input.json"
    with open(file_path) as f:
        data = json.load(f)
        for i in data:
            temp_sum = list(i.values())[0] * list(i.values())[1]
            result += temp_sum
    return round(result, 3)



print(task())
