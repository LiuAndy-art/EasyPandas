导入模块
```python
>>> import numpy as np
>>> from EasyPandas import read, group
>>> iris = read("../data/iris.xlsx", excelfileparamsdict={"index_col": 0})
```

不给func，只分组
```python
>>> res = group(iris, by="Species")
>>> print(res)
```

```
[('setosa',     Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
1            5.1          3.5           1.4          0.2  setosa
2            4.9          3.0           1.4          0.2  setosa
3            4.7          3.2           1.3          0.2  setosa
4            4.6          3.1           1.5          0.2  setosa
5            5.0          3.6           1.4          0.2  setosa
6            5.4          3.9           1.7          0.4  setosa
7            4.6          3.4           1.4          0.3  setosa
8            5.0          3.4           1.5          0.2  setosa
9            4.4          2.9           1.4          0.2  setosa
10           4.9          3.1           1.5          0.1  setosa
11           5.4          3.7           1.5          0.2  setosa
12           4.8          3.4           1.6          0.2  setosa
13           4.8          3.0           1.4          0.1  setosa
14           4.3          3.0           1.1          0.1  setosa
15           5.8          4.0           1.2          0.2  setosa
16           5.7          4.4           1.5          0.4  setosa
17           5.4          3.9           1.3          0.4  setosa
18           5.1          3.5           1.4          0.3  setosa
19           5.7          3.8           1.7          0.3  setosa
20           5.1          3.8           1.5          0.3  setosa
21           5.4          3.4           1.7          0.2  setosa
22           5.1          3.7           1.5          0.4  setosa
23           4.6          3.6           1.0          0.2  setosa
24           5.1          3.3           1.7          0.5  setosa
25           4.8          3.4           1.9          0.2  setosa
26           5.0          3.0           1.6          0.2  setosa
27           5.0          3.4           1.6          0.4  setosa
28           5.2          3.5           1.5          0.2  setosa
29           5.2          3.4           1.4          0.2  setosa
30           4.7          3.2           1.6          0.2  setosa
31           4.8          3.1           1.6          0.2  setosa
32           5.4          3.4           1.5          0.4  setosa
33           5.2          4.1           1.5          0.1  setosa
34           5.5          4.2           1.4          0.2  setosa
35           4.9          3.1           1.5          0.2  setosa
36           5.0          3.2           1.2          0.2  setosa
37           5.5          3.5           1.3          0.2  setosa
38           4.9          3.6           1.4          0.1  setosa
39           4.4          3.0           1.3          0.2  setosa
40           5.1          3.4           1.5          0.2  setosa
41           5.0          3.5           1.3          0.3  setosa
42           4.5          2.3           1.3          0.3  setosa
43           4.4          3.2           1.3          0.2  setosa
44           5.0          3.5           1.6          0.6  setosa
45           5.1          3.8           1.9          0.4  setosa
46           4.8          3.0           1.4          0.3  setosa
47           5.1          3.8           1.6          0.2  setosa
48           4.6          3.2           1.4          0.2  setosa
49           5.3          3.7           1.5          0.2  setosa
50           5.0          3.3           1.4          0.2  setosa), ('versicolor',      Sepal.Length  Sepal.Width  Petal.Length  Petal.Width     Species
51            7.0          3.2           4.7          1.4  versicolor
52            6.4          3.2           4.5          1.5  versicolor
53            6.9          3.1           4.9          1.5  versicolor
54            5.5          2.3           4.0          1.3  versicolor
55            6.5          2.8           4.6          1.5  versicolor
56            5.7          2.8           4.5          1.3  versicolor
57            6.3          3.3           4.7          1.6  versicolor
58            4.9          2.4           3.3          1.0  versicolor
59            6.6          2.9           4.6          1.3  versicolor
60            5.2          2.7           3.9          1.4  versicolor
61            5.0          2.0           3.5          1.0  versicolor
62            5.9          3.0           4.2          1.5  versicolor
63            6.0          2.2           4.0          1.0  versicolor
64            6.1          2.9           4.7          1.4  versicolor
65            5.6          2.9           3.6          1.3  versicolor
66            6.7          3.1           4.4          1.4  versicolor
67            5.6          3.0           4.5          1.5  versicolor
68            5.8          2.7           4.1          1.0  versicolor
69            6.2          2.2           4.5          1.5  versicolor
70            5.6          2.5           3.9          1.1  versicolor
71            5.9          3.2           4.8          1.8  versicolor
72            6.1          2.8           4.0          1.3  versicolor
73            6.3          2.5           4.9          1.5  versicolor
74            6.1          2.8           4.7          1.2  versicolor
75            6.4          2.9           4.3          1.3  versicolor
76            6.6          3.0           4.4          1.4  versicolor
77            6.8          2.8           4.8          1.4  versicolor
78            6.7          3.0           5.0          1.7  versicolor
79            6.0          2.9           4.5          1.5  versicolor
80            5.7          2.6           3.5          1.0  versicolor
81            5.5          2.4           3.8          1.1  versicolor
82            5.5          2.4           3.7          1.0  versicolor
83            5.8          2.7           3.9          1.2  versicolor
84            6.0          2.7           5.1          1.6  versicolor
85            5.4          3.0           4.5          1.5  versicolor
86            6.0          3.4           4.5          1.6  versicolor
87            6.7          3.1           4.7          1.5  versicolor
88            6.3          2.3           4.4          1.3  versicolor
89            5.6          3.0           4.1          1.3  versicolor
90            5.5          2.5           4.0          1.3  versicolor
91            5.5          2.6           4.4          1.2  versicolor
92            6.1          3.0           4.6          1.4  versicolor
93            5.8          2.6           4.0          1.2  versicolor
94            5.0          2.3           3.3          1.0  versicolor
95            5.6          2.7           4.2          1.3  versicolor
96            5.7          3.0           4.2          1.2  versicolor
97            5.7          2.9           4.2          1.3  versicolor
98            6.2          2.9           4.3          1.3  versicolor
99            5.1          2.5           3.0          1.1  versicolor
100           5.7          2.8           4.1          1.3  versicolor), ('virginica',      Sepal.Length  Sepal.Width  Petal.Length  Petal.Width    Species
101           6.3          3.3           6.0          2.5  virginica
102           5.8          2.7           5.1          1.9  virginica
103           7.1          3.0           5.9          2.1  virginica
104           6.3          2.9           5.6          1.8  virginica
105           6.5          3.0           5.8          2.2  virginica
106           7.6          3.0           6.6          2.1  virginica
107           4.9          2.5           4.5          1.7  virginica
108           7.3          2.9           6.3          1.8  virginica
109           6.7          2.5           5.8          1.8  virginica
110           7.2          3.6           6.1          2.5  virginica
111           6.5          3.2           5.1          2.0  virginica
112           6.4          2.7           5.3          1.9  virginica
113           6.8          3.0           5.5          2.1  virginica
114           5.7          2.5           5.0          2.0  virginica
115           5.8          2.8           5.1          2.4  virginica
116           6.4          3.2           5.3          2.3  virginica
117           6.5          3.0           5.5          1.8  virginica
118           7.7          3.8           6.7          2.2  virginica
119           7.7          2.6           6.9          2.3  virginica
120           6.0          2.2           5.0          1.5  virginica
121           6.9          3.2           5.7          2.3  virginica
122           5.6          2.8           4.9          2.0  virginica
123           7.7          2.8           6.7          2.0  virginica
124           6.3          2.7           4.9          1.8  virginica
125           6.7          3.3           5.7          2.1  virginica
126           7.2          3.2           6.0          1.8  virginica
127           6.2          2.8           4.8          1.8  virginica
128           6.1          3.0           4.9          1.8  virginica
129           6.4          2.8           5.6          2.1  virginica
130           7.2          3.0           5.8          1.6  virginica
131           7.4          2.8           6.1          1.9  virginica
132           7.9          3.8           6.4          2.0  virginica
133           6.4          2.8           5.6          2.2  virginica
134           6.3          2.8           5.1          1.5  virginica
135           6.1          2.6           5.6          1.4  virginica
136           7.7          3.0           6.1          2.3  virginica
137           6.3          3.4           5.6          2.4  virginica
138           6.4          3.1           5.5          1.8  virginica
139           6.0          3.0           4.8          1.8  virginica
140           6.9          3.1           5.4          2.1  virginica
141           6.7          3.1           5.6          2.4  virginica
142           6.9          3.1           5.1          2.3  virginica
143           5.8          2.7           5.1          1.9  virginica
144           6.8          3.2           5.9          2.3  virginica
145           6.7          3.3           5.7          2.5  virginica
146           6.7          3.0           5.2          2.3  virginica
147           6.3          2.5           5.0          1.9  virginica
148           6.5          3.0           5.2          2.0  virginica
149           6.2          3.4           5.4          2.3  virginica
150           5.9          3.0           5.1          1.8  virginica)]
```

