f=open("/Applications/Python 2.7/Install Certificates.Command")
print f.read()
f.close()
"""
i=0
for j in f:
    d=j.strip()
    i=i+1
    jk=j.split(",")
    
    print "name:",jk[0]
    print "attendence:",jk[1]

print "total records" + str(i)        
f.close()
"""
