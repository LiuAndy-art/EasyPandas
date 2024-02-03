导入模块
```python
>>> from EasyPandas import read, filter
>>> iris = read("../data/iris.xlsx")
```

DataFrame的筛选

等于筛选
```python
>>> res = filter(iris, "`Sepal.Length` == 4.9")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
1             2           4.9          3.0           1.4          0.2   
9            10           4.9          3.1           1.5          0.1   
34           35           4.9          3.1           1.5          0.2   
37           38           4.9          3.6           1.4          0.1   
57           58           4.9          2.4           3.3          1.0   
106         107           4.9          2.5           4.5          1.7   

        Species  
1        setosa  
9        setosa  
34       setosa  
37       setosa  
57   versicolor  
106   virginica
```

不等于筛选
```python
>>> res = filter(iris, "`Sepal.Length` != 4.9")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0             1           5.1          3.5           1.4          0.2   
2             3           4.7          3.2           1.3          0.2   
3             4           4.6          3.1           1.5          0.2   
4             5           5.0          3.6           1.4          0.2   
5             6           5.4          3.9           1.7          0.4   
..          ...           ...          ...           ...          ...   
145         146           6.7          3.0           5.2          2.3   
146         147           6.3          2.5           5.0          1.9   
147         148           6.5          3.0           5.2          2.0   
148         149           6.2          3.4           5.4          2.3   
149         150           5.9          3.0           5.1          1.8   

       Species  
0       setosa  
2       setosa  
3       setosa  
4       setosa  
5       setosa  
..         ...  
145  virginica  
146  virginica  
147  virginica  
148  virginica  
149  virginica  

[144 rows x 6 columns]
```

大于筛选
```python
>>> res = filter(iris, "`Sepal.Length` > 4.9")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0             1           5.1          3.5           1.4          0.2   
4             5           5.0          3.6           1.4          0.2   
5             6           5.4          3.9           1.7          0.4   
7             8           5.0          3.4           1.5          0.2   
10           11           5.4          3.7           1.5          0.2   
..          ...           ...          ...           ...          ...   
145         146           6.7          3.0           5.2          2.3   
146         147           6.3          2.5           5.0          1.9   
147         148           6.5          3.0           5.2          2.0   
148         149           6.2          3.4           5.4          2.3   
149         150           5.9          3.0           5.1          1.8   

       Species  
0       setosa  
4       setosa  
5       setosa  
7       setosa  
10      setosa  
..         ...  
145  virginica  
146  virginica  
147  virginica  
148  virginica  
149  virginica  

[128 rows x 6 columns]
```

大于等于筛选
```python
>>> res = filter(iris, "`Sepal.Length` >= 4.9")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0             1           5.1          3.5           1.4          0.2   
1             2           4.9          3.0           1.4          0.2   
4             5           5.0          3.6           1.4          0.2   
5             6           5.4          3.9           1.7          0.4   
7             8           5.0          3.4           1.5          0.2   
..          ...           ...          ...           ...          ...   
145         146           6.7          3.0           5.2          2.3   
146         147           6.3          2.5           5.0          1.9   
147         148           6.5          3.0           5.2          2.0   
148         149           6.2          3.4           5.4          2.3   
149         150           5.9          3.0           5.1          1.8   

       Species  
0       setosa  
1       setosa  
4       setosa  
5       setosa  
7       setosa  
..         ...  
145  virginica  
146  virginica  
147  virginica  
148  virginica  
149  virginica  

[134 rows x 6 columns]
```

小于筛选
```python
>>> res = filter(iris, "`Sepal.Length` < 4.9")
>>> print(res)
```

```
    Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
2            3           4.7          3.2           1.3          0.2  setosa
3            4           4.6          3.1           1.5          0.2  setosa
6            7           4.6          3.4           1.4          0.3  setosa
8            9           4.4          2.9           1.4          0.2  setosa
11          12           4.8          3.4           1.6          0.2  setosa
12          13           4.8          3.0           1.4          0.1  setosa
13          14           4.3          3.0           1.1          0.1  setosa
22          23           4.6          3.6           1.0          0.2  setosa
24          25           4.8          3.4           1.9          0.2  setosa
29          30           4.7          3.2           1.6          0.2  setosa
30          31           4.8          3.1           1.6          0.2  setosa
38          39           4.4          3.0           1.3          0.2  setosa
41          42           4.5          2.3           1.3          0.3  setosa
42          43           4.4          3.2           1.3          0.2  setosa
45          46           4.8          3.0           1.4          0.3  setosa
47          48           4.6          3.2           1.4          0.2  setosa
```

