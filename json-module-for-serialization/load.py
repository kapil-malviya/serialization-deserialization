"""

for deserialization purpose (json -> python form) :

- loads() : converting JSON string to python dict, it deserializes to a string
- load() : reading json from a file and converting to the python dict object

"""

import json

with open('emp.json', 'r') as f :
    emp_dict = json.load(f)

print(type(emp_dict))

# print('employee name : ', emp_dict['name'])
# print('employee age : ', emp_dict['age'])
# print('employee salary : ', emp_dict['salary'])
# print('is employee married : ', emp_dict['ismarried'])
# print('is employee having gfs : ', emp_dict['ishavinggfs'])


for x,y in emp_dict.items() :
    print('{} : {}'.format(x,y))




"""
<class 'dict'>

name : kapil
age : 28
salary : 88888888
ismarried : True
ishavinggfs : None

"""