导入模块
```python
>>> import numpy as np
>>> from EasyPandas import read, sort
>>> iris = read("../data/iris.csv")
```

对DataFrame按照index排序
```python
>>> idx = iris.index.tolist()
>>> np.random.shuffle(idx)
>>> iris.index = idx
>>> sortdf = sort(iris, by="index")
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0           123           7.7          2.8           6.7          2.0   
1            91           5.5          2.6           4.4          1.2   
2           112           6.4          2.7           5.3          1.9   
3             2           4.9          3.0           1.4          0.2   
4           148           6.5          3.0           5.2          2.0   
..          ...           ...          ...           ...          ...   
145         127           6.2          2.8           4.8          1.8   
146           8           5.0          3.4           1.5          0.2   
147          38           4.9          3.6           1.4          0.1   
148           7           4.6          3.4           1.4          0.3   
149          74           6.1          2.8           4.7          1.2   

        Species  
0     virginica  
1    versicolor  
2     virginica  
3        setosa  
4     virginica  
..          ...  
145   virginica  
146      setosa  
147      setosa  
148      setosa  
149  versicolor  

[150 rows x 6 columns]
```

对DataFrame按照index排序，降序
```python
>>> idx = iris.index.tolist()
>>> np.random.shuffle(idx)
>>> iris.index = idx
>>> sortdf = sort(iris, by="index", isincreasing=0)
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
149          97           5.7          2.9           4.2          1.3   
148          24           5.1          3.3           1.7          0.5   
147          76           6.6          3.0           4.4          1.4   
146         129           6.4          2.8           5.6          2.1   
145          29           5.2          3.4           1.4          0.2   
..          ...           ...          ...           ...          ...   
4            75           6.4          2.9           4.3          1.3   
3            55           6.5          2.8           4.6          1.5   
2             1           5.1          3.5           1.4          0.2   
1            38           4.9          3.6           1.4          0.1   
0            66           6.7          3.1           4.4          1.4   

        Species  
149  versicolor  
148      setosa  
147  versicolor  
146   virginica  
145      setosa  
..          ...  
4    versicolor  
3    versicolor  
2        setosa  
1        setosa  
0    versicolor  

[150 rows x 6 columns]
```

对DataFrame按照index排序，重新设置index
```python
>>> idx = iris.index.tolist()
>>> np.random.shuffle(idx)
>>> iris.index = idx
>>> sortdf = sort(iris, by="index", isincreasing=0, isreindex=1)
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0             7           4.6          3.4           1.4          0.3   
1            88           6.3          2.3           4.4          1.3   
2            31           4.8          3.1           1.6          0.2   
3            87           6.7          3.1           4.7          1.5   
4            98           6.2          2.9           4.3          1.3   
..          ...           ...          ...           ...          ...   
145          62           5.9          3.0           4.2          1.5   
146          76           6.6          3.0           4.4          1.4   
147         106           7.6          3.0           6.6          2.1   
148           6           5.4          3.9           1.7          0.4   
149          39           4.4          3.0           1.3          0.2   

        Species  
0        setosa  
1    versicolor  
2        setosa  
3    versicolor  
4    versicolor  
..          ...  
145  versicolor  
146  versicolor  
147   virginica  
148      setosa  
149      setosa  

[150 rows x 6 columns]
```

对DataFrame按照index排序，重新设置index，在原数据上修改
```python
>>> idx = iris.index.tolist()
>>> np.random.shuffle(idx)
>>> iris.index = idx
>>> sortdf = sort(iris, by="index", isincreasing=0, isreindex=1, isinplace=1)
>>> print(sortdf)
>>> print(iris)
```

```
None
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0           104           6.3          2.9           5.6          1.8   
1           142           6.9          3.1           5.1          2.3   
2            90           5.5          2.5           4.0          1.3   
3            47           5.1          3.8           1.6          0.2   
4            63           6.0          2.2           4.0          1.0   
..          ...           ...          ...           ...          ...   
145          52           6.4          3.2           4.5          1.5   
146           8           5.0          3.4           1.5          0.2   
147         101           6.3          3.3           6.0          2.5   
148          19           5.7          3.8           1.7          0.3   
149          92           6.1          3.0           4.6          1.4   

        Species  
0     virginica  
1     virginica  
2    versicolor  
3        setosa  
4    versicolor  
..          ...  
145  versicolor  
146      setosa  
147   virginica  
148      setosa  
149  versicolor  

[150 rows x 6 columns]
```

