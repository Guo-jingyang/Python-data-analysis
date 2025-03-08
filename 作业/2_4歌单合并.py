list = []
n = int(input())
for i in range(n):
    count = int(input())
    for j in range(count):
        list.append(tuple(input().split()))

list.sort(key=lambda x:int(x[1]), reverse=True)

for i in list:
    print(i[0], i[1])