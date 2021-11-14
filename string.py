#Strings: ordered, immutable, text representation
greeting = "Hello"
name="Tom"
sentence = greeting +" "+name
print(sentence)

for i in greeting:
    print(i)

if 'e' in greeting:
    print('Yes')
else:
    print('No')

my_string = '   Hello World     '
my_string = my_string.strip()
print(my_string)

print(my_string.upper())
print(my_string.lower())

print(my_string.endswith('World'))

print(my_string.find('o'))
print(my_string.count('o'))

print(my_string.replace('World','Universe'))

m_string = 'How you doin?'
m_string = m_string.split(" ")
print(m_string)

new_string = ' '.join(m_string)
print(new_string)

my_list_2 =['a']*1000000

from timeit import default_timer as timer
start = timer()
my_string = ''

#Bad
for i in my_list_2:
    my_string +=i
stop = timer()
print(stop-start)

#Good
start = timer()
my_string = ''.join(my_list_2)
stop= timer()
print(stop-start)

# %, .format(), f-Strings
var = 3.123412
var2=6
my_string = f"the varaible is {var*2} and {var2}"
print(my_string)