不给func，只分组，给定组别名称
```python
>>> res = group(iris, by="Species", groupname="virginica")
>>> print(res)
```

```
     Sepal.Length  Sepal.Width  Petal.Length  Petal.Width    Species
101           6.3          3.3           6.0          2.5  virginica
102           5.8          2.7           5.1          1.9  virginica
103           7.1          3.0           5.9          2.1  virginica
104           6.3          2.9           5.6          1.8  virginica
105           6.5          3.0           5.8          2.2  virginica
106           7.6          3.0           6.6          2.1  virginica
107           4.9          2.5           4.5          1.7  virginica
108           7.3          2.9           6.3          1.8  virginica
109           6.7          2.5           5.8          1.8  virginica
110           7.2          3.6           6.1          2.5  virginica
111           6.5          3.2           5.1          2.0  virginica
112           6.4          2.7           5.3          1.9  virginica
113           6.8          3.0           5.5          2.1  virginica
114           5.7          2.5           5.0          2.0  virginica
115           5.8          2.8           5.1          2.4  virginica
116           6.4          3.2           5.3          2.3  virginica
117           6.5          3.0           5.5          1.8  virginica
118           7.7          3.8           6.7          2.2  virginica
119           7.7          2.6           6.9          2.3  virginica
120           6.0          2.2           5.0          1.5  virginica
121           6.9          3.2           5.7          2.3  virginica
122           5.6          2.8           4.9          2.0  virginica
123           7.7          2.8           6.7          2.0  virginica
124           6.3          2.7           4.9          1.8  virginica
125           6.7          3.3           5.7          2.1  virginica
126           7.2          3.2           6.0          1.8  virginica
127           6.2          2.8           4.8          1.8  virginica
128           6.1          3.0           4.9          1.8  virginica
129           6.4          2.8           5.6          2.1  virginica
130           7.2          3.0           5.8          1.6  virginica
131           7.4          2.8           6.1          1.9  virginica
132           7.9          3.8           6.4          2.0  virginica
133           6.4          2.8           5.6          2.2  virginica
134           6.3          2.8           5.1          1.5  virginica
135           6.1          2.6           5.6          1.4  virginica
136           7.7          3.0           6.1          2.3  virginica
137           6.3          3.4           5.6          2.4  virginica
138           6.4          3.1           5.5          1.8  virginica
139           6.0          3.0           4.8          1.8  virginica
140           6.9          3.1           5.4          2.1  virginica
141           6.7          3.1           5.6          2.4  virginica
142           6.9          3.1           5.1          2.3  virginica
143           5.8          2.7           5.1          1.9  virginica
144           6.8          3.2           5.9          2.3  virginica
145           6.7          3.3           5.7          2.5  virginica
146           6.7          3.0           5.2          2.3  virginica
147           6.3          2.5           5.0          1.9  virginica
148           6.5          3.0           5.2          2.0  virginica
149           6.2          3.4           5.4          2.3  virginica
150           5.9          3.0           5.1          1.8  virginica
```

