# put your python code here
a = int(input())
b = int(input())
num = list()

for x in range(a, b+1):
    if x % 3 == 0:
        num.append(x)

print(sum(num) / len(num))
