'''
for serialization purpose (python -> json form) :

- dumps() : it serialized python dict object to JSON string
- dump() : converting python dict object to JSON and write that JSON to 
			specified JSON file

'''

import json 

employee = {'name' : 'kapil', 'age' : 28, 'salary' : 88888888, 'ismarried' : True, 'ishavinggfs' : None}

with open('emp.json','w') as f :
	# json.dump(employee, f)
	json.dump(employee, f, indent=4)



'''
json.dump(employee, f)  =>

{"name": "kapil", "age": 28, "salary": 88888888, "ismarried": true, "ishavinggfs": null}


 when, indent = 4
{
    "name": "kapil",
    "age": 28,
    "salary": 88888888,
    "ismarried": true,
    "ishavinggfs": null
}
'''