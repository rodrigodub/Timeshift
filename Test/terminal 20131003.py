Last login: Thu Oct  3 20:56:28 on ttys000
coltrane:~ Rodrigo$ python
Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import datetime
>>> linestring = '00:00:14,455 --> 00:00:15,886'
>>> linelist = linestring.split(' --> ')
>>> linelist
['00:00:14,455', '00:00:15,886']
>>> linelistright = linelist.replace(',','.')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'replace'
>>> linestringright = linestring.replace(',','.')
>>> linelist = linestringright.split(' --> ')
>>> linelist
['00:00:14.455', '00:00:15.886']
>>> linelist[1]
'00:00:15.886'
>>> linelist[0]
'00:00:14.455'
>>> 

























