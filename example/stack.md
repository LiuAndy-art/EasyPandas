导入模块
```python
>>> import numpy as np
>>> import pandas as pd
>>> from EasyPandas import stack
```

测试stack参数
```python
>>> df_single_level_cols = pd.DataFrame([[0, 1], [2, 3]], index=['cat', 'dog'], columns=['weight', 'height'])
>>> print(df_single_level_cols)
>>> res = stack(df_single_level_cols)
>>> print(res)
```

```
     weight  height
cat       0       1
dog       2       3
cat  weight    0
     height    1
dog  weight    2
     height    3
dtype: int64
```

测试unstack参数
```python
>>> index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'), ('two', 'a'), ('two', 'b')])
>>> s = pd.Series(np.arange(1.0, 5.0), index=index)
>>> print(s)
>>> res = stack(s, isstack=0)
>>> print(res)
```

```
one  a    1.0
     b    2.0
two  a    3.0
     b    4.0
dtype: float64
       a    b
one  1.0  2.0
two  3.0  4.0
```

测试unstack参数，指定level
```python
>>> index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'), ('two', 'a'), ('two', 'b')])
>>> s = pd.Series(np.arange(1.0, 5.0), index=index)
>>> print(s)
>>> res = stack(s, isstack=0, level=0)
>>> print(res)
```

```
one  a    1.0
     b    2.0
two  a    3.0
     b    4.0
dtype: float64
   one  two
a  1.0  3.0
b  2.0  4.0
```
