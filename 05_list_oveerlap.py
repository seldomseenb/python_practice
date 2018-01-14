import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commons = []

for i in a:
	if i in b:
		commons.append(i)

print(a)
print(b)
print(commons)


c = random.sample(range(100), random.randint(5,10))
d = random.sample(range(100), random.randint(5,10))
commons2 = []

for j in c:
	if j in d:
		commons2.append(j)

print("Random Lists")
print(c)
print(d)
print(commons2)