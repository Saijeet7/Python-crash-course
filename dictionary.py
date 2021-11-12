#Dictionary: Key-value pairs, Unordered, Mutable
myDict = {"name":"Max", "age":28 , "city":"Newyork"}
print(myDict)

mydict_cpy = myDict.copy()

mydict_cpy["email"] = "max@max.com"
print(mydict_cpy)
print(myDict)

diction = {"name":"Saijeet","age":25,"email":"sai@gmail.com"}
diction2 = dict(name="Sanju",age=29,city="Boston")

diction.update(diction2)
print(diction)

dicitonary={3:7,4:8,5:9,6:10}
print(dicitonary)
value=dicitonary[4]
print(value)

myTuple = (8,9,10)
dicitonary = {myTuple: 15}
print(dicitonary)