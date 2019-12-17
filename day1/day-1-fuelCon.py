import math

bigList = []
myfile = open('dataSet.txt', mode='r').readlines()
for line in myfile:
    bigList.append(math.floor(int(line)//3)-2)

numT = 0
for num in bigList:
    numT = numT + num

print(numT)
input() 