小于等于筛选
```python
>>> res = filter(iris, "`Sepal.Length` <= 4.9")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
1             2           4.9          3.0           1.4          0.2   
2             3           4.7          3.2           1.3          0.2   
3             4           4.6          3.1           1.5          0.2   
6             7           4.6          3.4           1.4          0.3   
8             9           4.4          2.9           1.4          0.2   
9            10           4.9          3.1           1.5          0.1   
11           12           4.8          3.4           1.6          0.2   
12           13           4.8          3.0           1.4          0.1   
13           14           4.3          3.0           1.1          0.1   
22           23           4.6          3.6           1.0          0.2   
24           25           4.8          3.4           1.9          0.2   
29           30           4.7          3.2           1.6          0.2   
30           31           4.8          3.1           1.6          0.2   
34           35           4.9          3.1           1.5          0.2   
37           38           4.9          3.6           1.4          0.1   
38           39           4.4          3.0           1.3          0.2   
41           42           4.5          2.3           1.3          0.3   
42           43           4.4          3.2           1.3          0.2   
45           46           4.8          3.0           1.4          0.3   
47           48           4.6          3.2           1.4          0.2   
57           58           4.9          2.4           3.3          1.0   
106         107           4.9          2.5           4.5          1.7   

        Species  
1        setosa  
2        setosa  
3        setosa  
6        setosa  
8        setosa  
9        setosa  
11       setosa  
12       setosa  
13       setosa  
22       setosa  
24       setosa  
29       setosa  
30       setosa  
34       setosa  
37       setosa  
38       setosa  
41       setosa  
42       setosa  
45       setosa  
47       setosa  
57   versicolor  
106   virginica
```

字符串等于筛选
```python
>>> res = filter(iris, "`Species` == 'setosa'")
>>> print(res)
```

```
    Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0            1           5.1          3.5           1.4          0.2  setosa
1            2           4.9          3.0           1.4          0.2  setosa
2            3           4.7          3.2           1.3          0.2  setosa
3            4           4.6          3.1           1.5          0.2  setosa
4            5           5.0          3.6           1.4          0.2  setosa
5            6           5.4          3.9           1.7          0.4  setosa
6            7           4.6          3.4           1.4          0.3  setosa
7            8           5.0          3.4           1.5          0.2  setosa
8            9           4.4          2.9           1.4          0.2  setosa
9           10           4.9          3.1           1.5          0.1  setosa
10          11           5.4          3.7           1.5          0.2  setosa
11          12           4.8          3.4           1.6          0.2  setosa
12          13           4.8          3.0           1.4          0.1  setosa
13          14           4.3          3.0           1.1          0.1  setosa
14          15           5.8          4.0           1.2          0.2  setosa
15          16           5.7          4.4           1.5          0.4  setosa
16          17           5.4          3.9           1.3          0.4  setosa
17          18           5.1          3.5           1.4          0.3  setosa
18          19           5.7          3.8           1.7          0.3  setosa
19          20           5.1          3.8           1.5          0.3  setosa
20          21           5.4          3.4           1.7          0.2  setosa
21          22           5.1          3.7           1.5          0.4  setosa
22          23           4.6          3.6           1.0          0.2  setosa
23          24           5.1          3.3           1.7          0.5  setosa
24          25           4.8          3.4           1.9          0.2  setosa
25          26           5.0          3.0           1.6          0.2  setosa
26          27           5.0          3.4           1.6          0.4  setosa
27          28           5.2          3.5           1.5          0.2  setosa
28          29           5.2          3.4           1.4          0.2  setosa
29          30           4.7          3.2           1.6          0.2  setosa
30          31           4.8          3.1           1.6          0.2  setosa
31          32           5.4          3.4           1.5          0.4  setosa
32          33           5.2          4.1           1.5          0.1  setosa
33          34           5.5          4.2           1.4          0.2  setosa
34          35           4.9          3.1           1.5          0.2  setosa
35          36           5.0          3.2           1.2          0.2  setosa
36          37           5.5          3.5           1.3          0.2  setosa
37          38           4.9          3.6           1.4          0.1  setosa
38          39           4.4          3.0           1.3          0.2  setosa
39          40           5.1          3.4           1.5          0.2  setosa
40          41           5.0          3.5           1.3          0.3  setosa
41          42           4.5          2.3           1.3          0.3  setosa
42          43           4.4          3.2           1.3          0.2  setosa
43          44           5.0          3.5           1.6          0.6  setosa
44          45           5.1          3.8           1.9          0.4  setosa
45          46           4.8          3.0           1.4          0.3  setosa
46          47           5.1          3.8           1.6          0.2  setosa
47          48           4.6          3.2           1.4          0.2  setosa
48          49           5.3          3.7           1.5          0.2  setosa
49          50           5.0          3.3           1.4          0.2  setosa
```

