d = {'key1': 'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


print(d['key1'])

print(d.keys())

print(d.values())

# remove element
print('removing element from dictionary')
d.pop('key2')
print(d)
# another way to remove an element
del d['key3']
print(d)