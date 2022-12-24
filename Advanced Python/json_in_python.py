import json
# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x) # -- loads method converts json to python

# the result is a Python dictionary:
print(y["name"])

# a Python object (dict):
sa = {
  "name": "John",
  "age": 30,
  "city": "New York"
}      

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# convert into JSON:   dumps method converts python code to jsons
z = json.dumps(sa)


# sort_keys is used to sort the itmes accodring to alphabetically
json.dumps(x, indent=1 ,sort_keys= True)
# the result is a JSON string:
print(y)