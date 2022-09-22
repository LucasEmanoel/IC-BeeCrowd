soma = 0
x = int(input())
y = int(input())

if x > y:
    for i in range(x, y):
        if x % 13 != 0:
            soma += i
else:
    for i in range(y, x):
        if x % 13 != 0:
            soma += i

print(soma)