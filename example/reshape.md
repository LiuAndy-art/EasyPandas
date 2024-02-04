导入模块
```python
>>> import pandas as pd
>>> from EasyPandas import reshape
>>> df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'], 'bar': ['A', 'B', 'C', 'A', 'B', 'C'], 'baz': [1, 2, 3, 4, 5, 6], 'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
```

测试l2w
```python
>>> print(df)
>>> res = reshape(df, "l2w", index='foo', columns='bar', values='baz')
>>> print(res)
```

```
   foo bar  baz zoo
0  one   A    1   x
1  one   B    2   y
2  one   C    3   z
3  two   A    4   q
4  two   B    5   w
5  two   C    6   t
bar  A  B  C
foo         
one  1  2  3
two  4  5  6
```

测试w2l
```python
>>> res = reshape(df, "l2w", index='foo', columns='bar', values='baz')
>>> print(res)
>>> res = reshape(res, "w2l", groups={"baz": ["A", "B", "C"]})
>>> print(res)
```

```
bar  A  B  C
foo         
one  1  2  3
two  4  5  6
   baz
0    1
1    4
2    2
3    5
4    3
5    6
```