对DataFrame按照colname排序
```python
>>> sortdf = sort(iris, by="Sepal.Length")
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
11           14           4.3          3.0           1.1          0.1   
137           9           4.4          2.9           1.4          0.2   
85           43           4.4          3.2           1.3          0.2   
100          39           4.4          3.0           1.3          0.2   
73           42           4.5          2.3           1.3          0.3   
..          ...           ...          ...           ...          ...   
103         119           7.7          2.6           6.9          2.3   
105         118           7.7          3.8           6.7          2.2   
41          123           7.7          2.8           6.7          2.0   
131         136           7.7          3.0           6.1          2.3   
117         132           7.9          3.8           6.4          2.0   

       Species  
11      setosa  
137     setosa  
85      setosa  
100     setosa  
73      setosa  
..         ...  
103  virginica  
105  virginica  
41   virginica  
131  virginica  
117  virginica  

[150 rows x 6 columns]
```

对DataFrame按照colname排序，降序
```python
>>> sortdf = sort(iris, by="Sepal.Length", isincreasing=0)
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
117         132           7.9          3.8           6.4          2.0   
131         136           7.7          3.0           6.1          2.3   
41          123           7.7          2.8           6.7          2.0   
103         119           7.7          2.6           6.9          2.3   
105         118           7.7          3.8           6.7          2.2   
..          ...           ...          ...           ...          ...   
73           42           4.5          2.3           1.3          0.3   
100          39           4.4          3.0           1.3          0.2   
137           9           4.4          2.9           1.4          0.2   
85           43           4.4          3.2           1.3          0.2   
11           14           4.3          3.0           1.1          0.1   

       Species  
117  virginica  
131  virginica  
41   virginica  
103  virginica  
105  virginica  
..         ...  
73      setosa  
100     setosa  
137     setosa  
85      setosa  
11      setosa  

[150 rows x 6 columns]
```

对DataFrame按照colname排序，重新设置index
```python
>>> sortdf = sort(iris, by="Sepal.Length", isincreasing=0, isreindex=1)
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0           132           7.9          3.8           6.4          2.0   
1           136           7.7          3.0           6.1          2.3   
2           123           7.7          2.8           6.7          2.0   
3           119           7.7          2.6           6.9          2.3   
4           118           7.7          3.8           6.7          2.2   
..          ...           ...          ...           ...          ...   
145          42           4.5          2.3           1.3          0.3   
146          39           4.4          3.0           1.3          0.2   
147           9           4.4          2.9           1.4          0.2   
148          43           4.4          3.2           1.3          0.2   
149          14           4.3          3.0           1.1          0.1   

       Species  
0    virginica  
1    virginica  
2    virginica  
3    virginica  
4    virginica  
..         ...  
145     setosa  
146     setosa  
147     setosa  
148     setosa  
149     setosa  

[150 rows x 6 columns]
```

对DataFrame按照colname排序，重新设置index，在原数据上修改
```python
>>> sortdf = sort(iris, by="Sepal.Length", isincreasing=0, isreindex=1, isinplace=1)
>>> print(sortdf)
>>> print(iris)
```

```
None
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0           132           7.9          3.8           6.4          2.0   
1           136           7.7          3.0           6.1          2.3   
2           123           7.7          2.8           6.7          2.0   
3           119           7.7          2.6           6.9          2.3   
4           118           7.7          3.8           6.7          2.2   
..          ...           ...          ...           ...          ...   
145          42           4.5          2.3           1.3          0.3   
146          39           4.4          3.0           1.3          0.2   
147           9           4.4          2.9           1.4          0.2   
148          43           4.4          3.2           1.3          0.2   
149          14           4.3          3.0           1.1          0.1   

       Species  
0    virginica  
1    virginica  
2    virginica  
3    virginica  
4    virginica  
..         ...  
145     setosa  
146     setosa  
147     setosa  
148     setosa  
149     setosa  

[150 rows x 6 columns]
```

