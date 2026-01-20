Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
year=int(input("ENTER A YEAR : "))
ENTER A YEAR : 2007
>>> if(year%400==0)or(year%4==0 and year%100 !=0):
...     print("leap year")
... else:
...     print(" not a leap year")
... 
...     
 not a leap year
>>> import math
>>> print("value of PI = ",math.pi)
value of PI =  3.141592653589793
>>> PI=3.14
>>> print("constant value of PI = 3.14")
constant value of PI = 3.14
>>> num=int(input("ENTER A NUMBER : "))
ENTER A NUMBER : 24
>>> if num>0:
...     print("POSITIVE NUMBER")
... elif num<0:
...     print("NEGATIVE NUMBER")
... else:
...     print("zero")
... 
...     
POSITIVE NUMBER
