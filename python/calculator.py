
def calculator(o,a,b):
	if(o=="+"):
		c=a+b
		return c
	elif(o=="-"):
		c=a-b
		return c
	elif(o=="*"):
		c=a*b
		return c
	elif(o=="/"):
		c=a/b
		return c
	elif(o=="%"):
		c=a%b
		return c
	else:
		print("Not valid")
p=raw_input("enter operator :")
q=int(raw_input("enter 1st value:"))
r=int(raw_input("enter 2nd value:"))
ans=calculator(p,q,r)
print ans
"""
def sum(o,a,b,*val):
        add = 0
        for i in val:
                add = add + i
        return add
                
print sum(1,2,34,54,6,67,8,89,)
"""
