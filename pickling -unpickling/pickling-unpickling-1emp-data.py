### Pickling and Unpickling of Objects :

"""
=>> Sometimes we have to write total state of object to the file and we have to read total
	object from the file.
=>> The process of writing state of object to the file is called pickling and the process of
	reading state of an object from the file is called unpickling.

=>> We can implement pickling and unpickling by using pickle module of Python.


->  pickle module contains dump() function to perform pickling.
	through pickling we are saving data to the file for future purpose permanently.

	pickle.dump(object,file)


->  pickle module contains load() function to perform unpickling

	obj=pickle.load(file)

"""

#	pickling & unpickling data of single employee :


import pickle

class Employee :
	def __init__(self, eno, ename, esal, eaddr) :
		self.eno = eno
		self.ename = ename
		self.esal = esal
		self.eaddr = eaddr
	def display(self) :
		print(self.eno, '\t', self.ename, '\t', self.esal, '\t', self.eaddr, '\t',)

with open('emp.dat', 'wb') as f : 
	e = Employee(100, 'Anar', 10000, 'Hyd')
	pickle.dump(e, f)
	print('pickling of Employee object completed...')


with open('emp.dat', 'rb') as f :
	obj = pickle.load(f)
	print('Employee Information after unpickling...')
	obj.display()