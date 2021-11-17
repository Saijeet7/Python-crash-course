#error and exceptions
# x= -5
# if x<0:
#     raise Exception('x should be positive')
# else:
#     print(x)

# assert (x>=0), 'X is not positive'

# try:
#     a=5/0
#     b = a+ 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('Everything is fine')
# finally:
#     print('Cleaning up...')

class ValueTooHighError(Exception):
    pass

class ValueTooShortError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError('value too high')
    if x<5:
        raise ValueTooShortError('value too small',x)
try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooShortError as e:
    print(e.message,e.value)