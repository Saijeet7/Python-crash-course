import secrets

myList = list("ABCDEFGH")
a = secrets.choice(myList)
a = secrets.randbits(4)
print(a)
