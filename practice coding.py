print("--------------------list methods---------")
l=[1,5,4,2,10,9,12,11,20,15]
l.sort()
print(l)
l.reverse()
print(l)
l.sort()
print(l)
l.append(30)
print(l)
l.pop(5)
print(l)
l.insert(5,50)
print(l)
l.remove(11)
print(l)

print("---------------dictionary methods---------")
d={1:"john",2:"ram",3:"rohan"}
print(d.keys())
print(d.values())

dictionary = {"apples":3, "bananas":4, "pears":5, "lemons":10, "tomatoes": 7}

a = ["apples","lemons"]
b = {key: dictionary[key] for key in a }
print(b)


print("python add two number")

a= int(input("Enter number a:"))
b= int(input("Enter number b:"))
c=a+b
print("addition",c)

print("---------maximum number find-------")

a=100
b=200
print(max(a,b))

print("-----------Factorial number-------------")

n=int(input("Enter factorial number:"))
if (n == 0 or n == 1):
    print(1)
else:
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    print(fac)
print("----------------------dictionary---------------")

test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
print("The original dictionary is : " + str(test_dict))
res = list(sorted({ element for val in test_dict.values() for element in val}))
print("The unique values list is : " + str(res))


print("---------------Simple Intrest-----------")
p = int(input('enter principle amount:'))
r = int(input("enter rate of intrest;"))
y = int(input('enter year: '))
SI= p*r*y/100
print("simple intrest",SI)

'''
For a Product Latop(HP,Dell,Lenovo, Apple) below are the fields
1. product id 2.Product Name 3. Brand 4.Price 5.Color 6.RAM


Create Product class and 3 objects for all 3 products(HP,Dell Lenovo)
Compare all products and get highest cost, lowest cost, highest ram, lowest ram laptop details
'''
print("---------------------- laptop details--------------------------")

class Product:
    # electronic='laptop'
    def model(self, pi, pn, b, p, c, r):
        self.productId = pi
        self.productName = pn
        self.brand = b
        self.price = p
        self.color = c
        self.ram = r

    def display(self):
        print(self.productId)
        print(self.productName)
        print(self.brand)
        print(self.price)
        print(self.color)
        print(self.ram)


ob = Product()
ob1 = Product()
ob2 = Product()
ob.model(123245, 'hp Pavilion', 'hp', 55000, 'white', 4)
ob.display()
ob1.model(98567, 'thinkerpad', 'lenovo', 45000, 'white', 4)
ob1.display()
ob2.model(23412, 'inspiron', 'dell', 48000, 'gray', 8)
ob2.display()



print("------------- factorial number------------")
# Find factorial of any number
# example (5)


def factorial(n):
    if (n == 0 or n == 1):
        print(1)
    else:
        fac = 1
        for i in range(1, n + 1):
            fac = fac * i
        print(fac)


factorial(5)

# Find largest and smallest number in list.
print("-------largest and smallest number in list.------------")
a = [10, 23, 32, 45, 25, 68, 89, 110]
print("largest number in list", max(a))
print("lowest number in list", min(a))



# find range in (*) to making tringle of star.
print("---------------range in (*) to making tringle of star.------------------")

n = int(input("Enter number :"))
for i in range(n):
    for j in range(i, n):
        print(' ', end='')
    for j in range(i + 1):
        print(' ', end=' ')
    print()

# find odd and even number
print("--------- odd even number--------------")

odd = []
even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
        if len(even) == 20:
            break
    else:
        odd.append(i)
        if len(odd) == 20:
            break
print(odd, even)


employees = ["john", "rohan"]
defaults = {"Employee_Id": 1, "salary": 8000, "Experiance": 0}
result = dict.fromkeys(employees, defaults)
print(result)

Employee = {"EmplId:1234": ["Ram", 8000, 1], "EmplId:2345": ["john", 10000, 2]}
eid = input("Please enter your employee ID")

if eid == "EmplId:1234":
    salary1 = list(Employee.values())[0][1]
    exp1 = list(Employee.values())[0][2]
    print(salary1)
if eid == "EmplId:2345":
    salary2 = list(Employee.values())[1][1]
    exp2 = list(Employee.values())[1][2]
    print(salary2)

