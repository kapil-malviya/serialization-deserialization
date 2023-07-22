"""
JSON module defines the following important functions :

for serialization purpose (python -> json form) :

- dumps() : it serialized python dict object to JSON string
- dump() : converting python dict object to JSON and write that JSON to 
			specified JSON file

for deserialization purpose (json -> python form) :

- loads() : converting JSON string to python dict, it deserializes to a string
- load() : reading json from a file and converting to the python dict object

"""


import json 

employee = {'name' : 'kapil', 'age' : 28, 'salary' : 88888888, 'ismarried' : True, 'ishavinggfs' : None}

json_string = json.dumps(employee)

print(json_string)  
print(type(json_string))      # <class 'str'>
print(type(employee))         # <class 'dict'>

# data in json form : {"name": "kapil", "age": 28, "salary": 88888888, "ismarried": true, "ishavinggfs": null}