单变量分组，给定单个func
```python
>>> res = group(iris, by="Species", func="sum")
>>> print(res)
```

```
            Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
Species                                                         
setosa             250.3        171.4          73.1         12.3
versicolor         296.8        138.5         213.0         66.3
virginica          329.4        148.7         277.6        101.3
```

单变量分组，给定多个func
```python
>>> res = group(iris, by="Species", func=["mean", "std"])
>>> print(res)
```

```
           Sepal.Length           Sepal.Width           Petal.Length  \
                   mean       std        mean       std         mean   
Species                                                                
setosa            5.006  0.352490       3.428  0.379064        1.462   
versicolor        5.936  0.516171       2.770  0.313798        4.260   
virginica         6.588  0.635880       2.974  0.322497        5.552   

                     Petal.Width            
                 std        mean       std  
Species                                     
setosa      0.173664       0.246  0.105386  
versicolor  0.469911       1.326  0.197753  
virginica   0.551895       2.026  0.274650
```

单变量分组，给定多个func，自定义函数
```python
>>> res = group(iris, by="Species", func=["mean", lambda x: x.max()-x.min()])
>>> print(res)
```

```
           Sepal.Length            Sepal.Width            Petal.Length  \
                   mean <lambda_0>        mean <lambda_0>         mean   
Species                                                                  
setosa            5.006        1.5       3.428        2.1        1.462   
versicolor        5.936        2.1       2.770        1.4        4.260   
virginica         6.588        3.0       2.974        1.6        5.552   

                      Petal.Width             
           <lambda_0>        mean <lambda_0>  
Species                                       
setosa            0.9       0.246        0.5  
versicolor        2.1       1.326        0.8  
virginica         2.4       2.026        1.1
```

