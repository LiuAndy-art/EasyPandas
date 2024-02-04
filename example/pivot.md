导入模块
```python
>>> import pandas as pd
>>> from EasyPandas import pivot
>>> df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo", "bar", "bar", "bar", "bar"], "B": ["one", "one", "one", "two", "two", "one", "one", "two", "two"], "C": ["small", "large", "large", "small", "small", "large", "small", "small", "large"], "D": [1, 2, 2, 3, 3, 4, 5, 6, 7], "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
```

给定index, columns和values，单个聚合函数
```python
>>> print(df)
>>> res = pivot(df, values='D', index=['A', 'B'], columns=['C'], aggfunc="sum")
>>> print(res)
```

```
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9
C        large  small
A   B                
bar one    4.0    5.0
    two    7.0    6.0
foo one    4.0    1.0
    two    NaN    6.0
```

给定index, 和values，多个聚合函数
```python
>>> print(df)
>>> res = pivot(df, values=['D', 'E'], index=['A', 'C'], aggfunc={'D': "mean", 'E': "mean"})
>>> print(res)
```

```
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9
                  D         E
A   C                        
bar large  5.500000  7.500000
    small  5.500000  8.500000
foo large  2.000000  4.500000
    small  2.333333  4.333333
```

不同的列给定不同的聚合函数
```python
>>> print(df)
>>> res = pivot(df, values=['D', 'E'], index=['A', 'C'], aggfunc={'D': "mean", 'E': ["min", "max", "mean"]})
>>> print(res)
```

```
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9
                  D   E              
               mean max      mean min
A   C                                
bar large  5.500000   9  7.500000   6
    small  5.500000   9  8.500000   8
foo large  2.000000   5  4.500000   4
    small  2.333333   6  4.333333   2
```

添加边际统计量
```python
>>> print(df)
>>> res = pivot(df, values=['D', 'E'], index=['A', 'C'], aggfunc="var", margin=1)
>>> print(res)
```

```
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9
                  D         E
A   C                        
bar large  4.500000  4.500000
    small  0.500000  0.500000
foo large  0.000000  0.500000
    small  1.333333  4.333333
All        4.000000  5.500000
```

添加边际统计量，给定名称
```python
>>> print(df)
>>> res = pivot(df, values=['D', 'E'], index=['A', 'C'], aggfunc="var", margin=1, margin_name="方差")
>>> print(res)
```

```
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9
                  D         E
A   C                        
bar large  4.500000  4.500000
    small  0.500000  0.500000
foo large  0.000000  0.500000
    small  1.333333  4.333333
方差         4.000000  5.500000
```
