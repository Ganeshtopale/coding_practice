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

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)
a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)


a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)

a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
print("addition",c)


a=int(input("enter number 1:"))
b=int(input("enter number2:"))
c=a+b
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








