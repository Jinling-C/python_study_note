a=100+200+300
print(a)

#2018.7.17字符串和编码
ord('a')
#97
ord('A')
#65
ord('中')
#20013
ord('文')
#25991
chr(20013)
#'中'

'abc'.encode('ascii')
#b'abc'
b'abc'.decode('ascii')
#'abc'
'中文'.encode('utf-8')
#b'\xe4\xb8\xad\xe6\x96\x87'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#'中文'

len('abc')
#3
len('中文')
#2
len('中文'.encode('utf-8'))
#6

print('%2d-%02d' % (3, 1))
# 3-01
print('%.2f' % 3.1415926)
#3.14
'age:%s  gender:%s'%(29,'female')
#'age:29  gender:female'
'%s的成绩提高了%.1f'%('小明',(85-72)/72)
#'小明的成绩提高了0.2'
'{0}的成绩提高了{1:.1}'.format('小明',(85-72)/72)
#'小明的成绩提高了0.2'
print('{0}的成绩提高了{1:.2}'.format('小明',(85-72)/72))
#'小明的成绩提高了0.18'
print('{0}的成绩提高了{1:.2%}'.format('小明',(85-72)/72))
#小明的成绩提高了18.06%
print('{0}的成绩提高了{1:.2}%'.format('小明',(85-72)/72*100))
#小明的成绩提高了1.8e+01%
print('{0}的成绩提高了{1:.2f}%'.format('小明',(85-72)/72*100))
#小明的成绩提高了18.06%

# -*- coding: utf-8 -*-
# list
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])

#tuple unchangeable
>>>classmates = ('Michael', 'Bob', 'Tracy')
>>>print(classmates[0])
Michael
>>> t = (1,)   #tuple with just 1 element
>>> t
(1,)



#loop
>>> height = 1.75
>>> weight = 80.5
>>> bmi=height/weight
>>> if bmi<18.5:
...     print('过轻')
... elif bmi<25:
...     print('正常')
... elif bmi<28:
...     print('过重')
... else:
...     print('肥胖')
...


>>> names = ['Michael', 'Bob', 'Tracy']
>>> for name in names:
...     print(name)
...
Michael
Bob
Tracy


>>> sum=0
>>> for x in range(6):
...   sum=sum+x
...   print(sum)
...
0
1
3
6
10
15

>>> sum=0
>>> for x in range(6):
...   sum=sum+x
...
>>> print(sum)
15


>>> list(range(6))
[0, 1, 2, 3, 4, 5]


>>> sum=0
>>> n=99
>>> while n>0:
...     sum=sum+n
...     n=n-2
...
>>> print(sum)
2500


# -*- coding: utf-8 -*-
 L = ['Bart', 'Lisa', 'Adam']
>>> for x in L:
...    print(x)
...
Bart
Lisa
Adam

>>> n=len(L)
>>> while n>0:
...   print(L[len(L)-n])
...   n=n-1
...
Bart
Lisa
Adam


>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95

>>> d['Adam'] = 67
>>> d['Adam']
67

>>> 'Thomas' in d
False

>>> d.get('Thomas', -1)
-1

>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
>>> d['Thomas']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Thomas'

>>> d['Adam'] = 67
>>> d['Adam']
67

>>> d['Jack'] = 90
>>> d['Jack']
90
>>> d['Jack'] = 88
>>> d['Jack']
88

>>> 'Thomas' in d
False
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
>>> d.get('Bob')
75

>>> d.pop('Bob')
75
>>> d
{'Michael': 95, 'Tracy': 85}


>>> s=set([1,2,3])
>>> s
{1, 2, 3}
>>> s=set([1,1,2,2,3])
>>> s
{1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.remove(4)
>>> s
{1, 2, 3}
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1&s2
{2, 3}
>>> s1|s2
{1, 2, 3, 4}

>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']

>>> a = ['c', 'b', 'a']  #list is changeable
>>> a.sort()
>>> a
['a', 'b', 'c']
>>>
>>> a = 'abc'   #str is unchangeable
>>> a.replace('a', 'A')
'Abc'
>>> a
'abc'


>>> abs(-100)
100
>>> max(1,2)
2
>>> min(1,2)
1


>>> int('123')
123
>>> str(123)
'123'
>>> float('12.34')
12.34
>>> bool(1)
True
>>> bool(0)
False
>>> bool(False)
False

>>> a = abs  #变量a指向abs函数
>>> a(-1)
1
>>> a=max
>>> a(1,2,3)
3
>>> n1 = 255
>>> print(hex(n1))
0xff
>>> n2 = 1000
>>> print(hex(n2))
0x3e8
>>> n1 =0xff
>>> print(int(n1))
255

>>> def my_abs(x):
...   if x>0:
...      return x
...   else:
...      return -x
...
>>> print(my_abs(-10))
10

#默认参数
>>> def my_power(x=1,n=2):  #设置默认参数时，有几点要注意：一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；二是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
...     s=1
...     while n>0:
...        s=s*x
...        n=n-1
...     return s
...
>>> print(my_power())
1
>>> print(my_power(2))
4


>>> def enroll(name, gender, age=6, city='Beijing'):
...    print('name:', name)
...    print('gender:', gender)
...    print('age:', age)
...    print('city:', city)
...
>>> enroll('Sarah', 'F')
name: Sarah
gender: F
age: 6
city: Beijing
>>> enroll('Bob', 'M', 7)
name: Bob
gender: M
age: 7
city: Beijing
>>> enroll('Adam', 'M', city='Tianjin')
name: Adam
gender: M
age: 6
city: Tianjin



def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
>>> add_end()
['END']
>>> add_end()
['END']

def calc(numbers):   #参数为一个list或tuple
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

>>> calc([1,2,3])
14
>>> calc((1,2,3,4,5,6,7))
140

#可变参数
>>> def calc(*numbers):   #*numbers 可变参数
...    sum=0
...    for n in numbers:
...       sum=sum+n*n
...    return sum
...
>>> calc(1,2,3)
14

#关键字参数
>>> def person(name, age, **kw):
...     print('name:', name, 'age:', age, 'other:', kw)
...
>>> person('Michael', 30)
name: Michael age: 30 other: {}
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}


#2018.11.5 Advance properties
>>> list=[]
>>> n=1
>>> while n<15:
...   list.append(n)
...   n=n+2
...
>>> print(list)
[1, 3, 5, 7, 9, 11, 13]
>>>

>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
>>> [L[0], L[1], L[2]]
['Michael', 'Sarah', 'Tracy']
>>> r=[]
>>> n=3
>>> for i in range(n):
...   r.append(L[i])
...
...
>>> r
['Michael', 'Sarah', 'Tracy']
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
>>> L[1:3]
['Sarah', 'Tracy']
>>> L[-1]
'Jack'