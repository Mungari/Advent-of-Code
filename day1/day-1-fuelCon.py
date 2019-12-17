import math

def fuelRecurs(fuel):
    f = (int(fuel)//3)-2
    if(f <= 0):
        pass
    else:
        fuelList.append(f)
        fuelRecurs(f)

bigList = []
with open('dataSet.txt', mode='r') as myfile:
    for line in myfile.readlines():
        bigList.append(int(line)//3-2)

fuelList = []
for fuel in bigList:
    fuelList.append(fuel)
    fuelRecurs(fuel)

print(sum(fuelList))
input() 