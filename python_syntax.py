name ="priyanshu yadav"
if name[0].islower:
    name =name.capitalize()
print(name)
#concept of index[] =gives access to a sequence 's element(str,tuples,list)
#example -2
name ='Shivani Pal'
first_name =name[0:7].upper()# all character of string will be in upper case
last_name =name[8:].lower()# all character of string will be in upper case
print(first_name)
print(last_name)
print(name[-1])

#function =a block of code which is executed only when it is called


# example -1-----
def hello(name,age):
    print("hello!"+name)
    print("HAPPY BIRTHDAY")
    print("you are {age} years old")



#
my_name =input("enter your name: ")
age =int(input("enter age"))

hello(my_name,age) #calling function

#example 2---
#check wether the number is even or odd
def divides(m,n):
    if n%m ==0:
        return True
    else:
        return False

def check_even(n):
    return divides(2,n)

def check_odd(n):
    return not divides(2,n)



m =int(input("enter m"))
n =int(input("enter n"))
print(divides(m,n))
print(check_even(n))
print(check_odd(n))

# return statement== Functions send Python values /objects back to the caller.
#                      these valures/objects are known as function return values

def multiply(num1,num2):
    return  num1*num2

result =multiply(4,9)
print(result) #36



#keyword arguments ----- arguments preceded by an identifier when we pass them to ac function
#                           the order of arguments doesn't matter ,unlike positional arguments
#                               python knows the names of the arguments that our function recieves
 #example--1---
def hello(first,middle ,last):
    print("welcome home "+first+" "+middle+" "+last)

hello(last="SHIVANI", middle="PAL ", first ="YADAV")



# nested function call = function calls inside other functions calls
#                           innermost functions calls are resolved first
#                             returned value is used as  argumnent for the next outer function
#
# example --1

num =input("enter  a whole positive number")
num =float(num)
num =abs(num)
num =round(num)
print(num)

 #we can do this by using nested function calls method
print(round(abs(float(input("enter a whole positive number: "))))) #input = 34.89 #output =35

#scope of  variables
# scope =the region that a variable is recognised
#           a variable is only available from inside the region it is created
#             a global and  local scope version of a variable is created

name ="PRIYANSHU YADAV" # global scope(available inside and outside of a function)
def display_name():
    name ="Code" #local scope (available only inside the function
    print (name)
 # note ==  python follow  L=LOCAL then E = ENCLOSING , G =GLOBAL ,B =BUILT IN)
display_name()
print(name)



# *args  = parameter that will pack all arguments into a tuple
#             useful so that function can accept varrying amout of arguments
#example--1
def add(*args):
    sum =0
    for i in args :
        sum+=i
    return sum

print(add(1,2,3,4,4,5,6,6)) #31

#example-2
def add1(*stuff):#creating args =tuple
    stuff =list(stuff) #changing tuple into list
    sum =0
    stuff[0]=0  #changing 0th index element  1 to 0
    for i in  stuff:
        sum +=i
    return sum
print(add1(1,2,3,4,4,5,6,6)) #30 as th index element which is 1 changed to zero



# **kwargs = parameter that will pack all arguments into a dictionary
#                   useful so that a function can accept a varyying amount of keyword argument


# example -1

def helo(**kwargs): #**kwargs =can be named as ** variable_name
    # print("hello"+" "+kwargs['first']+" "+kwargs['last'])
    print("hello",end =" ")
    for key,value in kwargs.items():
      print(value,end =" ")

helo(title ="Mr.",first ="Bro",middle ="code",last ="do\n")



# str.format() =optional method that gives users
#                  more control when displaying output

animal ="cow"
item ="moon"
print("the",animal ,"jumped over the",item)
print("the {1} jumped over the{0}".format(animal ,item)) #positional arguments
