导入模块
```python
>>> from EasyPandas import na
>>> import numpy as np
>>> import pandas as pd
>>> df = pd.DataFrame(np.random.randn(5, 3), index=["a", "c", "e", "f", "h"], columns=["one", "two", "three"])
>>> df["four"] = "bar"
>>> df["five"] = df["one"] > 0
>>> df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```

DataFrame判断是否为缺失值
```python
>>> res = na(df2, "isna")
>>> print(res)
```

```
     one    two  three   four   five
a  False  False  False  False  False
b   True   True   True   True   True
c  False  False  False  False  False
d   True   True   True   True   True
e  False  False  False  False  False
f  False  False  False  False  False
g   True   True   True   True   True
h  False  False  False  False  False
```

Series判断是否为缺失值
```python
>>> res = na(df2["two"], "isna")
>>> print(res)
```

```
a    False
b     True
c    False
d     True
e    False
f    False
g     True
h    False
Name: two, dtype: bool
```

DataFrame判断是否不为缺失值
```python
>>> res = na(df2, "notna")
>>> print(res)
```

```
     one    two  three   four   five
a   True   True   True   True   True
b  False  False  False  False  False
c   True   True   True   True   True
d  False  False  False  False  False
e   True   True   True   True   True
f   True   True   True   True   True
g  False  False  False  False  False
h   True   True   True   True   True
```

Series判断是否不为缺失值
```python
>>> res = na(df2["two"], "notna")
>>> print(res)
```

```
a     True
b    False
c     True
d    False
e     True
f     True
g    False
h     True
Name: two, dtype: bool
```

DataFrame填充缺失值为平均数
```python
>>> res = na(df2.iloc[:, :3], "fill")
>>> print(res)
```

```
        one       two     three
a  0.906106 -0.712913 -0.117904
b -0.154371 -0.159853  0.227454
c -0.912999  2.127544 -0.159811
d -0.154371 -0.159853  0.227454
e -0.755127 -0.585021  0.569916
f  0.497324 -0.645777  0.557569
g -0.154371 -0.159853  0.227454
h -0.507161 -0.983099  0.287500
```

DataFrame填充缺失值为100
```python
>>> res = na(df2.iloc[:, :3], "fill", fillvalue=100)
>>> print(res)
```

```
          one         two       three
a    0.906106   -0.712913   -0.117904
b  100.000000  100.000000  100.000000
c   -0.912999    2.127544   -0.159811
d  100.000000  100.000000  100.000000
e   -0.755127   -0.585021    0.569916
f    0.497324   -0.645777    0.557569
g  100.000000  100.000000  100.000000
h   -0.507161   -0.983099    0.287500
```

Series填充缺失值为平均数
```python
>>> res = na(df2["two"], "fill")
>>> print(res)
```

```
a   -0.712913
b   -0.159853
c    2.127544
d   -0.159853
e   -0.585021
f   -0.645777
g   -0.159853
h   -0.983099
Name: two, dtype: float64
```

Series填充缺失值为100
```python
>>> res = na(df2["two"], "fill", fillvalue=100)
>>> print(res)
```

```
a     -0.712913
b    100.000000
c      2.127544
d    100.000000
e     -0.585021
f     -0.645777
g    100.000000
h     -0.983099
Name: two, dtype: float64
```

Series填充缺失值为foo
```python
>>> res = na(df2["four"], "fill", fillvalue="foo")
>>> print(res)
```

```
a    bar
b    foo
c    bar
d    foo
e    bar
f    bar
g    foo
h    bar
Name: four, dtype: object
```

DataFrame向前填充
```python
>>> res = na(df2, "ffill")
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
b  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
d -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
g  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

Series向前填充
```python
>>> res = na(df2, "ffill")
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
b  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
d -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
g  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

Series向前填充
```python
>>> res = na(df2["four"], "ffill")
>>> print(res)
```

```
a    bar
b    bar
c    bar
d    bar
e    bar
f    bar
g    bar
h    bar
Name: four, dtype: object
```

DataFrame向后填充
```python
>>> res = na(df2, "ffill")
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
b  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
d -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
g  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

Series向后填充
```python
>>> res = na(df2, "ffill")
>>> print(res)
```

```
       one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
b  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
d -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
g  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

