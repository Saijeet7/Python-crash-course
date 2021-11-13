# Sets : unordered, mutable, no dublicates,

mySet={1,2,3,4,5,1,2}
mySet2 = set("Hello")

for i in mySet:
    print(i)

odds = {1,3,5,7,9}
evens={2,4,6,8}
primes={2,3,5,7}

u= odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setB.difference(setA)
print(diff)

sydiff = setB.symmetric_difference(setA)
print(sydiff)

# setA.update(setB)
# print(setA)

setA.intersection_update(setB)
print(setA)

print(setA.issubset(setB))


a= frozenset([1,2,3,4])