字符串不等于筛选
```python
>>> res = filter(iris, "`Species` != 'setosa'")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
50           51           7.0          3.2           4.7          1.4   
51           52           6.4          3.2           4.5          1.5   
52           53           6.9          3.1           4.9          1.5   
53           54           5.5          2.3           4.0          1.3   
54           55           6.5          2.8           4.6          1.5   
..          ...           ...          ...           ...          ...   
145         146           6.7          3.0           5.2          2.3   
146         147           6.3          2.5           5.0          1.9   
147         148           6.5          3.0           5.2          2.0   
148         149           6.2          3.4           5.4          2.3   
149         150           5.9          3.0           5.1          1.8   

        Species  
50   versicolor  
51   versicolor  
52   versicolor  
53   versicolor  
54   versicolor  
..          ...  
145   virginica  
146   virginica  
147   virginica  
148   virginica  
149   virginica  

[100 rows x 6 columns]
```

字符串包含筛选
```python
>>> res = filter(iris, "`Species` ^C$ 'v'")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
50           51           7.0          3.2           4.7          1.4   
51           52           6.4          3.2           4.5          1.5   
52           53           6.9          3.1           4.9          1.5   
53           54           5.5          2.3           4.0          1.3   
54           55           6.5          2.8           4.6          1.5   
..          ...           ...          ...           ...          ...   
145         146           6.7          3.0           5.2          2.3   
146         147           6.3          2.5           5.0          1.9   
147         148           6.5          3.0           5.2          2.0   
148         149           6.2          3.4           5.4          2.3   
149         150           5.9          3.0           5.1          1.8   

        Species  
50   versicolor  
51   versicolor  
52   versicolor  
53   versicolor  
54   versicolor  
..          ...  
145   virginica  
146   virginica  
147   virginica  
148   virginica  
149   virginica  

[100 rows x 6 columns]
```

字符串不包含筛选
```python
>>> res = filter(iris, "`Species` !^C$ 'v'")
>>> print(res)
```

```
    Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0            1           5.1          3.5           1.4          0.2  setosa
1            2           4.9          3.0           1.4          0.2  setosa
2            3           4.7          3.2           1.3          0.2  setosa
3            4           4.6          3.1           1.5          0.2  setosa
4            5           5.0          3.6           1.4          0.2  setosa
5            6           5.4          3.9           1.7          0.4  setosa
6            7           4.6          3.4           1.4          0.3  setosa
7            8           5.0          3.4           1.5          0.2  setosa
8            9           4.4          2.9           1.4          0.2  setosa
9           10           4.9          3.1           1.5          0.1  setosa
10          11           5.4          3.7           1.5          0.2  setosa
11          12           4.8          3.4           1.6          0.2  setosa
12          13           4.8          3.0           1.4          0.1  setosa
13          14           4.3          3.0           1.1          0.1  setosa
14          15           5.8          4.0           1.2          0.2  setosa
15          16           5.7          4.4           1.5          0.4  setosa
16          17           5.4          3.9           1.3          0.4  setosa
17          18           5.1          3.5           1.4          0.3  setosa
18          19           5.7          3.8           1.7          0.3  setosa
19          20           5.1          3.8           1.5          0.3  setosa
20          21           5.4          3.4           1.7          0.2  setosa
21          22           5.1          3.7           1.5          0.4  setosa
22          23           4.6          3.6           1.0          0.2  setosa
23          24           5.1          3.3           1.7          0.5  setosa
24          25           4.8          3.4           1.9          0.2  setosa
25          26           5.0          3.0           1.6          0.2  setosa
26          27           5.0          3.4           1.6          0.4  setosa
27          28           5.2          3.5           1.5          0.2  setosa
28          29           5.2          3.4           1.4          0.2  setosa
29          30           4.7          3.2           1.6          0.2  setosa
30          31           4.8          3.1           1.6          0.2  setosa
31          32           5.4          3.4           1.5          0.4  setosa
32          33           5.2          4.1           1.5          0.1  setosa
33          34           5.5          4.2           1.4          0.2  setosa
34          35           4.9          3.1           1.5          0.2  setosa
35          36           5.0          3.2           1.2          0.2  setosa
36          37           5.5          3.5           1.3          0.2  setosa
37          38           4.9          3.6           1.4          0.1  setosa
38          39           4.4          3.0           1.3          0.2  setosa
39          40           5.1          3.4           1.5          0.2  setosa
40          41           5.0          3.5           1.3          0.3  setosa
41          42           4.5          2.3           1.3          0.3  setosa
42          43           4.4          3.2           1.3          0.2  setosa
43          44           5.0          3.5           1.6          0.6  setosa
44          45           5.1          3.8           1.9          0.4  setosa
45          46           4.8          3.0           1.4          0.3  setosa
46          47           5.1          3.8           1.6          0.2  setosa
47          48           4.6          3.2           1.4          0.2  setosa
48          49           5.3          3.7           1.5          0.2  setosa
49          50           5.0          3.3           1.4          0.2  setosa
```

