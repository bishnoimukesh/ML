from __future__ import print_function

print ("tpyramid of * ")
for i in range(1,10):
    for j in range(10 - i):
        print (""*i, end =  " ")
    for j in range(1, i):
        print ("*"*i, end = " ")
    for j in range(i, 0, -1):
        print (""*i, end = " ")
        



   
