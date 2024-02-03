导入模块
```python
>>> from EasyPandas import read, cut
>>> iris = read("../data/iris.xlsx")
>>> sepal_length = iris["Sepal.Length"]
```

变量等距分组
```python
>>> res = cut(sepal_length, bins=5)
>>> print(res)
```

```
0       (5.02, 5.74]
1      (4.296, 5.02]
2      (4.296, 5.02]
3      (4.296, 5.02]
4      (4.296, 5.02]
           ...      
145     (6.46, 7.18]
146     (5.74, 6.46]
147     (6.46, 7.18]
148     (5.74, 6.46]
149     (5.74, 6.46]
Name: Sepal.Length, Length: 150, dtype: category
Categories (5, interval[float64, right]): [(4.296, 5.02] < (5.02, 5.74] < (5.74, 6.46] < (6.46, 7.18] < (7.18, 7.9]]
```

变量不等距分组
```python
>>> res = cut(sepal_length, bins=[4, 5.5, 6.5, 7, 8])
>>> print(res)
```

```
0      (4.0, 5.5]
1      (4.0, 5.5]
2      (4.0, 5.5]
3      (4.0, 5.5]
4      (4.0, 5.5]
          ...    
145    (6.5, 7.0]
146    (5.5, 6.5]
147    (5.5, 6.5]
148    (5.5, 6.5]
149    (5.5, 6.5]
Name: Sepal.Length, Length: 150, dtype: category
Categories (4, interval[float64, right]): [(4.0, 5.5] < (5.5, 6.5] < (6.5, 7.0] < (7.0, 8.0]]
```

变量不等距分组，给定标签
```python
>>> res = cut(sepal_length, bins=[4, 6.5, 7.5, 8], labels=["低", "中", "高"])
>>> print(res)
```

```
0      低
1      低
2      低
3      低
4      低
      ..
145    中
146    低
147    低
148    低
149    低
Name: Sepal.Length, Length: 150, dtype: category
Categories (3, object): ['低' < '中' < '高']
```

变量不等距分组，给定标签，不包括右边
```python
>>> res = cut(sepal_length, bins=[4, 6.5, 7.5, 8], right=0)
>>> print(res)
```

```
0      [4.0, 6.5)
1      [4.0, 6.5)
2      [4.0, 6.5)
3      [4.0, 6.5)
4      [4.0, 6.5)
          ...    
145    [6.5, 7.5)
146    [4.0, 6.5)
147    [6.5, 7.5)
148    [4.0, 6.5)
149    [4.0, 6.5)
Name: Sepal.Length, Length: 150, dtype: category
Categories (3, interval[float64, left]): [[4.0, 6.5) < [6.5, 7.5) < [7.5, 8.0)]
```

变量不等距分组，给定标签，第一个区间包括左边端点
```python
>>> res = cut(sepal_length, bins=[4, 6.5, 7.5, 8], include_lowest=1)
>>> print(res)
```

```
0      (3.999, 6.5]
1      (3.999, 6.5]
2      (3.999, 6.5]
3      (3.999, 6.5]
4      (3.999, 6.5]
           ...     
145      (6.5, 7.5]
146    (3.999, 6.5]
147    (3.999, 6.5]
148    (3.999, 6.5]
149    (3.999, 6.5]
Name: Sepal.Length, Length: 150, dtype: category
Categories (3, interval[float64, right]): [(3.999, 6.5] < (6.5, 7.5] < (7.5, 8.0]]
```

变量分位数分组
```python
>>> res = cut(sepal_length, cutbyquantile=1, bins=[0, 0.1, 0.5, 0.9, 1])
>>> print(res)
```

```
0                     (4.8, 5.8]
1                     (4.8, 5.8]
2      (4.2989999999999995, 4.8]
3      (4.2989999999999995, 4.8]
4                     (4.8, 5.8]
                 ...            
145                   (5.8, 6.9]
146                   (5.8, 6.9]
147                   (5.8, 6.9]
148                   (5.8, 6.9]
149                   (5.8, 6.9]
Name: Sepal.Length, Length: 150, dtype: category
Categories (4, interval[float64, right]): [(4.2989999999999995, 4.8] < (4.8, 5.8] < (5.8, 6.9] < (6.9, 7.9]]
```

变量分位数分组，指定标签
```python
>>> res = cut(sepal_length, cutbyquantile=1, bins=[0, 0.1, 0.5, 0.9, 1], labels=["低", "中低", "中高", "高"])
>>> print(res)
```

```
0      中低
1      中低
2       低
3       低
4      中低
       ..
145    中高
146    中高
147    中高
148    中高
149    中高
Name: Sepal.Length, Length: 150, dtype: category
Categories (4, object): ['低' < '中低' < '中高' < '高']
```
