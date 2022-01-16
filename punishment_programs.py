#PROGRAM 1- factorial
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)  #why write 'factorial(n-1)'

num=int(input())
print ("Factorial of",num,"is",
      factorial(num))



#PROGRAM 2- simple interest
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si)
    return si #is this line necessary?




#PROGRAM 3- compound interest
def compound_interest(principle, rate, time):
 
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)  #Why is return line not present but the code still works?




#PROGRAM 4- prime numbers in an interval
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list



#PROGRAM 5- checking if a number is a prime number
if num > 1:
  
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
  
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")




#PROGRAM 6- trying to find the n-th Fibonacci number
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)    #How does last line work?




#PROGRAM 7- checking if a number is part of the Fibonacci sequence

#A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
import math
 
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
    
for i in range(1,11):
     if (isFibonacci(i) == True):
         print i,"is a Fibonacci Number"
     else:
         print i,"is a not Fibonacci Number "




#PROGRAM 8- sum of squares of first n natural numbers
def squaresum(n) :

    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i * i)
      
    return sm



#PROGRAM 9- to find sum of elements
def _sum(arr): 
    sum=0
    for i in arr:
        sum = sum + i     
    return(sum) 




#PROGRAM 10- finding the maximum of two numbers
def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b




#PROGRAM 11- finding ASCII value
c = 'g'
print("The ASCII value of '" + c + "' is", ord(c))





#PROGRAM 12- finding cube sum of first n natural numbers
def sumOfSeries(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i*i*i         
    return sum







#PROGRAM 13- finding largest element in an array
def largest(arr,n):
  
    # Initialize maximum element
    max = arr[0]
  
    # Traverse array elements from second
    # and compare every element with current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max






#PROGRAM 14- swapping first and last element
def swapList(newList):
    size = len(newList)
     
    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList







#PROGRAM 15

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))#Remember to write pos1-1, not pos1





#PROGRAM 16- checking if an element is present in the list

# Python code to demonstrate checking of element existence using loops and in
 
# Initializing list
test_list = [ 1, 6, 3, 5, 3, 4 ]
 
print("Checking if 4 exists in list ( using loop ) : ")
 
# Checking if 4 exists in list using loop
for i in test_list:
    if(i == 4) :
        print ("Element Exists")
 
print("Checking if 4 exists in list ( using in ) : ")
 
# Checking if 4 exists in list using in
if (4 in test_list):
    print ("Element Exists")





#PROGRAM 17- how to clear a list

# Python3 code to demonstrate clearing a list using clear and Reinitializing 
  
# Initializing lists
list1 = [1, 2, 3]
list2 = [5, 6, 7]
  
# deleting list using clear()- method 1
list1.clear()

  
# deleting list using reinitialization- method 2
list2 = []







#PROGRAM 18- how to reverse a list
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
      
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))






#PROGRAM 19- finding sum of elements in a list
total = 0
 
# creating a list
list1 = [11, 5, 17, 18, 23]
 
# Iterate each element in list and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]






#PROGRAM 20- multiply all numbers in a list
def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x
    return result


#PROGRAM 21- finding the second largest element in a list
list1 = [10, 20, 4, 45, 99]
 
# sorting the list
list1.sort()
 
# printing the second last element
print("Second largest element is:", list1[-2])



#PROGRAM 22- find n largest elements in a list
l = [1000,298,3579,100,200,-45,900]
n = 4
  
l.sort()
print(l[-n:])




#PROGRAM 23- print even numbers in a list
list1 = [10, 21, 4, 45, 66, 93]
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")



#PROGRAM 24- print odd numbers in a list
list1 = [10, 21, 4, 45, 66, 93]
  
# iterating each number in list
for num in list1:
      
    # checking condition
    if num % 2 != 0:
       print(num, end = " ")




#PROGRAM 25- finding all even numbers in a range
start, end = 4, 19
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 == 0:
        print(num, end = " ")



#PROGRAM 26- finding all odd numbers in a range
start, end = 4, 19
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")




#PROGRAM 27- finding all positive numbers in list
list1 = [11, -21, 0, 45, 66, -93]
  
