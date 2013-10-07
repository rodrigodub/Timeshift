PS C:\Users\rnobrega.METECH\Documents\GitHub\Timeshift\Source> python
Python 2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> li = ['00:02:51.326', '00:02:53.821']
>>> li
['00:02:51.326', '00:02:53.821']
>>> li[0]
'00:02:51.326'
>>> li[0].split(':')[0]
'00'
>>> int(li[0].split(':')[0])
0
>>> int(li[0].split(':')[1])
2
>>> int(li[0].split(':')[2])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '51.326'
>>> float(li[0].split(':')[2])
51.326
>>> int(float(li[0].split(':')[2]))
51
>>> float(li[0].split(':')[2])
51.326
>>> string(float(li[0].split(':')[2]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'string' is not defined
>>> str(float(li[0].split(':')[2]))
'51.326'
>>> float(li[0].split(':')[2])
51.326
>>> str(float(li[0].split(':')[2]))
'51.326'
>>> str(float(li[0].split(':')[2])).split('.')[1]
'326'
>>> int(str(float(li[0].split(':')[2])).split('.')[1])
326
>>> str(float(li[0].split(':')[2])).split('.')[1] + '000000'
'326000000'
>>> (str(float(li[0].split(':')[2])).split('.')[1] + '000000')[0:6]
'326000'
>>> int((str(float(li[0].split(':')[2])).split('.')[1] + '000000')[0:6])
326000
>>> ^Z