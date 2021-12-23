#Task1

Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]

#5
print(Li1[3])

#56
print(Li1[4][1])

#222
print(Li1[4][4][1])

#50000
print(Li1[4][4][3][2][1])

#put
print(Li1[4][4][3][2][3][3:6])

#5555
print(Li1[4][4][3][0])

#7777
print(Li1[4][4][3][4])

#666
print(Li1[4][4][6])

#89
print(Li1[4][5])

#on
print(Li1[4][4][3][2][2][-2:])

#333
print(Li1[4][4][2])

#3333
print(Li1[4][4][3][1])





#Task2

a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]

#science
print(a[4][-1][-7:])

#computer
b=(a[4][-1][0:8])
c=b.casefold()
print(c)





#Task3

a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]

#666
print(a[4][-2])

#201
print(a[4][3][0])

#102
print(a[4][1])

#999
print(a[4][3][-1][0])

#777
print(a[4][-1])





#Task4

Li2 = [2,3,"python","hello",4,5,0] 

#ll
print(Li2[3][2:4])

#thon
print(Li2[2][2:])






#Task6

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}

#py
print(a[1][-1][0:2])

#ello
print(a[2][10][1:])

#en
print(a[2][40][3:5])

#zoo
print(a[40][1][0:3])

#Bot
print(a[40][2][0:3])