字符串开始为
```python
>>> res = filter(iris, "`Species` ^^ 'set'")
>>> print(res)
```

```
    Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0            1           5.1          3.5           1.4          0.2  setosa
1            2           4.9          3.0           1.4          0.2  setosa
2            3           4.7          3.2           1.3          0.2  setosa
3            4           4.6          3.1           1.5          0.2  setosa
4            5           5.0          3.6           1.4          0.2  setosa
5            6           5.4          3.9           1.7          0.4  setosa
6            7           4.6          3.4           1.4          0.3  setosa
7            8           5.0          3.4           1.5          0.2  setosa
8            9           4.4          2.9           1.4          0.2  setosa
9           10           4.9          3.1           1.5          0.1  setosa
10          11           5.4          3.7           1.5          0.2  setosa
11          12           4.8          3.4           1.6          0.2  setosa
12          13           4.8          3.0           1.4          0.1  setosa
13          14           4.3          3.0           1.1          0.1  setosa
14          15           5.8          4.0           1.2          0.2  setosa
15          16           5.7          4.4           1.5          0.4  setosa
16          17           5.4          3.9           1.3          0.4  setosa
17          18           5.1          3.5           1.4          0.3  setosa
18          19           5.7          3.8           1.7          0.3  setosa
19          20           5.1          3.8           1.5          0.3  setosa
20          21           5.4          3.4           1.7          0.2  setosa
21          22           5.1          3.7           1.5          0.4  setosa
22          23           4.6          3.6           1.0          0.2  setosa
23          24           5.1          3.3           1.7          0.5  setosa
24          25           4.8          3.4           1.9          0.2  setosa
25          26           5.0          3.0           1.6          0.2  setosa
26          27           5.0          3.4           1.6          0.4  setosa
27          28           5.2          3.5           1.5          0.2  setosa
28          29           5.2          3.4           1.4          0.2  setosa
29          30           4.7          3.2           1.6          0.2  setosa
30          31           4.8          3.1           1.6          0.2  setosa
31          32           5.4          3.4           1.5          0.4  setosa
32          33           5.2          4.1           1.5          0.1  setosa
33          34           5.5          4.2           1.4          0.2  setosa
34          35           4.9          3.1           1.5          0.2  setosa
35          36           5.0          3.2           1.2          0.2  setosa
36          37           5.5          3.5           1.3          0.2  setosa
37          38           4.9          3.6           1.4          0.1  setosa
38          39           4.4          3.0           1.3          0.2  setosa
39          40           5.1          3.4           1.5          0.2  setosa
40          41           5.0          3.5           1.3          0.3  setosa
41          42           4.5          2.3           1.3          0.3  setosa
42          43           4.4          3.2           1.3          0.2  setosa
43          44           5.0          3.5           1.6          0.6  setosa
44          45           5.1          3.8           1.9          0.4  setosa
45          46           4.8          3.0           1.4          0.3  setosa
46          47           5.1          3.8           1.6          0.2  setosa
47          48           4.6          3.2           1.4          0.2  setosa
48          49           5.3          3.7           1.5          0.2  setosa
49          50           5.0          3.3           1.4          0.2  setosa
```

字符串结束为
```python
>>> res = filter(iris, "`Species` $$ 'color'")
>>> print(res)
```

