n = int(input())

ThisDict = dict()
for i in range(n):
    text_1 = input().split()
    ThisDict[text_1[0]] = text_1[1]

m = int(input())
ThisList = list()
for i in range(m):
    text_2 = input()
    ThisList.append(text_2)

for i in range(n):
    if ThisDict.__contains__(ThisList[i]):
        ThisList.append(ThisDict.get(ThisList[i]))
        ThisDict.pop(ThisList[i])
        del(ThisList[i])

print(ThisDict)
print(ThisList)
