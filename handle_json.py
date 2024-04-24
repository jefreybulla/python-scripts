import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])


# read json from a file
with open('person.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)

# more examples: https://www.programiz.com/python-programming/json