print("-----------add all dic values----------")

dict1 = {'a':100,'b':200,'c':300,'d':500,'e':600,'f':700,'g':800,'h':900,'i':1000}
list = []
for i in dict1:
    list.append(dict1[i])
    result = sum(list)
print("addtion",result)

print("------------delete dic---------")

dis = {"john":21,"rocky":32,"rinky":20,"riya":20,"johny":25}
print("before deleting dictionary: ",dis)
del dis["rinky"]
print("after deleting dictionary: ",dis)
del dis["riya"]
del dis["johny"]
print("after again deleting dictionary:",dis)

print("-----sort list of dictionaries by values in Python using lambda----")

lst = [{"name":"nandini","age":21},
       {"name":"ruhi","age":19},
       {"name":"jahnvi","age":19},
       {"name":"priyanka","age":23}]
print(sorted(lst , key = lambda i : i['age']))
print(sorted(lst , key = lambda i : (i['age'],i['name'])))
print(sorted(lst , key = lambda i : (i['age']), reverse=True))

print("---------------Merge two dictionary-------")

d = {"name":"rohan","age":21,"gender":"male"}
d1 = {"citizenship":"indian","state":"maharashtra","city":"nagpur"}
for i in d1.keys():
        d[i]=d1[i]
print(d)

print("-------------dictionary----------------")



'''
print("------------print windows page------------")
from tkinter import*
shinu=Tk()
shinu.title("hello friends good morning")
shinu=Label(shinu,text="Todays is my first day in my office",font=("Arial Bold",50))
shinu.grid(column=0,row=0)
mainloop()

from tkinter import*
from tkinter.ttk import*

from time import strftime

root=Tk()
root.title("clock")

def time():
    string = strftime('%D/%M/%Y , %H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label = Label(root,font=("ds-digital",20),background="white",foreground="green")
label.pack(anchor='center')

#def date():
    #string = date('%DD/%MM/%YY')
    #label.config(text=string)
    #label.after(2021,date)
#label = Label(root,font=("ds-digital",50),background="black",foreground="cyan")
#label.pack(anchor='center')
time()
#date()
mainloop()


from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcom to check button is properly working")
window.geometry('500x300')
rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=0, row=1)
rad3.grid(column=0, row=2)
window.mainloop()

'''
print("------------array---------")

import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)

print("--------------------ATM code program------------------")

print("Welcome to State Bank of India")
m=100000
p=int(input("Please Enter your ATM Pin: "))
if p in range (0,9):
    print("Please enter your pin:",p)
if p != 1234:
    print("invalid pin")
    print("1-Withdraw")
    print("2-Balance Enquiry")
    print("3- Fast cash")

c=int(input("please choose trasction"))

if (c==1):
    w=int(input("Enter withdraw amount:"))
    if (w<m and w% 100==0):
        print("please take your cash:",w)
    else:
        print("invalid cash")

elif(c==2):
    print("your available amount:",m)
elif(c==3):
    print("1->5000")
    print("2->10000")
    print("3->15000")
    print("4->20000")
    f=int(input("enter fast cash"))
    if(f==1 and 5000<m):
        print("please take cash 5000")
    elif(f==2 and 10000<m):
        print("please take cash 10000")
    elif(f==3 and 15000<m):
        print("please take cash 15000")
    elif(f==4 and 20000<m):
        print("please take cash 20000")
    else:
        print("invalide fast cash option")
else:
    print("wrong choice")

print("--------------marksheet program using if,elif condition-----------")

p=int(input("enter pysics marks="))
c=int(input("enter chemistry marks="))
b=int(input("enter biology marks="))
m=int(input("enter maths marks="))
e=int(input("enter english marks="))

t=p+c+b+m+e
print("total=",t)

a=t/5
print("avarage=",a)

p=t/500*100
print("percentage",p)

if p >90 and p<=100:
    print("Merit list")

elif p>75 and p<=89:
    print("First class")

elif p>60 and p<=75:
    print("Second class")

elif p>45 and p<=59:
    print("Third class")

elif p>35 and p<=44:
    print("Pass")

else:
    print("Fail")

