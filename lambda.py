#Lambda arguments: expression

add10 = lambda x:x +10
print(add10(10))

mult = lambda x,y: x*y
print(mult(10,2))

points2D = [(1,2),(15,1),(5,-1),(10,1),(10,4)]
points2D_sorted = sorted(points2D, key=lambda x:x[0] + x[1])

print(points2D)
print(points2D_sorted)

#map(func, sequences)

a=[1,2,3,4,5,6]
b=map(lambda x:x*2, a)
print(list(b))

c=[x*2 for x in a]
print(c)

#filter (funct, seq)

d = filter(lambda x:x%2==0,a)
e = [x for x in a if x%2==0]
print(list(d))
print(list(e))

#reduce(func,seq)
from functools import reduce
product_a = reduce(lambda x,y:x*y, a)
print(product_a)