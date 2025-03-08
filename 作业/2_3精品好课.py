n, m = map(int, input().split())
name = input().split()
list = []
for i in range(m):
    list.extend(input().split())

learned = set(list)
print(n-len(learned))