'''

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

d=int(input("enter number 1:"))
e=int(input("enter number2:"))
c=d+e
print("addition",c)

t=int(input("enter number 1:"))
m=int(input("enter number2:"))
c=t+m
print("addition",c)

b=int(input("enter number 1:"))
a=int(input("enter number2:"))
c=b+a
print("addition",c)



a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

'''
print("-------------using function -------------")
print("---------add/multiplication----------")
def add(*a):
    total=0
    for i in a:
        total=total+i
        print("sum:",total)
add(1,2,3,10,15,20,100,110)


def mult(*a):
    total=1
    for i in a:
        total=total*i
        print("summation:",total)
mult(1,2,3,10,15,20,100,110)

print("-------------using funtion ----------------")
class Add:
    def __int__(self,n,a,g):
        self.name=n
        self.age=a
        self.gender=g
    def talk(self):
        print("i am ",self.name)
    def vote(self):
        if self.age<18:
            print("not eligible")
        else:
            print("eligible")
ob=Add("shinu",21,"male")
ob.talk()
ob.vote()

print("-------------find perfect square and divisible by 3 number--------")


import math
num=int(input("Enter number:"))
root = math.sqrt(num)
if int(root + 0.5 ) ** 2 == num :
    print(num,"is a perfect square")
else:
    print(num,"is not a perfect square ")


a=10

a = int(input("Enter your number:"))
a
if a % 3 == 0:
    print("divisible by 3")
else:
    print("not divisible by 3")

'''

        Cost price (in Rs)                                       Tax
        > 100000                                                  15 %
        > 50000 and <= 100000                                     10%
        <= 50000                                                  5%

'''
'''
price= int(input("enetr bike price="))
if price > 100000:
    rint("final bike price is",price+(15/100*price))
elif price > 50000 and price <=  100000:
    print("final bike price is",price+(10/100*price))
elif price <= 50000:
    print("bike price is ",price+(5/100*price))
'''
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

'''
city = input("Enter name of the city")
if city.lower()=="delhi":
    print("Monument name is : Red Fort")
elif city.lower()=="agra":
    print("Monument name is : Taj Mahal")
elif city.lower()=="jaipur":
    print("Monument name is : Jal Mahal")
else:
    print("Enter correct name of city")
'''
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


str1='''welcome pycharm
this is python first program'''
print(str1)

s1='core'
s2=' python'
print(s1,s2)

'''
#cheking membership

str=input("enter main sting")
sub= input("enter sub string")
if sub in str:
    print(sub+" is found in main string")
else:
    print(sub+" is not found in main string ")
'''
print("--------identify operator--------------")
s1= "john is boy"
s2= "riya is girl"
if s1 == s2:odd=[]
even=[]
for i in range(1,100):
    if i % 2 == 0:
        even.append(i)
        if len(even)== 20:
            break
    else:
        odd.append(i)
        if len(odd) == 20:
            break
print(even,odd)


for even_number in range(1,100,2):
    print(even_number)
for odd_number in range(0,100,3):
    print(odd_number)
l=[]
[x+1 for x in range(1,100) if x%2==2]
print(l)


[(i,"Even") if i%2==0 else (i,"Odd") for i in range(1,100)]
print(i)


for n in range(1,100):
    mod = n % 2
    if mod > 0:
        print("This is an odd number. ")
    else:
        print("This is an even number. ")

    print("both are same")
else:
    print("not are same")

print("--------------practice code----------------")

inp = [4,7,2,9,6,3,1]
out = []
square_list = []
i = 2
while i < len(inp) + 3:
    square_list.append(i)
    i = i*2
num_list = []
x = 0
for i in range(len(square_list)):
    num_list.append(x)
    x = x + square_list[i]
for i in num_list:
    if i == 0:
        out.append(inp[0])
num_list.pop(0)
square_list.pop()
for (i,j) in zip(num_list, square_list):
    for x in range(j):
        out.append(inp[i-x])
print(inp)
print(out)

print("------------------------------------")

x = int(input("Enter a number : "))
flag = True
for i in range(1, x):
    if i == 1:
        print(f"{i} is neither prime nor composite number")
    else:
        for j in range(2,i):
            if i%j == 0:
                break
                flag = False
        else:
            print(i)

print("-----------------------------------")

