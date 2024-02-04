导入模块
```python
>>> from EasyPandas import read, strdesc
>>> auto = read("../data/auto.dta")
```

DataFrame的测试
```python
>>> res = strdesc(auto[["make", "foreign"]], isprint=1)
```

```
               make  foreign
count            74       74
duplicate_num     0       72
unique_num       74        2
na_num            0        0
max_freq          1       52
min_freq          1       22
```

Series的测试
```python
>>> res = strdesc(auto["foreign"], isprint=1)
```

```
count            74
duplicate_num    72
unique_num        2
na_num            0
max_freq         52
min_freq         22
Name: foreign, dtype: int64
```
