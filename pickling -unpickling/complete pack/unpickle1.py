"""
load() : unpickling of data from the stored file 
		  empy.dat 

"""



import empy, pickle

f = open('empy.dat', 'rb')
print('Employee detailes... \n')
while True:
	try:
		obj=pickle.load(f)
#		obj.display()
		if obj.eno==100:
			obj.display()
	except EOFError:
		print("\nAll employees Completed")
		break
f.close()