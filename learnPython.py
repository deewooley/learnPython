print("Hello, I am now Learning Python!")
if 5 > 2:
     print("Five is greater than two!") 
x = 5
y = "Hello, World!"
# for comments
"""
multiline
comments
"""
print(x)
print(y)


d, e, w = "Orange", "Banana", "Cherry"

print(d)
print(e)
print(w)


x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

def myfunc2():
      global r
r = "fantastic"

myfunc2()

print("Python is " + r)

#Get Data Type
x = 5
print(type(x))

"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	


Specifying the Data Type
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview

NEXT Python Numbers W3

Operators Remember:

**Exponentation
//Floor Division

Logical Operators = and, or, not
Identity Operators= is(x is y), is not(x is not y)
Membership operators = in(ret True if value is present in the object), not it(ret true if a seq w a spec value is not present in the object)
Bitwise Operators = &, |, ^(XOR - 	Sets each bit to 1 if only one of two bits is 1), ~(NOT), <<(Zero fill left shift), >>(Zero fill right shift)
_______________
(12 >> 1) - 1)         
>> shifts binary 12(1100) 1 times to the right.
12 >> 1 == 6(110)

6 - 1 == 5


Continue with python lists
"""