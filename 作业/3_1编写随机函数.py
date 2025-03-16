import random

def my_random(keys, weights):
    lis = []
    for e, n in zip(keys, weights):
        lis.extend([e] * n)
    
    return lis[random.randrange(len(lis))]

for i in range(10):
    print(my_random(keys=['a', 'b', 'c'], weights=[1, 1, 2]))