Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("iftekhar")
iftekhar
>>> a=20
>>> b=100
>>> print(a+b)
120
>>> 
120
120
>>> a=[1,2,4,8,-3,4,8,'b']
>>> a.append(5)
>>> print(a)
[1, 2, 4, 8, -3, 4, 8, 'b', 5]
>>> a.append('5')
>>> a
[1, 2, 4, 8, -3, 4, 8, 'b', 5, '5']
>>> b=[1,2,3]
>>> a.extend(['a','b','c'])
>>> a
[1, 2, 4, 8, -3, 4, 8, 'b', 5, '5', 'a', 'b', 'c']
>>> a.extend(b)
>>> a
[1, 2, 4, 8, -3, 4, 8, 'b', 5, '5', 'a', 'b', 'c', 1, 2, 3]
>>> a=['1',4,5]
>>> b=[7,8,9]
>>> a+b
['1', 4, 5, 7, 8, 9]
>>> a.index(8)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.index(8)
ValueError: 8 is not in list
>>> a.index(5)
2
>>> a="python programming"
>>> a[0:5]
'pytho'
>>> print(a.lower())
python programming
>>> print(a.upper())
PYTHON PROGRAMMING
>>> a=["cmr',"good","college"]
   
SyntaxError: invalid syntax
>>> a=["cmr","good","college"]
>>> a.insert(1,"is"]
SyntaxError: invalid syntax
>>> a.insert(1,"is")
>>> a
['cmr', 'is', 'good', 'college']
>>> print(string.replace("college", "university", 3))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(string.replace("college", "university", 3))
NameError: name 'string' is not defined
>>> print(a.replace("college", "university", 3))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(a.replace("college", "university", 3))
AttributeError: 'list' object has no attribute 'replace'
>>> a.pop(3)
'college'
>>> a
['cmr', 'is', 'good']
>>> a.insert(3,"university")
>>> a
['cmr', 'is', 'good', 'university']
>>> a.reverse()
>>> a
['university', 'good', 'is', 'cmr']
>>> a.count(o)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.count(o)
NameError: name 'o' is not defined
>>> a.count(2)
0
>>> a=(1,2,3,"a")
>>> a*2
(1, 2, 3, 'a', 1, 2, 3, 'a')
>>> 
