Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2.1      
>>> tempo="00:04:33,571 --> 00:04:36,244"
>>> print tempo
00:04:33,571 --> 00:04:36,244
>>> tempo.find("-->")
13
>>> tempo.rsplit(" --> ")
['00:04:33,571', '00:04:36,244']
>>> inifim=tempo.rsplit(" --> ")
>>> inifim
['00:04:33,571', '00:04:36,244']
>>> inifim[1]
'00:04:36,244'
>>> inifim[0]
'00:04:33,571'
>>> inifim[0].split(":")
['00', '04', '33,571']
>>>  inifim[0].split(":")[0]
 
  File "<pyshell#9>", line 1
    inifim[0].split(":")[0]
   ^
IndentationError: unexpected indent
>>> listinicio= inifim[0].split(":")
>>> listfim= inifim[1].split(":")
>>> listinicio
['00', '04', '33,571']
>>> listfim
['00', '04', '36,244']
>>> 
listinicio[0]
'00'
>>> listinicio[1]
'04'
>>> listinicio[2]
'33,571'
>>> tempo.find("abc")
-1
>>> 
>>> dif=3.5
>>> dif
3.5
>>> listinicio[2]
'33,571'
>>> listinicio[2]+dif

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    listinicio[2]+dif
TypeError: cannot concatenate 'str' and 'float' objects
>>> listinicio[2].replace(",",".")
'33.571'
>>> seg=listinicio[2].replace(",",".")
>>> seg+dif

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    seg+dif
TypeError: cannot concatenate 'str' and 'float' objects
>>> seg.float

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    seg.float
AttributeError: 'str' object has no attribute 'float'
>>> seg.
SyntaxError: invalid syntax
>>> seg.real

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    seg.real
AttributeError: 'str' object has no attribute 'real'
>>> float(seg)
33.570999999999998
>>> seg
'33.571'
>>> float(seg)
33.570999999999998
>>> float(seg)+dif
37.070999999999998
>>> dif
3.5
>>> round(float(seg)+dif,3)
37.070999999999998
>>> abs(float(seg)+dif)
37.070999999999998
>>> fix(float(seg)+dif,3)

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    fix(float(seg)+dif,3)
NameError: name 'fix' is not defined
>>> str(float(seg)+dif)
'37.071'
>>> 
