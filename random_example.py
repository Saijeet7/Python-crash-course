import random

a = random.normalvariate(0, 1)
print(a)

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))


random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))


mylist = list("ABCDEFGHIJK")
random.shuffle(mylist)
print(mylist)
a = random.choices(mylist,k=3)
print(a)