def binary_search(arr,low, high, x):
    if high >= low:
        mid = (high + low) // 2
    else:
        return -1
        arr = [2, 3, 4, 10, 40]
        x = 10
        result = binary_search(arr, 0, len(arr) - 1, x)
        if result != -1:
            print("Element is present at index",result)
        else:
            print("Element is not present in array")
ob=binary_search(arr,2,40,4)

print("-----------------find odd/even number----------")

odd = []
even = []
for i in range(1, 101):
    if i%2 == 0:
        even.append(i)
        if len(even) == 20:
            break
    else:
        odd.append(i)
        if len(odd) == 20:
            break
print(odd, even)
print("--------------using lambda function--------------")

a = lambda x: x*2
print(a(25))

a = lambda y: y**2
print(a(5))

a = lambda z:print(z**2)
a(8)


print("-----------make number pyramids-------------------")

rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')

print("---------------number pyramids-------------")

rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')

print("--------------------------pyramids------------------")

rows = 5
a = 0
for i in range(rows,0,-1):
    a +=1
    for j in range(1,i+1):
        print(a,end='')
        print('\r')

print('------Inverted Pyramid pattern with the same digit-----------')

rows=5
a = rows
for i in range(rows,0,-1):
    for j in range(0, i):
        print(a, end=' ')
    print("\r")

print("--Reverse Pyramid of Numbers---------------")

rows = 6
for i in range(1,rows):
    for j in range(i,0,-1):
        print(j,end='')
        print(" ")

print("--------------string methods-------------")

s = 'welcomeworldgoodmorning'

print(s[-1::-4])
print(s[-1::-2])
print(s[-1::-5])

print("--------------reverse the element using slicing methid----")

s = "welcome python language"
a = (s[-1::-1])
print(a)
b = (a[-1::-1])
print(b)
print("-----------len method-----------")
s = "welcome python language"
a = len(s)
print(a)
for i in range(a):
    print(i)

x = "shinu"
a = "hello wrold"
b = a.replace(a,x)
print("b:",b)

a = "good day welcome python langauge"
old = "good day"
new = "good morning"
b = a.replace(old,new)
print(a)
print(b)


print("------------class and object program------------")

#program 1:

class student:
    #the below block is define attribute
    def __init__(self):
        self.name = "ganesh"
        self.age = 19
        self.Class = "12th"
        #the block is define method
    def display(self):
        print("my name is",self.name)
        print("my age is",self.age)
        print("i am in ",self.Class)
ob = student()
ob.display()

#program 2:

#instance variable and instance method
class student:
    #the below block is define attribute
    def __init__(self):  #this is special method called constructor
        self.name = "ganesh"
        self.age = 19
        self.Class = "12th"
        #the block is define method

    def display(self):       #this is an instance method
        print("my name is",self.name)
        print("my age is",self.age)
        print("i am in ",self.Class)

ob = student()     #create an instance to student class
ob.display()       #call the method using the instance

#program 3: python program to unnderstand instance variable

class Sample:
    def __init__(self):
        self.x = 10
    def modify(self):
        self.x +=1
a=Sample()
b=Sample()
print("x",a.x)
print("x",b.x)
a.modify()
print("x",a.x)
print("x",b.x)

print('------------emplyee -----------------')

class Employee:
    def __init__(self,id,name,salary,exp):
        self.id = id
        self.name = name
        self.salary = salary
        self.exp = exp
    def display(self):
        print("emplyee id is",self.id)
        print("emplyee name is ",self.name)
        print("emplyee salary is",self.salary)
        print("emplyee exp is",self.exp)

ob=Employee(100,"john",45000,3)
ob.display()

class Student:
    def __init__(self,n = ''):
        self.name = n
        #self.marks = m
    def display(self):
        print("hello",self.name)
        #print("your marks is",self.marks)
    def marksheet(self,p,c,m,b,e):
        self.pysics=p
        self.chemistry=c
        self.maths=m
        self.biology=b
        self.english=e
        self.t = p+c+m+b+e
        print("your total Marks is :",self.t)
        self.percentage = self.t/500*100
        if (self.percentage <=  100 and self.percentage >= 75):
            print("you got first grade")
        elif (self.percentage <= 75 and self.percentage >= 65 ):
            print("you have got second grade")
        elif(self.percentage <= 65 and self.percentage >= 55):
            print("you have got third grade")
        elif(self.percentage <=55 and self.percentage >= 45):
            print("pass")
        else:
            print("fail")
