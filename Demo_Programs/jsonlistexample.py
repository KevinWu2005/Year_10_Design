import json	

jString = ‘{"name":{"firstName":"Cleopatra", "lastName":"Ptolemy"}, "address":{"city":"Alexandria", "province":"Egypt"}}’


data = json.loads(jString)


print(data["address"]["city"])