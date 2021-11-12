# Tuple: ordered, immutable(Cannot be changed), allows dublicate elements

a=(1,2,3,4,5,6,7,8,9,10)

b = a[7:2:-1]
print(b)

my_tuple = "Max",28,"Boston"
name , age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0,1,2,3,4)
i1, *i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)