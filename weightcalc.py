import csv
from collections import Counter

#Mean
with open("WH.csv", newline = "" ) as f:
    reader = csv.reader(f)
    listData = list(reader)

listData.pop(0)
weightData = []
for i in range(len(listData)):
    num = listData[i][2]
    weightData.append(float(num))
totalWeight = 0 
for i in weightData:
    totalWeight += i
n = len(weightData)
mean = totalWeight/n
print("This is the average weight: " +str(mean))


#Median
with open("WH.csv", newline = "" ) as f:
    reader = csv.reader(f)
    listData = list(reader)

listData.pop(0)
weightData = []

for i in range(len(listData)):
    num = listData[i][2]
    weightData.append(float(num))

weightData.sort()
n = len(weightData)

if(n % 2 == 0):
    median1 = float(weightData[n//2])
    median2 = float(weightData[n//2 -1])
    median = (median1 + median2)/2
else:
    median = float(weightData[n//2])

print("The median weight is " + str(median))



#Mode
with open("WH.csv", newline = "" ) as f:
    reader = csv.reader(f)
    listData = list(reader)

listData.pop(0)
weightData = []

for i in range(len(listData)):
    num = listData[i][2]
    weightData.append(float(num))

modeData = Counter(weightData)

modeDataforRange = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0,
    '165-175':0
}

#print(modeData.items())
for weight, occurance in modeData.items():
    if 75<float(weight)<85:
        modeDataforRange["75-85"] += occurance
    elif 85<float(weight)<95:
        modeDataforRange["85-95"] += occurance
    elif 95<float(weight)<105:
        modeDataforRange["95-105"] += occurance
    elif 105<float(weight)<115:
        modeDataforRange["105-115"] += occurance
    elif 115<float(weight)<125:
        modeDataforRange["115-125"] += occurance
    elif 125<float(weight)<135:
        modeDataforRange["125-135"] += occurance
    elif 135<float(weight)<145:
        modeDataforRange["135-145"] += occurance
    elif 145<float(weight)<155:
        modeDataforRange["145-155"] += occurance
    elif 155<float(weight)<165:
        modeDataforRange["155-165"] += occurance
    elif 165<float(weight)<175:
        modeDataforRange["165-175"] += occurance

modeRange, modeOccurance = 0, 0
for range, occurance in modeDataforRange.items():
    if occurance > modeOccurance:
        modeRange, modeOccurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance
mode = float(modeRange[0]+modeRange[1])/2

print("The mode weight is " + str(mode))







