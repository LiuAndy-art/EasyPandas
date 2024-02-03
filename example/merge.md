导入模块
```python
>>> import pandas as pd
>>> from EasyPandas import merge
>>> df1 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'], 'value_1': [1, 2, 3, 5]})
>>> df2 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'], 'value_2': [5, 6, 7, 8]})
```

测试按照变量合并，inner合并
```python
>>> print(df1)
>>> print(df2)
>>> res = merge([df1, df2], isbyvar=1, on="key", how="inner")
>>> print(res)
```

```
   key  value_1
0  foo        1
1  bar        2
2  baz        3
3  foo        5
   key  value_2
0  foo        5
1  bar        6
2  baz        7
3  foo        8
   key  value_1  value_2
0  foo        1        5
1  foo        1        8
2  bar        2        6
3  baz        3        7
4  foo        5        5
5  foo        5        8
```

测试按照变量合并，outer合并
```python
>>> print(df1)
>>> print(df2)
>>> res = merge([df1, df2], isbyvar=1, on="key", how="outer")
>>> print(res)
```

```
   key  value_1
0  foo        1
1  bar        2
2  baz        3
3  foo        5
   key  value_2
0  foo        5
1  bar        6
2  baz        7
3  foo        8
   key  value_1  value_2
0  bar        2        6
1  baz        3        7
2  foo        1        5
3  foo        1        8
4  foo        5        5
5  foo        5        8
```

测试按照变量合并，left合并
```python
>>> print(df1)
>>> print(df2)
>>> res = merge([df1, df2], isbyvar=1, on="key", how="left")
>>> print(res)
```

```
   key  value_1
0  foo        1
1  bar        2
2  baz        3
3  foo        5
   key  value_2
0  foo        5
1  bar        6
2  baz        7
3  foo        8
   key  value_1  value_2
0  foo        1        5
1  foo        1        8
2  bar        2        6
3  baz        3        7
4  foo        5        5
5  foo        5        8
```

测试普通合并，按行合并
```python
>>> print(df1)
>>> print(df2)
>>> res = merge([df1, df2])
>>> print(res)
```

```
   key  value_1
0  foo        1
1  bar        2
2  baz        3
3  foo        5
   key  value_2
0  foo        5
1  bar        6
2  baz        7
3  foo        8
   key
0  foo
1  bar
2  baz
3  foo
0  foo
1  bar
2  baz
3  foo
```

测试普通合并，按列合并
```python
>>> print(df1)
>>> print(df2)
>>> res = merge([df1, df2], axis=1)
>>> print(res)
```

```
  key  value_1
0  foo        1
1  bar        2
2  baz        3
3  foo        5
   key  value_2
0  foo        5
1  bar        6
2  baz        7
3  foo        8
   key  value_1  key  value_2
0  foo        1  foo        5
1  bar        2  bar        6
2  baz        3  baz        7
3  foo        5  foo        8
```

测试普通合并，按列合并，重新排列索引
```python
>>> print(df1)
>>> print(df2)
>>> res = merge([df1, df2], axis=1, ignore_index=1)
>>> print(res)
```

```
   key  value_1
0  foo        1
1  bar        2
2  baz        3
3  foo        5
   key  value_2
0  foo        5
1  bar        6
2  baz        7
3  foo        8
     0  1    2  3
0  foo  1  foo  5
1  bar  2  bar  6
2  baz  3  baz  7
3  foo  5  foo  8
```

测试普通合并，按行合并，设置多重索引
```python
>>> print(df1)
>>> print(df2)
>>> res = merge([df1, df2], axis=0, keys=["left", "right"])
>>> print(res)
```

```
   key  value_1
0  foo        1
1  bar        2
2  baz        3
3  foo        5
   key  value_2
0  foo        5
1  bar        6
2  baz        7
3  foo        8
         key
left  0  foo
      1  bar
      2  baz
      3  foo
right 0  foo
      1  bar
      2  baz
      3  foo
```

测试普通合并，按行合并，outer合并
```python
>>> print(df1)
>>> print(df2)
>>> res = merge([df1, df2], axis=0, keys=["left", "right"], join="outer")
>>> print(res)
```

```
   key  value_1
0  foo        1
1  bar        2
2  baz        3
3  foo        5
   key  value_2
0  foo        5
1  bar        6
2  baz        7
3  foo        8
         key  value_1  value_2
left  0  foo      1.0      NaN
      1  bar      2.0      NaN
      2  baz      3.0      NaN
      3  foo      5.0      NaN
right 0  foo      NaN      5.0
      1  bar      NaN      6.0
      2  baz      NaN      7.0
      3  foo      NaN      8.0
```
