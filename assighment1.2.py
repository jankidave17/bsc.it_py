Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
>>> num =  int(input("enter a number : "))
enter a number : 40
>>> print("square root = ",math.sqrt(num))
square root =  6.324555320336759
>>> print("factorial=",math.factorial(num))
factorial= 815915283247897734345611269596115894272000000000
>>> base=int(input("enter a base: "))
enter a base: 20
>>> power=int(inpit("enter a power: "))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    power=int(inpit("enter a power: "))
NameError: name 'inpit' is not defined. Did you mean: 'input'?
>>> power=int(input("enter a power : "))
enter a power : 2
>>> result=base**power
>>> print("result=",result)
result= 400
