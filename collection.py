#collection: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "aaaaabbbbbbcccc"

my_collection = Counter(a)
print(my_collection)
print(list(my_collection.elements()))

Point = namedtuple('Point','x,y')
pt = Point(1,-4)
print(pt.x, pt.y)

ordered_dict = {}
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['a']=1
ordered_dict['d']=4
ordered_dict['e']=5
print(ordered_dict)

d = defaultdict(float)
d['a']=1
d['b']=2
d['c']=3
d['d']=4
print(d['a'], d['b'])

d= deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(7)
d.extend([4,5,6])
d.rotate(1)
print(d)