Series向后填充
```python
>>> res = na(df2["four"], "ffill")
>>> print(res)
```

```
a    bar
b    bar
c    bar
d    bar
e    bar
f    bar
g    bar
h    bar
Name: four, dtype: object
```

DataFrame删除缺失值，按行删除，只要某行存在缺失值就删除，不原地删除
```python
>>> res = na(df2, "delete")
>>> print(df2)
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
b       NaN       NaN       NaN  NaN    NaN
c -0.912999  2.127544 -0.159811  bar  False
d       NaN       NaN       NaN  NaN    NaN
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
g       NaN       NaN       NaN  NaN    NaN
h -0.507161 -0.983099  0.287500  bar  False
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

DataFrame删除缺失值，按行删除，只要某行存在缺失值就删除，原地删除
```python
>>> res = na(df2, "delete", inplace=1)
>>> print(df2)
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
None
```

DataFrame删除缺失值，按行删除，某行全为缺失值才删除，不原地删除
```python
>>> res = na(df2, "delete", how="all")
>>> print(df2)
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

DataFrame删除缺失值，按行删除，某行全为缺失值才删除，原地删除
```python
>>> res = na(df2, "delete", how="all", inplace=1)
>>> print(df2)
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
None
```

DataFrame删除缺失值，按行删除，只要two列存在缺失值就删除，不原地删除
```python
>>> res = na(df2, "delete", subset="two")
>>> print(df2)
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

DataFrame删除缺失值，按行删除，two列和four列全为缺失值才删除，不原地删除
```python
>>> res = na(df2, "delete", subset=["two", "four"], how="all")
>>> print(df2)
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

DataFrame删除缺失值，按列删除，某列全为缺失值才删除，不原地删除
```python
>>> res = na(df2, "delete", how="all", bycol=1)
>>> print(df2)
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

DataFrame删除缺失值，按列删除，某列存在缺失值就删除，不原地删除
```python
>>> res = na(df2, "delete", bycol=1)
>>> print(df2)
>>> print(res)
```

```
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
        one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
```

DataFrame删除缺失值，按列删除，某列存在缺失值就删除，原地删除
```python
>>> res = na(df2, "delete", bycol=1, inplace=1)
>>> print(df2)
>>> print(res)
```

```
       one       two     three four   five
a  0.906106 -0.712913 -0.117904  bar   True
c -0.912999  2.127544 -0.159811  bar  False
e -0.755127 -0.585021  0.569916  bar  False
f  0.497324 -0.645777  0.557569  bar   True
h -0.507161 -0.983099  0.287500  bar  False
None
```

Series删除缺失值，存在缺失值就删除，不原地删除
```python
>>> res = na(df2["two"], "delete")
>>> print(df2["two"])
>>> print(res)
```

```
a   -0.712913
c    2.127544
e   -0.585021
f   -0.645777
h   -0.983099
Name: two, dtype: float64
a   -0.712913
c    2.127544
e   -0.585021
f   -0.645777
h   -0.983099
Name: two, dtype: float64
```

Series删除缺失值，全为缺失值才删除，不原地删除（Series只能按照上面的方式删除，这种方法是无法删除的）
```python
>>> res = na(df2["two"], "delete", how="all")
>>> print(df2["two"])
>>> print(res)
```

```
a   -0.712913
c    2.127544
e   -0.585021
f   -0.645777
h   -0.983099
Name: two, dtype: float64
a   -0.712913
c    2.127544
e   -0.585021
f   -0.645777
h   -0.983099
Name: two, dtype: float64
```

Series删除缺失值，存在缺失值就删除，原地删除（DataFrame的列是视图，无法原地删除）
```python
>>> res = na(df2["two"], "delete", inplace=1)
>>> print(df2["two"])
>>> print(res)
```

```
a   -0.712913
c    2.127544
e   -0.585021
f   -0.645777
h   -0.983099
Name: two, dtype: float64
None
```

Series删除缺失值，存在缺失值就删除，原地删除（DataFrame的列是视图，无法原地删除，先复制才能）
```python
>>> s = df2["two"].copy()
>>> res = na(s, "delete", inplace=1)
>>> print(s)
>>> print(res)
```

```
a   -0.712913
c    2.127544
e   -0.585021
f   -0.645777
h   -0.983099
Name: two, dtype: float64
None
```
