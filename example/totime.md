导入模块
```python
>>> import pandas as pd
>>> from EasyPandas import totime
```

基本测试
```python
>>> timestr = "Jul 31, 2009"
>>> res = totime(timestr)
>>> print(res)
```

```
2009-07-31 00:00:00
```

基本测试
```python
>>> timestr = "2005/11/23"
>>> res = totime(timestr)
>>> print(res)
```

```
2005-11-23 00:00:00
```

基本测试
```python
>>> timestr = None
>>> res = totime(timestr)
>>> print(res)
```

```
None
```

基本测试
```python
>>> timestr = "04-14-2012 10:00"
>>> res = totime(timestr)
>>> print(res)
```

```
2012-04-14 10:00:00
```

基本测试
```python
>>> timestr = "2018-01-01"
>>> res = totime(timestr)
>>> print(res)
```

```
2018-01-01 00:00:00
```

基本测试，定制格式
```python
>>> timestr = "2018*01||01"
>>> res = totime(timestr, format="%Y*%m||%d")
>>> print(res)
```

```
2018-01-01 00:00:00
```

基本测试，将数字转为时间
```python
>>> timestr = [2018, 2020, 10000]
>>> res = totime(timestr, unit="D")
>>> print(res)
```

```
DatetimeIndex(['1975-07-12', '1975-07-14', '1997-05-19'], dtype='datetime64[ns]', freq=None)
```

基本测试，将数字转为时间，给定原始时间
```python
>>> timestr = [2018, 2020, 10000]
>>> res = totime(timestr, unit="D", origin="2000-01-01")
>>> print(res)
```

```
DatetimeIndex(['2005-07-11', '2005-07-13', '2027-05-19'], dtype='datetime64[ns]', freq=None)
```