```
    Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
50          51           7.0          3.2           4.7          1.4   
51          52           6.4          3.2           4.5          1.5   
52          53           6.9          3.1           4.9          1.5   
53          54           5.5          2.3           4.0          1.3   
54          55           6.5          2.8           4.6          1.5   
55          56           5.7          2.8           4.5          1.3   
56          57           6.3          3.3           4.7          1.6   
57          58           4.9          2.4           3.3          1.0   
58          59           6.6          2.9           4.6          1.3   
59          60           5.2          2.7           3.9          1.4   
60          61           5.0          2.0           3.5          1.0   
61          62           5.9          3.0           4.2          1.5   
62          63           6.0          2.2           4.0          1.0   
63          64           6.1          2.9           4.7          1.4   
64          65           5.6          2.9           3.6          1.3   
65          66           6.7          3.1           4.4          1.4   
66          67           5.6          3.0           4.5          1.5   
67          68           5.8          2.7           4.1          1.0   
68          69           6.2          2.2           4.5          1.5   
69          70           5.6          2.5           3.9          1.1   
70          71           5.9          3.2           4.8          1.8   
71          72           6.1          2.8           4.0          1.3   
72          73           6.3          2.5           4.9          1.5   
73          74           6.1          2.8           4.7          1.2   
74          75           6.4          2.9           4.3          1.3   
75          76           6.6          3.0           4.4          1.4   
76          77           6.8          2.8           4.8          1.4   
77          78           6.7          3.0           5.0          1.7   
78          79           6.0          2.9           4.5          1.5   
79          80           5.7          2.6           3.5          1.0   
80          81           5.5          2.4           3.8          1.1   
81          82           5.5          2.4           3.7          1.0   
82          83           5.8          2.7           3.9          1.2   
83          84           6.0          2.7           5.1          1.6   
84          85           5.4          3.0           4.5          1.5   
85          86           6.0          3.4           4.5          1.6   
86          87           6.7          3.1           4.7          1.5   
87          88           6.3          2.3           4.4          1.3   
88          89           5.6          3.0           4.1          1.3   
89          90           5.5          2.5           4.0          1.3   
90          91           5.5          2.6           4.4          1.2   
91          92           6.1          3.0           4.6          1.4   
92          93           5.8          2.6           4.0          1.2   
93          94           5.0          2.3           3.3          1.0   
94          95           5.6          2.7           4.2          1.3   
95          96           5.7          3.0           4.2          1.2   
96          97           5.7          2.9           4.2          1.3   
97          98           6.2          2.9           4.3          1.3   
98          99           5.1          2.5           3.0          1.1   
99         100           5.7          2.8           4.1          1.3   

       Species  
50  versicolor  
51  versicolor  
52  versicolor  
53  versicolor  
54  versicolor  
55  versicolor  
56  versicolor  
57  versicolor  
58  versicolor  
59  versicolor  
60  versicolor  
61  versicolor  
62  versicolor  
63  versicolor  
64  versicolor  
65  versicolor  
66  versicolor  
67  versicolor  
68  versicolor  
69  versicolor  
70  versicolor  
71  versicolor  
72  versicolor  
73  versicolor  
74  versicolor  
75  versicolor  
76  versicolor  
77  versicolor  
78  versicolor  
79  versicolor  
80  versicolor  
81  versicolor  
82  versicolor  
83  versicolor  
84  versicolor  
85  versicolor  
86  versicolor  
87  versicolor  
88  versicolor  
89  versicolor  
90  versicolor  
91  versicolor  
92  versicolor  
93  versicolor  
94  versicolor  
95  versicolor  
96  versicolor  
97  versicolor  
98  versicolor  
99  versicolor
```

列之间的大于比较
```python
>>> res = filter(iris, "`Sepal.Length` > `Petal.Length`")
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

[150 rows x 6 columns]
```

列之间的大于等于比较
```python
>>> res = filter(iris, "`Sepal.Width` > `Petal.Width`")
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

[150 rows x 6 columns]
```

列之间的小于比较
```python
>>> res = filter(iris, "`Sepal.Width` < `Petal.Width`")
>>> print(res)
```

```
Empty DataFrame
Columns: [Unnamed: 0, Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, Species]
Index: []
```

列之间的小于等于比较
```python
>>> res = filter(iris, "`Sepal.Length` <= `Petal.Length`")
>>> print(res)
```

```
Empty DataFrame
Columns: [Unnamed: 0, Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, Species]
Index: []
```

列之间的等于比较
```python
>>> res = filter(iris, "`Sepal.Length` == `Petal.Length`")
>>> print(res)
```

```
Empty DataFrame
Columns: [Unnamed: 0, Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, Species]
Index: []
```

列之间的不等于比较
```python
>>> res = filter(iris, "`Sepal.Width` != `Petal.Width`")
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

[150 rows x 6 columns]
```

