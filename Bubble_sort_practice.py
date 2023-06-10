print('.......sorting of element............')

x = [ 5, 3, 8, 6, 7, 2 ]
x.reverse()
x.sort()
print(x)
#####################################################

print(".......Bubble sort........")
print("...accending order........")

x = [3, 4, 6, 2, 8, 18, 17, 15, 20]
for i in range(0, len(x)):
    for j in range(0, len(x) - 1):
        if x [j] > x [j + 1]:
            c = x [j]
            x [j] = x [j + 1]
            x [j + 1] = c
print(x)

#########################################################

lst = [3, 5, 2, 7, 5, 8, 10, 15, 11, 14]
for i in range(0, len(lst)):
    for j in range(0, len(lst) - 1):
        if lst[j] > lst[j + 1]:
            x = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = x
print(lst)

################################################################

x = ["mango", "chiku", "chaku", "apple", "orange", "banana"]
for i in range(0, len(x)):
    for j in range(0, len(x) - 1):
        if x[j] > x[j + 1]:
            c = x[j]
            x[j] = x[j + 1]
            x[j + 1] = c
print(x)

#############################################

lst = [3, 5, 2, 7, 5, 8, 10, 15, 11, 14]
for i in range(0, len(lst)):
    for j in range(0, len(lst) - 1):
        if lst[j] > lst[j + 1]:
            c = lst[j]
            lst[j] = lst[j + 1]
            lst[j+1] = c
print(lst)

###############################################

x = [1, 4, 6, 5, 3, 8, 4, 15, 14, 12, 11, 20]
for i in range (0,len(x)):
    for j in range(0,len(x)-1):
        if x[j] > x[j+1]:
            c = x[j]
            x[j] = x[j+1]
            x[j+1] = c
print(x)

####################################################

print("....decending order.......")

x = [1, 4, 6, 5, 3, 8, 4, 15, 14, 12, 11, 20]
for i in range(0, len(x)):
    for j in range(0, len(x) - 1):
        if x[j] < x[j + 1]:
            c = x[j]
            x[j] = x[j + 1]
            x[j + 1] = c
print(x)

#############################################

a = ["raju",'xerox',"ankita","anushka","zebra","yak","ox"]
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if a[j] < a[j+1]:
            c = a[j]
            a[j] = a[j+1]
            a[j+1] = c
print(a)

###################################################

x = [5,3,8,6,7,2]
for i in range(0,len(x)):
    for j in range(0,len(x)-1):
        if x[j] > x[j+1]:
            c = x[j]
            x[j] = x[j+1]
            x[j+1] = c
print(x)

#####################################################

x = [3,2,6,8,4,19,16,15,22]
for i in range(0,len(x)):
    for j in range(0,len(x)-1):
        if x[j] > x[j+1]:
            c = x[j]
            x[j] = x[j+1]
            x[j+1] = c
print(x)

#####################################################

a = ['ganesh',"shinu",'yogesh','sachin','rishi','aaryan']
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if a [j] > a [j+1]:
            x = a[j]
            a [j] = a [j+1]
            a [j+1] = x
print(a)
a = ['ganesh',"shinu",'yogesh','sachin','rishi','aaryan']
lst = a.sort()
print(lst)

#######################################################################