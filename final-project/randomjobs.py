import random


joblist = ["carpenter","cabin boy","powder monkey","swabbies","quartermaster","boatswain","Sailing Master"]
rando = []
for i in range(0,4):
    n = random.choice(joblist)
    rando.append(n)
print(rando)