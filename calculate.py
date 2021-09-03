x=0
y=0
z=0
soma=x+y+z
check=0
answer=23
array=[0]

while check==0:
	for x in range(10):
		if x not in array:
			for y in range(10):
				if y not in array:
					for z in range(10):
						if z not in array and x!=y and x!=z and y!=z:
							soma=x+y+z
							if soma==22:
								print(x,"+",y,"+",z,"=",answer)
								check=1
		
