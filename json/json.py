import json

person = {"name": "John", "age":30, "city": "London","hasChildren":False,"title": ["engineer","programmer"]}

personJSON = json.dumps(person)
print(personJSON)