import json
jString = ‘[{"name":{"firstName":"Cleopatra", "lastName" : "Ptolemy"}, "address": {"city":"Alexandria", "province":"Egypt"}}, {"name":{"firstName":"Marc", "lastName":"Antony"}, "address":{"city":"Rome", "province":"Italia"}}]’
data = json.loads(jString)

print(data[1]["address"]["city"])