多变量分组，给定单个func
```python
>>> df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"], "B": ["one", "one", "two", "three", "two", "two", "one", "three"], "C": np.random.randn(8), "D": np.random.randn(8)})
>>> print(df)
>>> res = group(df, by=["A", "B"], func="mean")
>>> print(res)
```

```
     A      B         C         D
0  foo    one -0.154084  0.094814
1  bar    one  1.832513  0.480066
2  foo    two -0.140966 -0.266691
3  bar  three -0.816862 -1.022963
4  foo    two -1.085039  1.707270
5  bar    two  1.207212  0.187914
6  foo    one -1.123343 -0.482232
7  foo  three  0.249204 -0.672850
                  C         D
A   B                        
bar one    1.832513  0.480066
    three -0.816862 -1.022963
    two    1.207212  0.187914
foo one   -0.638713 -0.193709
    three  0.249204 -0.672850
    two   -0.613003  0.720289
```

多变量分组，给定多个func
```python
>>> df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"], "B": ["one", "one", "two", "three", "two", "two", "one", "three"], "C": np.random.randn(8), "D": np.random.randn(8)})
>>> print(df)
>>> res = group(df, by=["A", "B"], func=["mean", "sum", lambda x: x.min()/x.max()])
>>> print(res)
```

```
     A      B         C         D
0  foo    one -0.567393  1.239113
1  bar    one  3.226269 -0.142902
2  foo    two -1.911891  0.645869
3  bar  three  0.186747  1.706045
4  foo    two -0.196699 -0.455707
5  bar    two  1.627984 -0.607902
6  foo    one -0.339718 -0.281234
7  foo  three -1.596971  0.857096
                  C                              D                     
               mean       sum <lambda_0>      mean       sum <lambda_0>
A   B                                                                  
bar one    3.226269  3.226269   1.000000 -0.142902 -0.142902   1.000000
    three  0.186747  0.186747   1.000000  1.706045  1.706045   1.000000
    two    1.627984  1.627984   1.000000 -0.607902 -0.607902   1.000000
foo one   -0.453556 -0.907112   1.670186  0.478940  0.957879  -0.226964
    three -1.596971 -1.596971   1.000000  0.857096  0.857096   1.000000
    two   -1.054295 -2.108590   9.719869  0.095081  0.190162  -0.705572
```

单变量分组，给定单个func，改名称
```python
>>> res = group(iris, by="Species", func=["sum"], renamedict={"sum": "求和"})
>>> print(res)
```

```
           Sepal.Length Sepal.Width Petal.Length Petal.Width
                     求和          求和           求和          求和
Species                                                     
setosa            250.3       171.4         73.1        12.3
versicolor        296.8       138.5        213.0        66.3
virginica         329.4       148.7        277.6       101.3
```

单变量分组，给定多个func，改名称
```python
>>> res = group(iris, by="Species", func=["sum", "mean"], renamedict={"sum": "求和", "mean": "平均值"})
>>> print(res)
```

```
           Sepal.Length        Sepal.Width        Petal.Length         \
                     求和    平均值          求和    平均值           求和    平均值   
Species                                                                 
setosa            250.3  5.006       171.4  3.428         73.1  1.462   
versicolor        296.8  5.936       138.5  2.770        213.0  4.260   
virginica         329.4  6.588       148.7  2.974        277.6  5.552   

           Petal.Width         
                    求和    平均值  
Species                        
setosa            12.3  0.246  
versicolor        66.3  1.326  
virginica        101.3  2.026 
```

多个变量分组，给定一个func，改名称
```python
>>> df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"], "B": ["one", "one", "two", "three", "two", "two", "one", "three"], "C": np.random.randn(8), "D": np.random.randn(8)})
>>> print(df)
>>> res = group(df, by=["A", "B"], func=["mean"], renamedict={"mean": "均值"})
>>> print(res)
```

