#Create an empty list (two ways)

a= []
b= list()


#Concatenate with [5,6,7,8]

A= [1,2,3,4]
B= [5,6,7,8]
c= (A+B)
print(c)



#add 8,9,1,5,6,7,8,1 elements to that list

d= [8,9,1,5,6,7,8,1]
e= (c+d)
print(e)



#Find frequency of 8 (count)


print(e.count(8))




#find the mean of the list

print(sum(e))
print(81/16)


#find sum (List) + min + Max


print(sum(e))
print(max(e))
print(min(e))



#Find median of the list

e.sort()
print(e)
print(e[7])
print(e[8])
median=(5+6)/2
print(median)





#remove duplicates from list and give output in the format of tuple

e.remove(1)
e.remove(1)
e.remove(5)
e.remove(6)
e.remove(7)
e.remove(8)
e.remove(8)
print(e)