# iterating each number in list
for num in list1:
      
    # checking condition
    if num >= 0:
       print(num, end = " ")



#PROGRAM 28- finding all negative numbers in list
list1 = [11, -21, 0, 45, 66, -93]
  
# iterating each number in list
for num in list1:
      
    # checking condition
    if num < 0:
       print(num, end = " ")



#PROGRAM 29- finding all positive numbers in a range
start, end = -4, 19
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num >= 0:
        print(num, end = " ")



#PROGRAM 30- finding all negative numbers in a range

start, end = -4, 19
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num < 0:
        print(num, end = " ")


#PROGRAM 31- removing all even numbers in a list
list1 = [11, 5, 17, 18, 23, 50]
 
# Iterate each element in list and add them in variable total
for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)
 
print("New list after removing all even numbers: ", list1)



#PROGRAM 32- removing empty list from list
test_list = [5, 6, [], 3, [], [], 9]
res = list(filter(None, test_list))



#PROGRAM 33- cloning/copying a list
def Cloning(li1):
    li_copy = li1[:]
    return li_copy



#PROGRAM 34- counting the frequency of an element
def countX(lst, x):
    return lst.count(x)



#PROGRAM 35- removing empty tuples
def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples


#PROGRAM 36- showing count of all elements in a list
from collections import Counter
 
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)




#PROGRAM 37- finding cumulative sum of a list
list=[10,20,30,40,50]
new_list=[]
j=0
for i in range(0,len(list)):
    j+=list[i]
    new_list.append(j)
     
print(new_list)




#PROGRAM 38- finding the smallest number
list1 = [10, 20, 4, 45, 99]
 

list1.sort()
 

print("Smallest element is:", *list1[:1])




#PROGRAM 39- finding largest number in a list
list1 = [10, 20, 4, 45, 99]
  
list1.sort()
  
print("Largest element is:", list1[-1])




#PROGRAM 40

my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']
  
# Yield successive n-sized chunks from l.
def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]
  
# How many elements each list should have
n = 5
  
x = list(divide_chunks(my_list, n))
print (x)



#PROGRAM 41- adding two matrices

# Program to add two matrices using nested loop
 
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)






#PROGRAM 42- multiply two matrices

# Program to multiply two matrices using nested loops
 
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
 
# iterating by row of A
for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)








#PROGRAM 43- adding and subtracting in matrices
import numpy as np
  
  
# creating first matrix
A = np.array([[1, 2], [3, 4]])
  
# creating second matrix
B = np.array([[4, 5], [6, 7]])
print(np.add(A, B))
print(np.subtract(A, B))








#PROGRAM 44- palindrome check
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")









#PROGRAM 45- reversing a string
def rev_sentence(sentence): 
  
    # first split the string into words 
    words = sentence.split(' ') 
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words)) 
  
    # finally return the joined string 
    return reverse_sentence 
  
if __name__ == "__main__": 
    input = 'geeks quiz practice code'
    print (rev_sentence(input))




#PROGRAM 46- finding length of string
str = "geeks"
print(len(str))



#PROGRAM 47- printing even length words in string

  
def printWords(s):
      
    # split the string 
    s = s.split(' ') 
      
    # iterate in words of string 
    for word in s: 
          
        # if length is even 
        if len(word)%2==0:
            print(word) 
  




#PROGRAM 48- finding sum of all values in dict
def returnSum(myDict):
     
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
     
    return final





#PROGRAM 49- removing a key in dict using del function
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
  
# Printing dictionary before removal
print ("The dictionary before performing remove is : " + str(test_dict))
  
# Using del to remove a dict
# removes Mani
del test_dict['Mani']






#PROGRAM 50- merging 2 dicts 
def Merge(dict1, dict2):
    return(dict2.update(dict1))



#Doubts about armstrong number program
#Python Program for n\’th multiple of a number in Fibonacci Series
#Array splitting
#Sum of number digits in List
#Python Program for Reversal algorithm for array rotation
#Python Program to check if given array is Monotonic
#Sort the values of first list using second list in Python