多个筛选条件
```python
>>> res = filter(iris, "`Sepal.Length` >= 5", "`Sepal.Length` <= 4.5", "and")
>>> print(res)
>>> res = filter(iris, "`Sepal.Length` >= 5", "`Sepal.Length` <= 4.5", "or")
>>> print(res)
>>> res = filter(iris, "`Sepal.Length` >= 5", "`Sepal.Length` <= 4.5", None)
>>> print(res)
>>> res = filter(iris, "`Species` ^C$ 'color'", "`Species` ^C$ 'set'", "or")
>>> print(res)
>>> res = filter(iris, "`Species` ^C$ 'color'", "`Sepal.Length` > 5", "and")
>>> print(res)
```

```
Empty DataFrame
Columns: [Unnamed: 0, Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, Species]
Index: []
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0             1           5.1          3.5           1.4          0.2   
4             5           5.0          3.6           1.4          0.2   
5             6           5.4          3.9           1.7          0.4   
7             8           5.0          3.4           1.5          0.2   
8             9           4.4          2.9           1.4          0.2   
..          ...           ...          ...           ...          ...   
145         146           6.7          3.0           5.2          2.3   
146         147           6.3          2.5           5.0          1.9   
147         148           6.5          3.0           5.2          2.0   
148         149           6.2          3.4           5.4          2.3   
149         150           5.9          3.0           5.1          1.8   

       Species  
0       setosa  
4       setosa  
5       setosa  
7       setosa  
8       setosa  
..         ...  
145  virginica  
146  virginica  
147  virginica  
148  virginica  
149  virginica  

[133 rows x 6 columns]
请给出条件之间的关系！
None
    Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
0            1           5.1          3.5           1.4          0.2   
1            2           4.9          3.0           1.4          0.2   
2            3           4.7          3.2           1.3          0.2   
3            4           4.6          3.1           1.5          0.2   
4            5           5.0          3.6           1.4          0.2   
..         ...           ...          ...           ...          ...   
95          96           5.7          3.0           4.2          1.2   
96          97           5.7          2.9           4.2          1.3   
97          98           6.2          2.9           4.3          1.3   
98          99           5.1          2.5           3.0          1.1   
99         100           5.7          2.8           4.1          1.3   

       Species  
0       setosa  
1       setosa  
2       setosa  
3       setosa  
4       setosa  
..         ...  
95  versicolor  
96  versicolor  
97  versicolor  
98  versicolor  
99  versicolor  

[100 rows x 6 columns]
    Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  \
50          51           7.0          3.2           4.7          1.4   
51          52           6.4          3.2           4.5          1.5   
52          53           6.9          3.1           4.9          1.5   
53          54           5.5          2.3           4.0          1.3   
54          55           6.5          2.8           4.6          1.5   
55          56           5.7          2.8           4.5          1.3   
56          57           6.3          3.3           4.7          1.6   
58          59           6.6          2.9           4.6          1.3   
59          60           5.2          2.7           3.9          1.4   
61          62           5.9          3.0           4.2          1.5   
62          63           6.0          2.2           4.0          1.0   
63          64           6.1          2.9           4.7          1.4   
64          65           5.6          2.9           3.6          1.3   
65          66           6.7          3.1           4.4          1.4   
66          67           5.6          3.0           4.5          1.5   
67          68           5.8          2.7           4.1          1.0   
68          69           6.2          2.2           4.5          1.5   
69          70           5.6          2.5           3.9          1.1   
70          71           5.9          3.2           4.8          1.8   
71          72           6.1          2.8           4.0          1.3   
72          73           6.3          2.5           4.9          1.5   
73          74           6.1          2.8           4.7          1.2   
74          75           6.4          2.9           4.3          1.3   
75          76           6.6          3.0           4.4          1.4   
76          77           6.8          2.8           4.8          1.4   
77          78           6.7          3.0           5.0          1.7   
78          79           6.0          2.9           4.5          1.5   
79          80           5.7          2.6           3.5          1.0   
80          81           5.5          2.4           3.8          1.1   
81          82           5.5          2.4           3.7          1.0   
82          83           5.8          2.7           3.9          1.2   
83          84           6.0          2.7           5.1          1.6   
84          85           5.4          3.0           4.5          1.5   
85          86           6.0          3.4           4.5          1.6   
86          87           6.7          3.1           4.7          1.5   
87          88           6.3          2.3           4.4          1.3   
88          89           5.6          3.0           4.1          1.3   
89          90           5.5          2.5           4.0          1.3   
90          91           5.5          2.6           4.4          1.2   
91          92           6.1          3.0           4.6          1.4   
92          93           5.8          2.6           4.0          1.2   
94          95           5.6          2.7           4.2          1.3   
95          96           5.7          3.0           4.2          1.2   
96          97           5.7          2.9           4.2          1.3   
97          98           6.2          2.9           4.3          1.3   
98          99           5.1          2.5           3.0          1.1   
99         100           5.7          2.8           4.1          1.3   

       Species  
50  versicolor  
51  versicolor  
52  versicolor  
53  versicolor  
54  versicolor  
55  versicolor  
56  versicolor  
58  versicolor  
59  versicolor  
61  versicolor  
62  versicolor  
63  versicolor  
64  versicolor  
65  versicolor  
66  versicolor  
67  versicolor  
68  versicolor  
69  versicolor  
70  versicolor  
71  versicolor  
72  versicolor  
73  versicolor  
74  versicolor  
75  versicolor  
76  versicolor  
77  versicolor  
78  versicolor  
79  versicolor  
80  versicolor  
81  versicolor  
82  versicolor  
83  versicolor  
84  versicolor  
85  versicolor  
86  versicolor  
87  versicolor  
88  versicolor  
89  versicolor  
90  versicolor  
91  versicolor  
92  versicolor  
94  versicolor  
95  versicolor  
96  versicolor  
97  versicolor  
98  versicolor  
99  versicolor
```

