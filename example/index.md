导入模块
```python
>>> from EasyPandas import read, index
>>> iris = read("../data/iris.xlsx")
>>> sepal_length = iris["Sepal.Length"]
```

测试Series参数
```python
>>> res = index(sepal_length, index=[i**2 for i in range(150)])
>>> print(res)
```

```
0        5.1
1        4.9
4        4.7
9        4.6
16       5.0
        ... 
21025    6.7
21316    6.3
21609    6.5
21904    6.2
22201    5.9
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，修改原始数据
```python
>>> res = index(sepal_length, index=[i**2 for i in range(150)], indexgdata=1)
>>> print(res)
```

```
0        5.1
1        4.9
4        5.0
9        4.9
16       5.4
        ... 
21025    NaN
21316    NaN
21609    NaN
21904    NaN
22201    NaN
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，将index转为一列
```python
>>> res = index(sepal_length)
>>> print(res)
```

```
     index  Sepal.Length
0        0           5.1
1        1           4.9
2        2           4.7
3        3           4.6
4        4           5.0
..     ...           ...
145    145           6.7
146    146           6.3
147    147           6.5
148    148           6.2
149    149           5.9

[150 rows x 2 columns]
```

测试DataFrame参数，修改行名
```python
>>> res = index(iris, index=[i**2 for i in range(150)])
>>> print(res)
```

```
       Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0               1           5.1          3.5           1.4          0.2   
1               2           4.9          3.0           1.4          0.2   
4               3           4.7          3.2           1.3          0.2   
9               4           4.6          3.1           1.5          0.2   
16              5           5.0          3.6           1.4          0.2   
...           ...           ...          ...           ...          ...   
21025         146           6.7          3.0           5.2          2.3   
21316         147           6.3          2.5           5.0          1.9   
21609         148           6.5          3.0           5.2          2.0   
21904         149           6.2          3.4           5.4          2.3   
22201         150           5.9          3.0           5.1          1.8   

         Species  
0         setosa  
1         setosa  
4         setosa  
9         setosa  
16        setosa  
...          ...  
21025  virginica  
21316  virginica  
21609  virginica  
21904  virginica  
22201  virginica  

[150 rows x 6 columns]
```

测试DataFrame参数，原数据修改
```python
>>> res = index(iris, index=[i**2 for i in range(150)], indexgdata=1)
>>> print(res)
```

```
       Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0             1.0           5.1          3.5           1.4          0.2   
1             2.0           4.9          3.0           1.4          0.2   
4             5.0           5.0          3.6           1.4          0.2   
9            10.0           4.9          3.1           1.5          0.1   
16           17.0           5.4          3.9           1.3          0.4   
...           ...           ...          ...           ...          ...   
21025         NaN           NaN          NaN           NaN          NaN   
21316         NaN           NaN          NaN           NaN          NaN   
21609         NaN           NaN          NaN           NaN          NaN   
21904         NaN           NaN          NaN           NaN          NaN   
22201         NaN           NaN          NaN           NaN          NaN   

      Species  
0      setosa  
1      setosa  
4      setosa  
9      setosa  
16     setosa  
...       ...  
21025     NaN  
21316     NaN  
21609     NaN  
21904     NaN  
22201     NaN  

[150 rows x 6 columns]
```

测试DataFrame参数，修改列名
```python
>>> res = index(iris, columns=iris.columns.tolist()[:-1] + ["A"])
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0             1           5.1          3.5           1.4          0.2   
1             2           4.9          3.0           1.4          0.2   
2             3           4.7          3.2           1.3          0.2   
3             4           4.6          3.1           1.5          0.2   
4             5           5.0          3.6           1.4          0.2   
..          ...           ...          ...           ...          ...   
145         146           6.7          3.0           5.2          2.3   
146         147           6.3          2.5           5.0          1.9   
147         148           6.5          3.0           5.2          2.0   
148         149           6.2          3.4           5.4          2.3   
149         150           5.9          3.0           5.1          1.8   

             A  
0       setosa  
1       setosa  
2       setosa  
3       setosa  
4       setosa  
..         ...  
145  virginica  
146  virginica  
147  virginica  
148  virginica  
149  virginica  

[150 rows x 6 columns]
```

测试DataFrame参数，修改列名，原数据修改
```python
>>> res = index(iris, columns=iris.columns.tolist()[:-1] + ["A"], columngdata=1)
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width   A
0             1           5.1          3.5           1.4          0.2 NaN
1             2           4.9          3.0           1.4          0.2 NaN
2             3           4.7          3.2           1.3          0.2 NaN
3             4           4.6          3.1           1.5          0.2 NaN
4             5           5.0          3.6           1.4          0.2 NaN
..          ...           ...          ...           ...          ...  ..
145         146           6.7          3.0           5.2          2.3 NaN
146         147           6.3          2.5           5.0          1.9 NaN
147         148           6.5          3.0           5.2          2.0 NaN
148         149           6.2          3.4           5.4          2.3 NaN
149         150           5.9          3.0           5.1          1.8 NaN

[150 rows x 6 columns]
```

