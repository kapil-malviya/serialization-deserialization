"""
importing empy.py file

"""


import empy, pickle

f = open('empy.dat', 'wb')
n = int(input('Enter no. of employees : '))
for i in range(n) :
	eno = int(input('Enter the Employee number : '))
	ename = input('Enter the name of Employee : ')
	esal = float(input('Enter the salary of Employee : '))
	eaddr = input('Enter the address Employee : ')
	e = empy.Employee(eno, ename, esal, eaddr)
	pickle.dump(e,f)

print('Employees object pickled successfully...')