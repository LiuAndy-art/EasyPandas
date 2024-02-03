导入模块
```python
>>> from EasyPandas import dummy
```

测试还原哑变量
```python
>>> df = pd.DataFrame({"a": [1, 0, 0, 1], "b": [0, 1, 0, 0], "c": [0, 0, 1, 0]})
>>> print(df)
>>> res = dummy(df, getorfromdummy=0)
>>> print(res)
```

```
   a  b  c
0  1  0  0
1  0  1  0
2  0  0  1
3  1  0  0
    
0  a
1  b
2  c
3  a
```

```python
>>> df = pd.DataFrame({"col1_a": [1, 0, 1], "col1_b": [0, 1, 0], "col2_a": [0, 1, 0], "col2_b": [1, 0, 0], "col2_c": [0, 0, 1]})
>>> print(df)
>>> res = dummy(df, getorfromdummy=0, sep="_")
>>> print(res)
```

```
   col1_a  col1_b  col2_a  col2_b  col2_c
0       1       0       0       1       0
1       0       1       1       0       0
2       1       0       0       0       1
  col1 col2
0    a    b
1    b    a
2    a    c
```

测试变量虚拟化，给定前缀
```python
>>> s = pd.Series(list('abca'))
>>> print(s)
>>> res = dummy(s, prefix="AA")
>>> print(res)
```

```
0    a
1    b
2    c
3    a
dtype: object
    AA_a   AA_b   AA_c
0   True  False  False
1  False   True  False
2  False  False   True
3   True  False  False
```

测试变量虚拟化，给定前缀，给定分隔符
```python
>>> s = pd.Series(list('abca'))
>>> print(s)
>>> res = dummy(s, prefix="AA", prefix_sep="+")
>>> print(res)
```

```
0    a
1    b
2    c
3    a
dtype: object
    AA+a   AA+b   AA+c
0   True  False  False
1  False   True  False
2  False  False   True
3   True  False  False
```
