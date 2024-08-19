# -*- coding: utf-8 -*-pyder Editor


sample_str ='PRIYANSHU YADAV'
print(sample_str)
# code
# sequence data types ----- string ,tuple,array, list
lstNumber =[1,2,3,3,4,5]   #list with single data type
print(lstNumber)
lstSample =[1,2,'a','sam',2]  #mixed data type  list
print(lstSample)
print(len(lstSample))

from  array import *   #importnig array module
sampleArr =array('i',[1,2,3,4,5])  # array
for x in  sampleArr:print(x)  # printing value of array one by one
print(sampleArr) #printing array's value

tupleSample = (1,'me',2,3)  #tuple
print(tupleSample)
tupleSample =1,2,'py'      # tuple  packing
print(tupleSample)

# dictionary :
#dict ={12:'twelve','second':2,3:3}
#print(dict[12])
 # creating   a dictionary by using dict  keyword
dictSample = dict([(1,'one'),(2,3),('second',2)])
print(dictSample)



setSample ={1,"priyanshu yadav",2.4,True}

print(setSample)

#range (start,stop,step)  function
rangeSample =range(1,12,4)
for i in rangeSample:
    print(i)