```
     A      B         C         D
0  foo    one  1.349499 -0.273962
1  bar    one -0.334844 -0.814171
2  foo    two  0.268184  1.637648
3  bar  three -0.336772  0.157920
4  foo    two  0.148286 -0.550030
5  bar    two -1.810250 -0.317517
6  foo    one  1.174568  0.508763
7  foo  three  0.199181  1.447613
                  C         D
                 均值        均值
A   B                        
bar one   -0.334844 -0.814171
    three -0.336772  0.157920
    two   -1.810250 -0.317517
foo one    1.262033  0.117400
    three  0.199181  1.447613
    two    0.208235  0.543809
```

多个变量分组，给定多个func，改名称
```python
>>> df = pd.DataFrame({"A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"], "B": ["one", "one", "two", "three", "two", "two", "one", "three"], "C": np.random.randn(8), "D": np.random.randn(8)})
>>> print(df)
>>> res = group(df, by=["A", "B"], func=["sum", "mean"], renamedict={"sum": "求和", "mean": "平均值"})
>>> print(res)
```

```
     A      B         C         D
0  foo    one  0.147894  0.724984
1  bar    one -0.910781 -0.747095
2  foo    two  1.053112 -0.815764
3  bar  three -0.887718 -0.388407
4  foo    two  1.036878 -0.047299
5  bar    two  0.049228  0.264397
6  foo    one  0.221033  0.253804
7  foo  three  0.732797 -0.278411
                  C                   D          
                 求和       平均值        求和       平均值
A   B                                            
bar one   -0.910781 -0.910781 -0.747095 -0.747095
    three -0.887718 -0.887718 -0.388407 -0.388407
    two    0.049228  0.049228  0.264397  0.264397
foo one    0.368927  0.184463  0.978788  0.489394
    three  0.732797  0.732797 -0.278411 -0.278411
    two    2.089990  1.044995 -0.863063 -0.431531
```

单变量分组，给定func，字典形式
```python
>>> res = group(iris, by="Species", func={"Sepal.Length": "sum"})
>>> print(res)
```

```
            Sepal.Length
Species                 
setosa             250.3
versicolor         296.8
virginica          329.4
```

单变量分组，给定func，字典形式，改名
```python
>>> res = group(iris, by="Species", func={"Sepal.Length": "sum"}, renamedict={"sum": "求和"})
>>> print(res)
```

```
               求和
Species          
setosa      250.3
versicolor  296.8
virginica   329.4
```

单变量分组，给定func，字典形式
```python
>>> res = group(iris, by="Species", func={"Sepal.Length": ["sum", "mean"], "Sepal.Width": ["max", "var"]})
>>> print(res)
```

```
           Sepal.Length        Sepal.Width          
                    sum   mean         max       var
Species                                             
setosa            250.3  5.006         4.4  0.143690
versicolor        296.8  5.936         3.4  0.098469
virginica         329.4  6.588         3.8  0.104004
```

单变量分组，给定func，字典形式，改名
```python
>>> res = group(iris, by="Species", func={"Sepal.Length": ["sum", "mean"], "Sepal.Width": ["mean", "var"]}, renamedict={"sum": "求和", "mean": ["Length均值", "Width均值"], "var": "方差"})
>>> print(res)
```

```
               求和  Length均值  Width均值        方差
Species                                       
setosa      250.3     5.006    3.428  0.143690
versicolor  296.8     5.936    2.770  0.098469
virginica   329.4     6.588    2.974  0.104004
```

单变量分组，给定func，字典形式，改名
```python
>>> res = group(iris, by="Species", func={"Sepal.Length": "mean", "Sepal.Width": "sum"}, renamedict={"mean": "均值", "sum": "求和"})
>>> print(res)
```

```
               均值     求和
Species                 
setosa      5.006  171.4
versicolor  5.936  138.5
virginica   6.588  148.7
```

单变量分组，给定func，字典形式，改名
```python
>>> res = group(iris, by="Species", func={"Sepal.Length": ["sum", "mean"], "Sepal.Width": "mean"}, renamedict={"sum": "求和", "mean": ["Length均值", "Width均值"]})
>>> print(res)
```

```
               求和  Length均值  Width均值
Species                             
setosa      250.3     5.006    3.428
versicolor  296.8     5.936    2.770
virginica   329.4     6.588    2.974
```

单变量分组，给定func，字典形式，改名
```python
>>> res = group(iris, by="Species", func={"Sepal.Length": "mean", "Sepal.Width": "mean"}, renamedict={"mean": ["Length均值", "Width均值"]})
>>> print(res)
```

```
            Length均值  Width均值
Species                      
setosa         5.006    3.428
versicolor     5.936    2.770
virginica      6.588    2.974
```
