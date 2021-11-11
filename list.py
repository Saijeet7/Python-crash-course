#List: ordered, mutable, allows to duplicate elements

mylist =[1,2,3,4,5,6,7,8,9]
a = mylist[::2]
print(a)

list_org = ["banana","cherry","apple"]

list_cpy = list_org

list_cpy.append("lemon")

print(list_cpy)
print(list_org)

a=[1,2,3,4,5,6,7,8,9]
b = [i*i for i in a]

print(a)
print(b)