对DataFrame按照多个colname排序
```python
>>> sortdf = sort(iris, by=["Sepal.Width", "Sepal.Length"])
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
126          61           5.0          2.0           3.5          1.0   
62           63           6.0          2.2           4.0          1.0   
64          120           6.0          2.2           5.0          1.5   
51           69           6.2          2.2           4.5          1.5   
145          42           4.5          2.3           1.3          0.3   
..          ...           ...          ...           ...          ...   
99            6           5.4          3.9           1.7          0.4   
75           15           5.8          4.0           1.2          0.2   
107          33           5.2          4.1           1.5          0.1   
95           34           5.5          4.2           1.4          0.2   
80           16           5.7          4.4           1.5          0.4   

        Species  
126  versicolor  
62   versicolor  
64    virginica  
51   versicolor  
145      setosa  
..          ...  
99       setosa  
75       setosa  
107      setosa  
95       setosa  
80       setosa  

[150 rows x 6 columns]
```

对DataFrame按照多个colname排序，一个升序，一个降序
```python
>>> sortdf = sort(iris, by=["Sepal.Width", "Sepal.Length"], isincreasing=[1,0])
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
126          61           5.0          2.0           3.5          1.0   
51           69           6.2          2.2           4.5          1.5   
62           63           6.0          2.2           4.0          1.0   
64          120           6.0          2.2           5.0          1.5   
49           88           6.3          2.3           4.4          1.3   
..          ...           ...          ...           ...          ...   
99            6           5.4          3.9           1.7          0.4   
75           15           5.8          4.0           1.2          0.2   
107          33           5.2          4.1           1.5          0.1   
95           34           5.5          4.2           1.4          0.2   
80           16           5.7          4.4           1.5          0.4   

        Species  
126  versicolor  
51   versicolor  
62   versicolor  
64    virginica  
49   versicolor  
..          ...  
99       setosa  
75       setosa  
107      setosa  
95       setosa  
80       setosa
```

对DataFrame按照多个colname排序，一个升序，一个降序，一个升序，一个降序
```python
>>> sortdf = sort(iris, by=["Sepal.Width", "Sepal.Length", "Petal.Length", "Petal.Width"], isincreasing=[1,0,1,0])
>>> print(sortdf)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
126          61           5.0          2.0           3.5          1.0   
51           69           6.2          2.2           4.5          1.5   
62           63           6.0          2.2           4.0          1.0   
64          120           6.0          2.2           5.0          1.5   
49           88           6.3          2.3           4.4          1.3   
..          ...           ...          ...           ...          ...   
99            6           5.4          3.9           1.7          0.4   
75           15           5.8          4.0           1.2          0.2   
107          33           5.2          4.1           1.5          0.1   
95           34           5.5          4.2           1.4          0.2   
80           16           5.7          4.4           1.5          0.4   

        Species  
126  versicolor  
51   versicolor  
62   versicolor  
64    virginica  
49   versicolor  
..          ...  
99       setosa  
75       setosa  
107      setosa  
95       setosa  
80       setosa  

[150 rows x 6 columns]
```

对Series按照index排序
```python
>>> idx = iris.index.tolist()
>>> np.random.shuffle(idx)
>>> iris.index = idx
>>> sortdf = sort(iris["Sepal.Length"], by="index")
>>> print(sortdf)
```

```
0      5.5
1      6.4
2      5.6
3      5.0
4      7.4
      ... 
145    6.8
146    6.5
147    6.7
148    7.7
149    5.0
Name: Sepal.Length, Length: 150, dtype: float64
```

对Series按照index排序，降序
```python
>>> idx = iris.index.tolist()
>>> np.random.shuffle(idx)
>>> iris.index = idx
>>> sortdf = sort(iris["Sepal.Length"], by="index", isincreasing=0)
>>> print(sortdf)
```