测试Series

等于筛选
```python
>>> res = filter(iris["Sepal.Length"], "== 4.9")
>>> print(res)
```

```
1      4.9
9      4.9
34     4.9
37     4.9
57     4.9
106    4.9
Name: Sepal.Length, dtype: float64
```

不等于筛选
```python
>>> res = filter(iris["Sepal.Length"], "!= 4.9")
>>> print(res)
```

```
0      5.1
2      4.7
3      4.6
4      5.0
5      5.4
      ... 
145    6.7
146    6.3
147    6.5
148    6.2
149    5.9
Name: Sepal.Length, Length: 144, dtype: float64
```

大于筛选
```python
>>> res = filter(iris["Sepal.Length"], "> 4.9")
>>> print(res)
```

```
0      5.1
4      5.0
5      5.4
7      5.0
10     5.4
      ... 
145    6.7
146    6.3
147    6.5
148    6.2
149    5.9
Name: Sepal.Length, Length: 128, dtype: float64
```

大于等于筛选
```python
>>> res = filter(iris["Sepal.Length"], ">= 4.9")
>>> print(res)
```

```
0      5.1
1      4.9
4      5.0
5      5.4
7      5.0
      ... 
145    6.7
146    6.3
147    6.5
148    6.2
149    5.9
Name: Sepal.Length, Length: 134, dtype: float64
```

小于筛选
```python
>>> res = filter(iris["Sepal.Length"], "< 4.9")
>>> print(res)
```

```
2     4.7
3     4.6
6     4.6
8     4.4
11    4.8
12    4.8
13    4.3
22    4.6
24    4.8
29    4.7
30    4.8
38    4.4
41    4.5
42    4.4
45    4.8
47    4.6
Name: Sepal.Length, dtype: float64
```

小于等于筛选
```python
>>> res = filter(iris["Sepal.Length"], "<= 4.9")
>>> print(res)
```

```
1      4.9
2      4.7
3      4.6
6      4.6
8      4.4
9      4.9
11     4.8
12     4.8
13     4.3
22     4.6
24     4.8
29     4.7
30     4.8
34     4.9
37     4.9
38     4.4
41     4.5
42     4.4
45     4.8
47     4.6
57     4.9
106    4.9
Name: Sepal.Length, dtype: float64
```

字符串等于筛选
```python
>>> res = filter(iris["Species"], "== 'setosa'")
>>> print(res)
```

```
0     setosa
1     setosa
2     setosa
3     setosa
4     setosa
5     setosa
6     setosa
7     setosa
8     setosa
9     setosa
10    setosa
11    setosa
12    setosa
13    setosa
14    setosa
15    setosa
16    setosa
17    setosa
18    setosa
19    setosa
20    setosa
21    setosa
22    setosa
23    setosa
24    setosa
25    setosa
26    setosa
27    setosa
28    setosa
29    setosa
30    setosa
31    setosa
32    setosa
33    setosa
34    setosa
35    setosa
36    setosa
37    setosa
38    setosa
39    setosa
40    setosa
41    setosa
42    setosa
43    setosa
44    setosa
45    setosa
46    setosa
47    setosa
48    setosa
49    setosa
Name: Species, dtype: object
```

