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