n = int(input("how many student ?"))
i = 0
while (i < n):
    name =  input("Enter name :")
    p = int(input("enter pysics marks"))
    c = int(input("enter chemistry marks"))
    m = int(input("enter maths marks"))
    b = int(input("enter biology marks"))
    e = int(input("enter english maths"))
    ob = Student(name)
    ob.display()
    ob.marksheet(p,c,m,b,e)
    i += 1
    #print("total marks is :",t)
'''
# program new########################################

class Student:
    def setName(self,name):
        self.name = name
    def setMarks(self,marks):
        self.marks = marks
    def getName(self):
        return self.name
    def getMarks(self):
        return self.marks
n= int(input("enter number of student"))
i = 0
while(i < n):
    s = Student()
    name = (input("enter student name:"))
    marks = int(input("enter marks:"))
    s.getName()
    s.setName(name)
    s.setMarks(marks)
    print("hi",s.setName(name,marks))
    print('your marks is',s.getName())
    i += 1


'''
class Bird:
    wings = 2
    def fly(cls,name):
        print("{} flies with {} wings".format(name,cls.wings))
ob=Bird()
ob.fly("parrot")
ob.fly("pigeon")

class Animals:
    legs = 4
    def walk(cls,name):
        print("{} walking in {} legs".format(name,cls.legs))
ob = Animals()
ob.walk("lion")
ob.walk("tiger")
ob.walk("cow")

print("----------------withdraw and deposite programe------------------------")
import sys
class Bank:
    def __init__(self,name,balance = 0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            print("balance amount is less,so no withdraw.")
        else:
            self.balance -= amount
        return self.balance
name = input("enter name is")
while(True):
    print('d - deposit,w - withdraw, e - exit')
    choice = input("enter your choice")
    if choice == 'e' or choice == 'E':
        sys.exit()
    amt = float(input("enter amount: "))
    if choice =='d' or choice =='D':
        print('print balance after deposit')
    elif choice == 'w' or choice == 'W':
        print("blance after withdraw")
ob = ob=Bank(name)
ob.withdra(amt)
ob.deposit(amt)

print("------python program with date of birth within person class-------")

class Person:
    def __init__(self):
        self.name = "john"
        self.db = self.Dob()
    def display(self):
        print("name=",self.name)
    class Dob:
        def __init__(self):
            self.dd = 4
            self.mm = 2
            self.yy = 1995
        def display(self):
            print("Dob = {}/{}/{}".format(self.dd,self.mm,self.yy))
a = Person()
a.display()
b = a.db
b.display()

print("----------------date of birth------")

class Student:
    def __init__(self):
        self.name = "Rocky"
        self.db = self.Dob()
    def display(self):
        print("hi ",self.name)
    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yy = 2000
        def display(self):
            print("your Dob is = {}/{}/{}".format(self.dd,self.mm,self.yy))
ob= Student()
ob.display()
ob1 = ob.db
ob1.display()

print("--------emplyee details ---------------")

class Employee:
    #this is consructor
    def __init__(self,id,name,salary,expe):
        self.id = id
        self.name = name
        self.salary = salary
        self.expe = expe
    def display(self):
        print("Employee id is:",self.id)
        print("Employee Name is:",self.name)
        print("Employee Salary is:",self.salary)
        print("Employee Experience is:",self.expe)
class Myclass:
    def mymethod(e):
        e.salary += 10000
        e.display()
e = Employee(100,"john",45000,3)
Myclass.mymethod(e)

print("--------------Example for static method---------")

print("pytho programm to calculate power value of a number with the help of a static method")

class Myclass:
    def mymethod(x,n):
        result = x**n
        #print("{} to the power of {} is {} ".format(x,n,result))
        print("{} power {} is {}".format(x,n,result))

Myclass.mymethod(5,1)
Myclass.mymethod(5,2)
Myclass.mymethod(5,3)
Myclass.mymethod(5,4)
Myclass.mymethod(5,5)
Myclass.mymethod(5,6)
Myclass.mymethod(5,7)
Myclass.mymethod(5,8)
Myclass.mymethod(5,9)
Myclass.mymethod(5,10)

class Mobile:
    def __init__(self):
        self.model = "Nokia"
        self.price = 20000
        print("model Name: ",self.model)
        print("mobile price: ",self.price)
ob = Mobile()

print("---------------positional arguments------")

class Add:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
a = Add("john",21)
a.display()

print("----------default arguments---------")

def add(x,y=20):
    c = x+y
    print("addition",c)
add(10)

print("-----------keywords arguments--------------")

def person(name,age,gender):
    print("my name is : ",name)
    print("my age is : ",age)
    print("i am : ",gender)
person(name="shinu",age=25,gender="male")

class Mobile:
    def __init__(self,m,v=80):
        self.model = m
        self.volumn = v
    def display(self,p):
        self.price = p
        print('model: ',self.model)
        print("volumn : ",self.volumn)
        print("price of mobile : ",self.price)
ob = Mobile("nokia",100)
ob.display(20000)

print("------------encapsulation program---------------")

class Abc:
    def getvalue(self,x):
        self.a = x
    def fun(self):
        print(self.a)
ob = Abc()
ob.getvalue(100)
ob.fun()

print("-----protected and private member-----------")

class Super:
    def __init__(self):
        self._value1 = 100
        self.__value2 = 200
    def display(self):
        print(self._value1)
        print(self.__value2)
class Sub(Super):
    def show(self):
        print(self._value1)
        print(self.__value2)

ob = Sub()
ob.show()

print("-----------Abstraction -------------------")

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self,r):
        self.radius = r
        print("Area of circle is :",3.14*r*r)