字符串不等于筛选
```python
>>> res = filter(iris["Species"], "!='setosa'")
>>> print(res)
```

```
50     versicolor
51     versicolor
52     versicolor
53     versicolor
54     versicolor
          ...    
145     virginica
146     virginica
147     virginica
148     virginica
149     virginica
Name: Species, Length: 100, dtype: object
```

字符串包含筛选
```python
>>> res = filter(iris["Species"], "^C$ 'v'")
>>> print(res)
```

```
50     versicolor
51     versicolor
52     versicolor
53     versicolor
54     versicolor
          ...    
145     virginica
146     virginica
147     virginica
148     virginica
149     virginica
Name: Species, Length: 100, dtype: object
```

字符串不包含筛选
```python
>>> res = filter(iris["Species"], "!^C$ 'v'")
>>> print(res)
```

```
0     setosa
1     setosa
2     setosa
3     setosa
4     setosa
5     setosa
6     setosa
7     setosa
8     setosa
9     setosa
10    setosa
11    setosa
12    setosa
13    setosa
14    setosa
15    setosa
16    setosa
17    setosa
18    setosa
19    setosa
20    setosa
21    setosa
22    setosa
23    setosa
24    setosa
25    setosa
26    setosa
27    setosa
28    setosa
29    setosa
30    setosa
31    setosa
32    setosa
33    setosa
34    setosa
35    setosa
36    setosa
37    setosa
38    setosa
39    setosa
40    setosa
41    setosa
42    setosa
43    setosa
44    setosa
45    setosa
46    setosa
47    setosa
48    setosa
49    setosa
Name: Species, dtype: object
```

字符串开始为
```python
>>> res = filter(iris["Species"], "^^ 'set'")
>>> print(res)
```

```
0     setosa
1     setosa
2     setosa
3     setosa
4     setosa
5     setosa
6     setosa
7     setosa
8     setosa
9     setosa
10    setosa
11    setosa
12    setosa
13    setosa
14    setosa
15    setosa
16    setosa
17    setosa
18    setosa
19    setosa
20    setosa
21    setosa
22    setosa
23    setosa
24    setosa
25    setosa
26    setosa
27    setosa
28    setosa
29    setosa
30    setosa
31    setosa
32    setosa
33    setosa
34    setosa
35    setosa
36    setosa
37    setosa
38    setosa
39    setosa
40    setosa
41    setosa
42    setosa
43    setosa
44    setosa
45    setosa
46    setosa
47    setosa
48    setosa
49    setosa
Name: Species, dtype: object
```

字符串结束为
```python
>>> res = filter(iris["Species"], "$$ 'color'")
>>> print(res)
```

```
50    versicolor
51    versicolor
52    versicolor
53    versicolor
54    versicolor
55    versicolor
56    versicolor
57    versicolor
58    versicolor
59    versicolor
60    versicolor
61    versicolor
62    versicolor
63    versicolor
64    versicolor
65    versicolor
66    versicolor
67    versicolor
68    versicolor
69    versicolor
70    versicolor
71    versicolor
72    versicolor
73    versicolor
74    versicolor
75    versicolor
76    versicolor
77    versicolor
78    versicolor
79    versicolor
80    versicolor
81    versicolor
82    versicolor
83    versicolor
84    versicolor
85    versicolor
86    versicolor
87    versicolor
88    versicolor
89    versicolor
90    versicolor
91    versicolor
92    versicolor
93    versicolor
94    versicolor
95    versicolor
96    versicolor
97    versicolor
98    versicolor
99    versicolor
Name: Species, dtype: object
```

对于一个一般的Series

```python
>>> s = pd.Series([i for i in range(100)])
>>> res = filter(s, ">90")
>>> print(res)
```

```
91    91
92    92
93    93
94    94
95    95
96    96
97    97
98    98
99    99
Name: Name, dtype: int64
```

```python
s = pd.Series([i for i in range(100)])
res = filter(s, "in [90, 99]")
print(res)
```

```
90    90
99    99
Name: Name, dtype: int64
```

```python
s = pd.Series([i for i in range(100)])
res = filter(s, "not in [90, 99]")
print(res)
```

```
0      0
1      1
2      2
3      3
4      4
      ..
94    94
95    95
96    96
97    97
98    98
Name: Name, Length: 98, dtype: int64
```
