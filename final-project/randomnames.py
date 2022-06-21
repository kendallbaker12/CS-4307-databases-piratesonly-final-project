from itertools import count
from random import randint

counter = {}
i = 0
while i < 167:
    RandomNumber = (randint(1,20))
    if RandomNumber in counter:
        counter[RandomNumber] += 1
    else:
        counter[RandomNumber] = 1

    i += 1
    
sorted_age = sorted(counter.items(), key = lambda kv: kv[1])
print(sorted_age)