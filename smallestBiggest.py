largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
      fval= int(num)
    except ValueError:
        print('Invalid input')
        continue
    if smallest is None and largest is None:
        smallest=fval
        largest=fval
    elif fval<smallest:
        smallest=fval
        print('smallest ',smallest)
    elif largest<fval:
        largest=fval
        print('largest  ',largest)
print("Maximum is ", largest)
print("Minimum is ", smallest)