class Square(Shape):
    def area(self,l):
        self.length = l
        print("Area of square",l*l)

c1 = Circle()
c1.area(4)
s1=Square()
s1.area(6)

'''
 feature os object oriented programming system
1. class and object
2. Encapsulation 
3. Abstraction
4. Inheritance
5. Polymorphism


'''

print("--------------------metho overloadong----------")

class Sumation:
    def calculation(self,x = None, y = None):
        if x == None and y == None:
            print("Welcome python prograamm")
            print("thanks for visit")
        elif x != None and y == None:
            f=1
            for i in range(1,x+1):
                f = f*i
            print(f)
        else:
            print("addition",x+y)

ob=Sumation()
ob.calculation()
ob.calculation(5)
ob.calculation(100,200)

print("----------over riding----------")

class A:
    def add(self):
        print("hii")
class B(A):
    def add(self):
        print("hello")
    def xyz(self):
        print("good morning")

ob = A()
ob1 = B()
ob.add()
ob1.add()
ob1.xyz()

print("--------------------------------control statement-----------------------------------")
print("----------break/ continue / pass---------------")

for i in range(1,10):
    if i == 5:
        break
        print(i)

for i in range(1,10):
    if i == 6:
        continue
        print(i)
        i += 1

str1 = "python"
for i in str1:
    if i == 'h':
        break
        print(i)


import copy
l = [[1,2],[3,4]]
a = copy.deepcopy(l)
print(a)

a[0][0] = 12
print(a)

n = [m for m in range(1,101) if m % 2 == 0 or m % 3 ==0]
print(n)


print("------------------------------------------progranm practice-------------------------")


print("--------------using lambda function--------------")

a = lambda x: x*2
print(a(25))

a = lambda y: y**2
print(a(5))

a = lambda z:print(z**2)
a(8)
a(12)
a(13)
a(100)

a = lambda p,r,y: print("simple intrest",p*r*y/100)
a(20000,8.10,3)


p=int(input("enter principle"))
r=int(input("enter rate of intrest"))
y= int(input("enter year"))
a = lambda p,r,y: print("simple intrest",p*r*y/100)
a(p,r,y)

p=int(input("enter principle"))
r=int(input("enter rate of intrest"))
y= int(input("enter year"))
a = lambda p,r,y: p*r*y/100
print("simple intrest",a(p,r,y))


print('-------------lambda using def funtion--------------')

def sumation(a,b,c):
    return lambda x: a*x**2+b*x+c
a=sumation(10,5,2)
print(a(20))
print(a(10))
print(a(5))
print(a(2))

