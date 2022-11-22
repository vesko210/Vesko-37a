n = int(input())
list = []
for i in range(n):
    list.append(i)
a = int(input())
for j in range(0, len(list)):
    if a == 0 and list[j] % 2 == 0:
        list[j] = j + 10
    if a == 1 and list[j] % 2 != 0:
        list[j] = j + 5
print(list)
