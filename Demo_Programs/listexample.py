import json

jString = '{"name":"Felix","age":20,"city":"Toronto"}'

data = json.loads(jString)

print(data["city"])
#why doesn't this work??