print("-----------lambda function( map,filter,reduce)----------------")
print("----map-------")
a = (2,4,6,8,10)
result = map(lambda x: x+x,a)
print(list(result))

a=(1,2,3,4,5,6)
b=(1,2,3,4,5,6)
result=map(lambda x,y: x+y,a,b)
print(list(result))

a = [1,2,3,4,5]
result = map(lambda x: x,a)
print(list(result))

a = (1,2,3,4,5)
b = (9,8,7,6,5)
c = (1,2,3,4,5)
result = map(lambda x,y,z: x+y+z,a,b,c)
print(list(result))

print("==============map in list-------------------")
l = ['cat','bat','mat','rat']
result = list(map(list,l))
print(result)

print("----------map in list add two list-----------")

l = ['cat','bat','mat','rat']
m = ['hat','cat','nat','eat']
result= list(map(list,l+m))
print(result)

import functools

lis = [1, 3, 5, 6, 2, ]
#print("The sum of the list elements is : ", end="")

a = functools.reduce(lambda x,y: x+y,lis)
print(a)
#print(functools.reduce(lambda a, b: a + b, lis))



seq = [0, 1, 2, 3, 5, 8, 13]
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


print("//////////////////////////////////////////////////////////////////")

print("-----------------find odd/even number----------")

odd = []
even = []
for i in range(1, 101):
    if i%2 == 0:
        even.append(i)
        if len(even) == 20:
            break
    else:
        odd.append(i)
        if len(odd) == 20:
            break
print(odd, even)

print("/////////////////////////////////////////////////////////////////////////////////")

print("-------------------to check perfect square---------------------------")

import math

num = int(input("Enter number:"))
root = math.sqrt(num)
if int(root + 0.5) ** 2 == num:
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square ")

print("--------------divisible by 3 check---------------")
a = int(input("Enter your number:"))
if a % 3 == 0:
    print("divisible by 3")
else:
    print("not divisible by 3")


print("---------add/multiplication using function----------")
def add(*a):
    total=0
    for i in a:
        total=total+i
        print("sum:",total)
add(1,2,3,10,15,20,100,110)


def mult(*a):
    total=1
    for i in a:
        total=total*i
        print("summation:",total)
mult(1,2,3,10,15,20,100,110)

print("------------------------------factorial find--------------------------")

n=int(input("Enter factorial number:"))
if (n == 0 or n == 1):
    print(1)
else:
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    print(fac)


print("--------------------------------control statement-----------------------------------")
print("----------break/ continue / pass---------------")

for i in range(1,10):
    if i == 5:
        break
        print(i)

for i in range(1,10):
    if i == 6:
        continue
        print(i)
        i += 1


print("------------- *arg / non keyword arguments------------")

def myfun(*args):
    for i in args:
        print(i)
myfun("hello ","VN2 solution pvt ltd")

print("-------------- **karg / keyword arguments")

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
# Driver code
myFun(first='Ganesh', mid='Subhash', last='Topale')

l = "python"
a = l.split()
print(a)


'''

Instructions:
---------------
	1. Use proper namaing conventions
	2. Use pep8 standards
	3. Write readable and clean code
	4. Where ever required use functions,oops,exception hanlding etc.,
	5. Give detailed comments if required
	6. Write all programs in one .py file

	For ex:

	EID_Name.py
	------------
	print("--------------Program 1-------------------")
	print(" ------Get ODD NUMBERS -----")
	print(" ------- 1.a. List Comprehension ------ ")
		code
	print(" ------- 1.b. Normal For Loop -------")
		code
	print(" ------- 1.c. Generator mechanism ----")
		code

After writing program, write your own explanation for each problem.


1. Implement palindrome using iterator(for loop) and generator mechanism.

2. Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9
		         10 + 11 + 12 + 13
				 46

3. st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba

4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format


5. # t1 = (1, 2, 3, "a", "c")
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")

6  #Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196

7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]

8. Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total

'''

print("////////////////////////////////////////////////////////////////////////////////////////////////////")

print(" ------- 1.a. List Comprehension ------ ")

def palindrome(s):
    for i in range(0,len(s)-1):
        if s[i] == s[i][::-1]:
            return s[i]
words = ['foof','boom']
print(palindrome(words))

