n = int(input())
b = str(n)
c = 0
for i in range(0, n):
    a = (i + 1) * b
    a = int(a)
    c = c + a
print(c)
