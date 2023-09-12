import jsonpickle

class Employee:
	def __init__(self, eno, ename, eage, isMarried):
		self.eno = eno
		self.ename = ename
		self.eage = eage
		self.isMarried = isMarried

	def display(self):
		print("E. No. : {}, E. Name : {}, E. Age : {}, E. is Married : {} \n".format(self.eno, self.ename, self.eage, self.isMarried))

e = Employee(108, 'Kapil', 28, True)


# Serialization to json string :

json_string = jsonpickle.encode(e)
print(json_string,'\n')

''' output : 
{"py/object": "__main__.Employee", "eno": 108, "ename": "Kapil", "eage": 28, "isMarried": true}

'''

# Serialization to json file : 

with open('employee.json', 'w') as file:
	file.write(json_string)



# Deserialization from json string : 

e2 = jsonpickle.decode(json_string)     # we already have json string (json_string)
print(type(e2))
e2.display()

''' output :
<class '__main__.Employee'>
E. No. : 108, E. Name : Kapil, E. Age : 28, E. is Married : True

'''

# Deserialization from json file :

with open('employee.json', 'r') as file:
	json_file_string = file.readline()
e3 = jsonpickle.decode(json_file_string)
e3.display()