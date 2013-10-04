Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\rnobrega.METECH> python
Python 2.7.5 (default, May 15 2013, 22:44:16) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import datetime
>>> linestring = '00:00:14,455 --> 00:00:15,886'.replace(',','.')
>>> linelist = linestring.split(' --> ')
>>> linelist
['00:00:14.455', '00:00:15.886']
>>> print linelist
['00:00:14.455', '00:00:15.886']
>>> print datetime.time
<type 'datetime.time'>
>>> print datetime.time.now()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'datetime.time' has no attribute 'now'
>>> linelist[0] + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
>>>
>>>
>>> print datetime.time()
00:00:00
>>> print linelist[0].datetime.time()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'datetime'
>>> print datetime.strptime(linelist[0],%H:%M:%S)
  File "<stdin>", line 1
    print datetime.strptime(linelist[0],%H:%M:%S)
                                        ^
SyntaxError: invalid syntax
>>> print datetime.strptime(linelist[0],'%H:%M:%S')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'strptime'
>>> datetime.strptime(linelist[0],'%H:%M:%S')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'strptime'
>>> import time
>>> time.strptime(linelist[0],'%H:%M:%S')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\_strptime.py", line 467, in _strptime_time
    return _strptime(data_string, format)[0]
  File "C:\Python27\lib\_strptime.py", line 328, in _strptime
    data_string[found.end():])
ValueError: unconverted data remains: .455
>>> time.strptime(linelist[0],'%H %M %S')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\_strptime.py", line 467, in _strptime_time
    return _strptime(data_string, format)[0]
  File "C:\Python27\lib\_strptime.py", line 325, in _strptime
    (data_string, format))
ValueError: time data '00:00:14.455' does not match format '%H %M %S'
>>>
>>>
>>>
>>> time.strptime(linelist[0],'%H:%M:%S.')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\_strptime.py", line 467, in _strptime_time
    return _strptime(data_string, format)[0]
  File "C:\Python27\lib\_strptime.py", line 328, in _strptime
    data_string[found.end():])
ValueError: unconverted data remains: 455
>>> time.strptime(linelist[0],"%H:%M:%S")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\_strptime.py", line 467, in _strptime_time
    return _strptime(data_string, format)[0]
  File "C:\Python27\lib\_strptime.py", line 328, in _strptime
    data_string[found.end():])
ValueError: unconverted data remains: .455
>>> linelist[0]
'00:00:14.455'
>>> time.strptime(linelist[0],"%H:%M:%S.%f")
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=14, tm_wday=0, tm_yday=1, tm_isdst=-1)
>>> time.strptime(linelist[0],"%H:%M:%S%f")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\_strptime.py", line 467, in _strptime_time
    return _strptime(data_string, format)[0]
  File "C:\Python27\lib\_strptime.py", line 328, in _strptime
    data_string[found.end():])
ValueError: unconverted data remains: .455
>>> time.strptime(linelist[0],"%H:%M:%f")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python27\lib\_strptime.py", line 467, in _strptime_time
    return _strptime(data_string, format)[0]
  File "C:\Python27\lib\_strptime.py", line 328, in _strptime
    data_string[found.end():])
ValueError: unconverted data remains: .455
>>> time.strptime(linelist[0],"%H:%M:%S.%f")
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=14, tm_wday=0, tm_yday=1, tm_isdst=-1)
>>>
>>>
>>>  linestring = '00:14:03,635 --> 00:14:05,537'.replace(',','.')
  File "<stdin>", line 1
    linestring = '00:14:03,635 --> 00:14:05,537'.replace(',','.')
    ^
IndentationError: unexpected indent
>>>
>>> linestring = '00:14:03,635 --> 00:14:05,537'.replace(',','.')
>>> linelist = linestring.split(' --> ')
>>> linelist
['00:14:03.635', '00:14:05.537']
>>> time.strptime(linelist[0],"%H:%M:%S.%f")
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=14, tm_sec=3, tm_wday=0, tm_yday=1, tm_isdst=-1)
>>> print time.strptime(linelist[0],"%H:%M:%S.%f")
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=14, tm_sec=3, tm_wday=0, tm_yday=1, tm_isdst=-1)
>>> linestring = '00:14:03,635 --> 00:14:05,537'.replace(',','.000')
>>> linelist = linestring.split(' --> ')
>>> linelist
['00:14:03.000635', '00:14:05.000537']
>>> print time.strptime(linelist[0],"%H:%M:%S.%f")
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=14, tm_sec=3, tm_wday=0, tm_yday=1, tm_isdst=-1)
>>>