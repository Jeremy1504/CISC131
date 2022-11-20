import json

person_dict = {"name": "David",
    "languages": ["Python", "Java"],
    "age": 22
}

with open('Unit 09/person.json', 'w') as json_file:
    json.dump(person_dict, json_file)