```
149    6.2
148    5.1
147    4.9
146    6.5
145    4.8
      ... 
4      5.8
3      4.8
2      5.0
1      5.6
0      5.5
Name: Sepal.Length, Length: 150, dtype: float64
```

对Series按照index排序，降序，重新设置index
```python
>>> idx = iris.index.tolist()
>>> np.random.shuffle(idx)
>>> iris.index = idx
>>> sortdf = sort(iris["Sepal.Length"], by="index", isincreasing=0, isreindex=1)
>>> print(sortdf)
```

```
0      6.0
1      6.5
2      5.1
3      5.0
4      7.1
      ... 
145    6.5
146    6.7
147    4.9
148    6.1
149    6.9
Name: Sepal.Length, Length: 150, dtype: float64
```

对Series按照index排序，降序，重新设置index，在原数据上修改
```python
>>> idx = iris.index.tolist()
>>> np.random.shuffle(idx)
>>> iris.index = idx
>>> sortdf = sort(iris["Sepal.Length"], by="index", isincreasing=0, isreindex=1, isinplace=1)
>>> print(sortdf)
>>> print(iris)
```

```
None
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
5           132           5.1          3.8           6.4          2.0   
114         136           5.7          3.0           6.1          2.3   
111         123           4.6          2.8           6.7          2.0   
4           119           6.5          2.6           6.9          2.3   
77          118           6.3          3.8           6.7          2.2   
..          ...           ...          ...           ...          ...   
39           42           7.7          2.3           1.3          0.3   
139          39           6.4          3.0           1.3          0.2   
132           9           5.2          2.9           1.4          0.2   
78           43           6.3          3.2           1.3          0.2   
37           14           5.4          3.0           1.1          0.1   

       Species  
5    virginica  
114  virginica  
111  virginica  
4    virginica  
77   virginica  
..         ...  
39      setosa  
139     setosa  
132     setosa  
78      setosa  
37      setosa  

[150 rows x 6 columns]
```

对Series按照value排序
```python
>>> sortdf = sort(iris["Sepal.Length"])
>>> print(sortdf)
```

```
112    4.3
71     4.4
17     4.4
10     4.4
110    4.5
      ... 
38     7.7
35     7.7
72     7.7
145    7.7
144    7.9
Name: Sepal.Length, Length: 150, dtype: float64
```

对Series按照value排序，降序
```python
>>> sortdf = sort(iris["Sepal.Length"], isincreasing=0)
>>> print(sortdf)
```

```
144    7.9
38     7.7
35     7.7
72     7.7
145    7.7
      ... 
110    4.5
71     4.4
17     4.4
10     4.4
112    4.3
Name: Sepal.Length, Length: 150, dtype: float64
```

对Series按照value排序，降序，重新设置索引
```python
>>> sortdf = sort(iris["Sepal.Length"], isincreasing=0, isreindex=1)
>>> print(sortdf)
```

```
0      7.9
1      7.7
2      7.7
3      7.7
4      7.7
      ... 
145    4.5
146    4.4
147    4.4
148    4.4
149    4.3
Name: Sepal.Length, Length: 150, dtype: float64
```

对DataFrame的列名进行排序
```python
>>> sortdf = sort(iris, by="index", issortcol=1)
>>> print(sortdf)
```

```
     Petal.Length  Petal.Width  Sepal.Length  Sepal.Width    Species  \
5             6.4          2.0           5.1          3.8  virginica   
114           6.1          2.3           5.7          3.0  virginica   
111           6.7          2.0           4.6          2.8  virginica   
4             6.9          2.3           6.5          2.6  virginica   
77            6.7          2.2           6.3          3.8  virginica   
..            ...          ...           ...          ...        ...   
39            1.3          0.3           7.7          2.3     setosa   
139           1.3          0.2           6.4          3.0     setosa   
132           1.4          0.2           5.2          2.9     setosa   
78            1.3          0.2           6.3          3.2     setosa   
37            1.1          0.1           5.4          3.0     setosa   

     Unnamed: 0  
5           132  
114         136  
111         123  
4           119  
77          118  
..          ...  
39           42  
139          39  
132           9  
78           43  
37           14  

[150 rows x 6 columns]
```