print("1. (b) Implement palindrome using iterator(for loop) and generator mechanism.")

number = input("Enter any number :")
i=0
for i in range(len(number)):
    if number[i]!=number[-1-i]:
        print('It is not a palindrome')
        break
    else:
        print('It is a palindrome')
        break

print(" ------- 1.c. Generator mechanism ---------------------")

print("////////////////////////////////////////////////////////////////////////////////////////")

print(''' Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9
		         10 + 11 + 12 + 13
				 46
''')

n1 = 1234
n2 = 9999
def add(n1,n2):
    l1 =[]
    l2 = []
    l3 = []
    result=[]
    strn1 =str(n1)
    strn2 =str(n2)
    for i in strn1:
        l1.append(int(i))
    for j in strn2:
        l2.append(int(j))
    for (x,y) in zip(l1,l2):
        result.append(x+y)
        print(result)

add(n1,n2)

print("/////////////////////////////////////////////////////////////////////////////////")

print("--3.  #Reverse string considering only alphabets. Symobls should not be reversed")

strSample = "ab@#cd!ef"
# convert string into list
listSample = list(strSample)

i = 0
j = len(listSample) - 1

while i < j:
    if not listSample[i].isalpha():
        i += 1
    elif not listSample[j].isalpha():
        j -= 1
    else:
        listSample[i], listSample[j] = listSample[j], listSample[i]
        i += 1
        j -= 1
strOut = ''.join(listSample)
print(strOut)

print("///////////////////////////////////////////////////////////////////////////")

print('''4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"] #findout elements duplicate count output in  dict format''')

def getDuplicatesWithCount(listOfElems):
    dictOfElems = dict()
    # Iterate over each element in list
    for elem in listOfElems:
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1
    dictOfElems = {key: value for key, value in dictOfElems.items() if value > 1}

    return dictOfElems
# List of strings
listOfElems = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
dictOfElems = getDuplicatesWithCount(listOfElems)
for key, value in dictOfElems.items():
    print(({key :value}))

print("////////////////////////////////////////////////////////////////////////////////////////////")

print('''5. # t1 = (1, 2, 3, "a", "c")
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")''')

t1 = (1,2,3,'a','c')
t2 = (9,8,7,'b','d')
a = list(t1)
b = list(t2)
c = print(a)
d = print(b)
result=map(lambda x,y: x+y,a,b)
print(list(result))

print("///////////////////////////////////////////////////////////////////////////////////////")

print('''6  #Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196''')

str1 = "216.08.094.196"
list1 = []
for i in str1:
    if i != "0":
        list1.append(i)
strr = ''.join(list1)
print(strr)

print("/////////////////////////////////////////////////////////////////////////")

print('''7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10] ''')


l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
output=[]
final_out=[]
for item in l:
    if type(item)==list:
        output.extend(item)
    else:
        output.append(item)
for item2 in output:
    if type(item2)==list:
        final_out.extend(item2)
    else:
        final_out.append(item2)
print(final_out)

print("////////////////////////////////////////////////////////////////////////////////")

print('''8. Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total ''')



string = '''Moving to a new country and starting over is always appealing.\n
          The idea of meeting different people, traveling to places you’ve never been before,\n
          and learning a new culture seems exciting and enjoyable.'''

print(" ---------------------1. No of lines in file-----------------")
count = len(string.split("\n"))

print(string.split("\n"))
print(count)

print("---------------2. No of words in each line-------------")

a = " my name is Ganesh"
print(len(a))

print('''	3. No of chars in each line''')

b = " my name is ganesh i am from nagpur"
c = b.split(" ")
print(len(c))

print("--------------4. No of vowels and consonants-------------------")

def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)
string = " my name is Ganesh. and i am from nagpur"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels)

print("--------------5. No of special chars linewise and total--------------")


def count_special_character(string):
    special_char = 0

    for i in range(0, len(string)):
        ch = string[i]
        if (string[i].isalpha()):
            continue
        elif (string[i].isdigit()):
            continue

        else:
            special_char += 1
    if special_char >= 1:
        print(" {} Special Character in this string  ".format(special_char))
    else:
        print("There are no Special Characters in this String.")
if __name__ == '__main__':
    string = "vn2%^solution&*@$python"
    count_special_character(string)