测试DataFrame参数，修改列名和列名
```python
>>> res = index(iris, columns=iris.columns.tolist()[:-1] + ["A"], index=[i**2 for i in range(150)])
>>> print(res)
```

```
       Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0               1           5.1          3.5           1.4          0.2   
1               2           4.9          3.0           1.4          0.2   
4               3           4.7          3.2           1.3          0.2   
9               4           4.6          3.1           1.5          0.2   
16              5           5.0          3.6           1.4          0.2   
...           ...           ...          ...           ...          ...   
21025         146           6.7          3.0           5.2          2.3   
21316         147           6.3          2.5           5.0          1.9   
21609         148           6.5          3.0           5.2          2.0   
21904         149           6.2          3.4           5.4          2.3   
22201         150           5.9          3.0           5.1          1.8   

               A  
0         setosa  
1         setosa  
4         setosa  
9         setosa  
16        setosa  
...          ...  
21025  virginica  
21316  virginica  
21609  virginica  
21904  virginica  
22201  virginica  

[150 rows x 6 columns]
```

测试DataFrame参数，修改列名和列名，原数据修改
```python
>>> res = index(iris, columns=iris.columns.tolist()[:-1] + ["A"], index=[i**2 for i in range(150)], indexgdata=1, columngdata=1)
>>> print(res)
```

```
       Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width   A
0             1.0           5.1          3.5           1.4          0.2 NaN
1             2.0           4.9          3.0           1.4          0.2 NaN
4             5.0           5.0          3.6           1.4          0.2 NaN
9            10.0           4.9          3.1           1.5          0.1 NaN
16           17.0           5.4          3.9           1.3          0.4 NaN
...           ...           ...          ...           ...          ...  ..
21025         NaN           NaN          NaN           NaN          NaN NaN
21316         NaN           NaN          NaN           NaN          NaN NaN
21609         NaN           NaN          NaN           NaN          NaN NaN
21904         NaN           NaN          NaN           NaN          NaN NaN
22201         NaN           NaN          NaN           NaN          NaN NaN

[150 rows x 6 columns]
```

测试DataFrame参数，将某列作为行名
```python
>>> res = index(iris, index="Sepal.Length")
>>> print(res)
```

```
              Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  \
Sepal.Length                                                        
5.1                    1           5.1          3.5           1.4   
4.9                    2           4.9          3.0           1.4   
4.7                    3           4.7          3.2           1.3   
4.6                    4           4.6          3.1           1.5   
5.0                    5           5.0          3.6           1.4   
...                  ...           ...          ...           ...   
6.7                  146           6.7          3.0           5.2   
6.3                  147           6.3          2.5           5.0   
6.5                  148           6.5          3.0           5.2   
6.2                  149           6.2          3.4           5.4   
5.9                  150           5.9          3.0           5.1   

              Petal.Width    Species  
Sepal.Length                          
5.1                   0.2     setosa  
4.9                   0.2     setosa  
4.7                   0.2     setosa  
4.6                   0.2     setosa  
5.0                   0.2     setosa  
...                   ...        ...  
6.7                   2.3  virginica  
6.3                   1.9  virginica  
6.5                   2.0  virginica  
6.2                   2.3  virginica  
5.9                   1.8  virginica  

[150 rows x 6 columns]
```

测试DataFrame参数，将某列作为行名，从原数据中删除那一列
```python
>>> res = index(iris, index="Sepal.Length", drop=1)
>>> print(res)
```

```
              Unnamed: 0  Sepal.Width  Petal.Length  Petal.Width    Species
Sepal.Length                                                               
5.1                    1          3.5           1.4          0.2     setosa
4.9                    2          3.0           1.4          0.2     setosa
4.7                    3          3.2           1.3          0.2     setosa
4.6                    4          3.1           1.5          0.2     setosa
5.0                    5          3.6           1.4          0.2     setosa
...                  ...          ...           ...          ...        ...
6.7                  146          3.0           5.2          2.3  virginica
6.3                  147          2.5           5.0          1.9  virginica
6.5                  148          3.0           5.2          2.0  virginica
6.2                  149          3.4           5.4          2.3  virginica
5.9                  150          3.0           5.1          1.8  virginica

[150 rows x 5 columns]
```

测试DataFrame参数，将index转为列数据
```python
>>> res = index(iris, reset=1)
>>> print(res)
```

```
     index  Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0        0           1           5.1          3.5           1.4          0.2   
1        1           2           4.9          3.0           1.4          0.2   
2        2           3           4.7          3.2           1.3          0.2   
3        3           4           4.6          3.1           1.5          0.2   
4        4           5           5.0          3.6           1.4          0.2   
..     ...         ...           ...          ...           ...          ...   
145    145         146           6.7          3.0           5.2          2.3   
146    146         147           6.3          2.5           5.0          1.9   
147    147         148           6.5          3.0           5.2          2.0   
148    148         149           6.2          3.4           5.4          2.3   
149    149         150           5.9          3.0           5.1          1.8   

       Species  
0       setosa  
1       setosa  
2       setosa  
3       setosa  
4       setosa  
..         ...  
145  virginica  
146  virginica  
147  virginica  
148  virginica  
149  virginica  

[150 rows x 7 columns]
```
