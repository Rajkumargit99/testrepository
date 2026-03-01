import json

def read_json_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        print(type(data))
        json_data = json.loads(data)
        print(type(json_data))
        return json_data

output = read_json_data("user_data.json")

print(output["user name"])
print(output["city"])

output["country"] = "india"
output["location"] = "hyderabad"

print(output)

def write_json_data(file_path, json_d):
    with open(file_path, "w") as file:
        json_value = json.dumps(json_d)
        file.write(json_value)


write_json_data("user_data.json", output)