导入模块
```python
>>> from EasyPandas import duplicate, read
>>> iris = read("../data/iris.xlsx")
```

Series标记重复值
```python
>>> res = duplicate(iris["Sepal.Length"])
>>> print(res)
```

```
0      False
1      False
2      False
3      False
4      False
       ...  
145     True
146     True
147     True
148     True
149     True
Name: Sepal.Length, Length: 150, dtype: bool
```

Series标记重复值，keep=last
```python
>>> res = duplicate(iris["Sepal.Length"], keep="last")
>>> print(res)
```

```
0       True
1       True
2       True
3       True
4       True
       ...  
145    False
146    False
147    False
148    False
149    False
Name: Sepal.Length, Length: 150, dtype: bool
```

Series标记重复值，keep=False
```python
>>> res = duplicate(iris["Sepal.Length"], keep=False)
>>> print(res)
```

```
0      True
1      True
2      True
3      True
4      True
       ... 
145    True
146    True
147    True
148    True
149    True
Name: Sepal.Length, Length: 150, dtype: bool
```

DataFrame标记重复值
```python
>>> res = duplicate(iris)
>>> print(res)
```

```
0      False
1      False
2      False
3      False
4      False
       ...  
145    False
146    False
147    False
148    False
149    False
Length: 150, dtype: bool
```

DataFrame标记重复值，指定变量
```python
>>> res = duplicate(iris, subset="Species")
>>> print(res)
```

```
0      False
1       True
2       True
3       True
4       True
       ...  
145     True
146     True
147     True
148     True
149     True
Length: 150, dtype: bool
```

Series删除重复值
```python
>>> res = duplicate(iris["Sepal.Length"], action="drop")
>>> print(res)
```

```
0      5.1
1      4.9
2      4.7
3      4.6
4      5.0
5      5.4
8      4.4
11     4.8
13     4.3
14     5.8
15     5.7
27     5.2
33     5.5
41     4.5
48     5.3
50     7.0
51     6.4
52     6.9
54     6.5
56     6.3
58     6.6
61     5.9
62     6.0
63     6.1
64     5.6
65     6.7
68     6.2
76     6.8
102    7.1
105    7.6
107    7.3
109    7.2
117    7.7
130    7.4
131    7.9
Name: Sepal.Length, dtype: float64
```

DataFrame删除重复值
```python
>>> res = duplicate(iris, action="drop", subset="Species")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0             1           5.1          3.5           1.4          0.2   
50           51           7.0          3.2           4.7          1.4   
100         101           6.3          3.3           6.0          2.5   

        Species  
0        setosa  
50   versicolor  
100   virginica 
```
