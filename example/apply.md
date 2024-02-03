导入模块
```python
>>> from EasyPandas import read, apply
>>> iris = read("../data/iris.xlsx")
>>> sepal_length = iris["Sepal.Length"]
```

测试Series参数，applytowhat为obj，func为str=any
```python
>>> res = apply(sepal_length, "any")
>>> print(res)
```

```
True
```

测试Series参数，applytowhat为obj，func为str=all
```python
>>> res = apply(sepal_length, "all")
>>> print(res)
```

```
True
```

测试Series参数，applytowhat为obj，func为str=count
```python
>>> res = apply(sepal_length, "count")
>>> print(res)
```

```
150
```

测试Series参数，applytowhat为obj，func为str=idxmax
```python
>>> res = apply(sepal_length, "idxmax")
>>> print(res)
```

```
131
```

测试Series参数，applytowhat为obj，func为str=idxmin
```python
>>> res = apply(sepal_length, "idxmin")
>>> print(res)
```

```
13
```

测试Series参数，applytowhat为obj，func为str=max
```python
>>> res = apply(sepal_length, "max")
>>> print(res)
```

```
7.9
```

测试Series参数，applytowhat为obj，func为str=min
```python
>>> res = apply(sepal_length, "min")
>>> print(res)
```

```
4.3
```

测试Series参数，applytowhat为obj，func为str=mean
```python
>>> res = apply(sepal_length, "mean")
>>> print(res)
```

```5.8433333
```


测试Series参数，applytowhat为obj，func为str=median
```python
>>> res = apply(sepal_length, "median")
>>> print(res)
```

```
5.8
```

测试Series参数，applytowhat为obj，func为str=sum
```python
>>> res = apply(sepal_length, "sum")
>>> print(res)
```

```
8576.5
```

测试Series参数，applytowhat为obj，func为str=nunique
```python
>>> res = apply(sepal_length, "unique")
>>> print(res)
```

```
[5.1 4.9 4.7 4.6 5.  5.4 4.4 4.8 4.3 5.8 5.7 5.2 5.5 4.5 5.3 7. 6.4 6.9 6.5 6.3 6.6 5.9 6.  6.1 5.6 6.7 6.2 6.8 7.1 7.6 7.3 7.2 7.7 7.4 7.9]
```

测试Series参数，applytowhat为obj，func为str=prod
```python
>>> res = apply(sepal_length, "prod")
>>> print(res)
```

```
2.2574399991830563e+114
```

测试Series参数，applytowhat为obj，func为str=quantile
```python
>>> res = apply(sepal_length, "quantile", q=0.9)
>>> print(res)
```

```
6.9
```

测试Series参数，applytowhat为obj，func为str=sem
```python
>>> res = apply(sepal_length, "sem")
>>> print(res)
```

```
0.0676113162275986
```

测试Series参数，applytowhat为obj，func为str=size
```python
>>> res = apply(sepal_length, "size")
>>> print(res)
```

```
150
```

测试Series参数，applytowhat为obj，func为str=skew
```python
>>> res = apply(sepal_length, "skew")
>>> print(res)
```

```
0.3149109566369728
```

测试Series参数，applytowhat为obj，func为str=std
```python
>>> res = apply(sepal_length, "std")
>>> print(res)
```

```
0.828066127977863
```

测试Series参数，applytowhat为obj，func为str=var
```python
>>> res = apply(sepal_length, "var")
>>> print(res)
```

```
0.6856935123042507
```

测试Series参数，applytowhat为obj，func为str=bfill
```python
>>> res = apply(sepal_length, "bfill")
>>> print(res)
```

```
0      5.1
1      4.9
2      4.7
3      4.6
4      5.0
      ... 
145    6.7
146    6.3
147    6.5
148    6.2
149    5.9
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=cumsum
```python
>>> res = apply(sepal_length, "cumsum")
>>> print(res)
```

```
0        5.1
1       10.0
2       14.7
3       19.3
4       24.3
       ...  
145    851.6
146    857.9
147    864.4
148    870.6
149    876.5
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=cumprod
```python
>>> res = apply(sepal_length, "cumprod")
>>> print(res)
```

```
0       5.100000e+00
1       2.499000e+01
2       1.174530e+02
3       5.402838e+02
4       2.701419e+03
           ...      
145    1.507019e+111
146    9.494217e+111
147    6.171241e+112
148    3.826169e+113
149    2.257440e+114
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=cummax
```python
>>> res = apply(sepal_length, "cummax")
>>> print(res)
```

```
0      5.1
1      5.1
2      5.1
3      5.1
4      5.1
      ... 
145    7.9
146    7.9
147    7.9
148    7.9
149    7.9
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=cummin
```python
>>> res = apply(sepal_length, "cummin")
>>> print(res)
```

```
0      5.1
1      4.9
2      4.7
3      4.6
4      4.6
      ... 
145    4.3
146    4.3
147    4.3
148    4.3
149    4.3
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=diff
```python
>>> res = apply(sepal_length, "diff")
>>> print(res)
```

```
0      NaN
1     -0.2
2     -0.2
3     -0.1
4      0.4
      ... 
145    0.0
146   -0.4
147    0.2
148   -0.3
149   -0.3
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=ffill
```python
>>> res = apply(sepal_length, "ffill")
>>> print(res)
```

```
0      5.1
1      4.9
2      4.7
3      4.6
4      5.0
      ... 
145    6.7
146    6.3
147    6.5
148    6.2
149    5.9
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=fillna
```python
>>> res = apply(sepal_length, "fillna", value=100)
>>> print(res)
```

```
0      5.1
1      4.9
2      4.7
3      4.6
4      5.0
      ... 
145    6.7
146    6.3
147    6.5
148    6.2
149    5.9
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=rank
```python
>>> res = apply(sepal_length, "rank")
>>> print(res)
```

```
0       37.0
1       19.5
2       10.5
3        7.5
4       27.5
       ...  
145    126.5
146    104.0
147    118.0
148     97.5
149     82.0
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=shift
```python
>>> res = apply(sepal_length, "shift", periods=1)
>>> print(res)
```

```
0      NaN
1      5.1
2      4.9
3      4.7
4      4.6
      ... 
145    6.7
146    6.7
147    6.3
148    6.5
149    6.2
Name: Sepal.Length, Length: 150, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=head
```python
>>> res = apply(sepal_length, "head")
>>> print(res)
```

```
0    5.1
1    4.9
2    4.7
3    4.6
4    5.0
Name: Sepal.Length, dtype: float64
```

测试Series参数，applytowhat为obj，func为str=tail
```python
>>> res = apply(sepal_length, "tail")
>>> print(res)
```

```
145    6.7
146    6.3
147    6.5
148    6.2
149    5.9
Name: Sepal.Length, dtype: float64
```

测试Series参数，applytowhat为element，func为lambda x: str(x).split(".")[1]
```python
>>> res = apply(sepal_length, lambda x: str(x).split(".")[1], applytowhat="element")
>>> print(res)
```

```
0      1
1      9
2      7
3      6
4      0
      ..
145    7
146    3
147    5
148    2
149    9
Name: Sepal.Length, Length: 150, dtype: object
```

测试DataFrame参数，func为str=any
```python
>>> res = apply(iris, "any")
>>> print(res)
```

```
Unnamed: 0      True
Sepal.Length    True
Sepal.Width     True
Petal.Length    True
Petal.Width     True
Species         True
dtype: bool
```

测试DataFrame参数，func为str=all
```python
>>> res = apply(iris, "all")
>>> print(res)
```

```
Unnamed: 0      True
Sepal.Length    True
Sepal.Width     True
Petal.Length    True
Petal.Width     True
Species         True
dtype: bool
```

测试DataFrame参数，func为str=count
```python
>>> res = apply(iris, "count")
>>> print(res)
```

```
Unnamed: 0      150
Sepal.Length    150
Sepal.Width     150
Petal.Length    150
Petal.Width     150
Species         150
dtype: int64
```

测试DataFrame参数，func为str=idxmax
```python
>>> res = apply(iris, "idxmax")
>>> print(res)
```

```
Unnamed: 0      149
Sepal.Length    131
Sepal.Width      15
Petal.Length    118
Petal.Width     100
Species         100
dtype: int64
```

测试DataFrame参数，func为str=idxmin
```python
>>> res = apply(iris, "idxmin")
>>> print(res)
```

```
Unnamed: 0       0
Sepal.Length    13
Sepal.Width     60
Petal.Length    22
Petal.Width      9
Species          0
dtype: int64
```

测试DataFrame参数，func为str=max
```python
>>> res = apply(iris, "max")
>>> print(res)
```

```
Unnamed: 0            150
Sepal.Length          7.9
Sepal.Width           4.4
Petal.Length          6.9
Petal.Width           2.5
Species         virginica
dtype: object
```

测试DataFrame参数，func为str=min
```python
>>> res = apply(iris, "min")
>>> print(res)
```

```
Unnamed: 0           1
Sepal.Length       4.3
Sepal.Width        2.0
Petal.Length       1.0
Petal.Width        0.1
Species         setosa
dtype: object
```

测试DataFrame参数，func为str=mean
```python
>>> res = apply(iris.iloc[:,:-1], "mean")
>>> print(res)
```

```
Unnamed: 0      75.500000
Sepal.Length     5.843333
Sepal.Width      3.057333
Petal.Length     3.758000
Petal.Width      1.199333
dtype: float64
```

测试DataFrame参数，func为str=median
```python
>>> res = apply(iris.iloc[:,:-1], "median")
>>> print(res)
```

```
Unnamed: 0      75.50
Sepal.Length     5.80
Sepal.Width      3.00
Petal.Length     4.35
Petal.Width      1.30
dtype: float64
```

测试DataFrame参数，func为str=sum
```python
>>> res = apply(iris.iloc[:,:-1], "sum")
>>> print(res)
```

```
Unnamed: 0      11325.0
Sepal.Length      876.5
Sepal.Width       458.6
Petal.Length      563.7
Petal.Width       179.9
dtype: float64
```

测试DataFrame参数，func为str=prod
```python
>>> res = apply(iris.iloc[:,:-1], "prod")
>>> print(res)
```

```
Unnamed: 0       0.000000e+00
Sepal.Length    2.257440e+114
Sepal.Width      1.390618e+72
Petal.Length     3.522857e+76
Petal.Width      5.945429e-12
dtype: float64
```

测试DataFrame参数，func为str=quantile
```python
>>> res = apply(iris.iloc[:,:-1], "quantile", q=0.9)
>>> print(res)
```

```
Unnamed: 0      135.10
Sepal.Length      6.90
Sepal.Width       3.61
Petal.Length      5.80
Petal.Width       2.20
Name: 0.9, dtype: float64
```

测试DataFrame参数，func为str=sem
```python
>>> res = apply(iris.iloc[:,:-1], "sem")
>>> print(res)
```

```
Unnamed: 0      3.547299
Sepal.Length    0.067611
Sepal.Width     0.035588
Petal.Length    0.144136
Petal.Width     0.062236
dtype: float64
```

测试DataFrame参数，func为str=size
```python
>>> res = apply(iris.iloc[:,:-1], "size")
>>> print(res)
```

```
Unnamed: 0      150
Sepal.Length    150
Sepal.Width     150
Petal.Length    150
Petal.Width     150
dtype: int64
```

测试DataFrame参数，func为str=skew
```python
>>> res = apply(iris.iloc[:,:-1], "skew")
>>> print(res)
```

```
Unnamed: 0      0.000000
Sepal.Length    0.314911
Sepal.Width     0.318966
Petal.Length   -0.274884
Petal.Width    -0.102967
dtype: float64
```

测试DataFrame参数，func为str=std
```python
>>> res = apply(iris.iloc[:,:-1], "std")
>>> print(res)
```

```
Unnamed: 0      43.445368
Sepal.Length     0.828066
Sepal.Width      0.435866
Petal.Length     1.765298
Petal.Width      0.762238
dtype: float64
```

测试DataFrame参数，func为str=var
```python
>>> res = apply(iris.iloc[:,:-1], "var")
>>> print(res)
```

```
Unnamed: 0      1887.500000
Sepal.Length       0.685694
Sepal.Width        0.189979
Petal.Length       3.116278
Petal.Width        0.581006
dtype: float64
```

测试DataFrame参数，func为str=bfill
```python
>>> res = apply(iris.iloc[:,:-1], "bfill")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
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

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=cumsum
```python
>>> res = apply(iris.iloc[:,:-1], "cumsum")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0             1           5.1          3.5           1.4          0.2
1             3          10.0          6.5           2.8          0.4
2             6          14.7          9.7           4.1          0.6
3            10          19.3         12.8           5.6          0.8
4            15          24.3         16.4           7.0          1.0
..          ...           ...          ...           ...          ...
145       10731         851.6        446.7         543.0        171.9
146       10878         857.9        449.2         548.0        173.8
147       11026         864.4        452.2         553.2        175.8
148       11175         870.6        455.6         558.6        178.1
149       11325         876.5        458.6         563.7        179.9

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=cumprod
```python
>>> res = apply(iris.iloc[:,:-1], "cumprod")
>>> print(res)
```

```
     Unnamed: 0   Sepal.Length   Sepal.Width  Petal.Length   Petal.Width
0             1   5.100000e+00  3.500000e+00  1.400000e+00  2.000000e-01
1             2   2.499000e+01  1.050000e+01  1.960000e+00  4.000000e-02
2             6   1.174530e+02  3.360000e+01  2.548000e+00  8.000000e-03
3            24   5.402838e+02  1.041600e+02  3.822000e+00  1.600000e-03
4           120   2.701419e+03  3.749760e+02  5.350800e+00  3.200000e-04
..          ...            ...           ...           ...           ...
145           0  1.507019e+111  1.817801e+70  4.919916e+73  3.779194e-13
146           0  9.494217e+111  4.544504e+70  2.459958e+74  7.180469e-13
147           0  6.171241e+112  1.363351e+71  1.279178e+75  1.436094e-12
148           0  3.826169e+113  4.635394e+71  6.907562e+75  3.303016e-12
149           0  2.257440e+114  1.390618e+72  3.522857e+76  5.945429e-12

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=cummax
```python
>>> res = apply(iris.iloc[:,:-1], "cummax")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0             1           5.1          3.5           1.4          0.2
1             2           5.1          3.5           1.4          0.2
2             3           5.1          3.5           1.4          0.2
3             4           5.1          3.5           1.5          0.2
4             5           5.1          3.6           1.5          0.2
..          ...           ...          ...           ...          ...
145         146           7.9          4.4           6.9          2.5
146         147           7.9          4.4           6.9          2.5
147         148           7.9          4.4           6.9          2.5
148         149           7.9          4.4           6.9          2.5
149         150           7.9          4.4           6.9          2.5

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=cummin
```python
>>> res = apply(iris.iloc[:,:-1], "cummin", axis=1)
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0           1.0           1.0          1.0           1.0          0.2
1           2.0           2.0          2.0           1.4          0.2
2           3.0           3.0          3.0           1.3          0.2
3           4.0           4.0          3.1           1.5          0.2
4           5.0           5.0          3.6           1.4          0.2
..          ...           ...          ...           ...          ...
145       146.0           6.7          3.0           3.0          2.3
146       147.0           6.3          2.5           2.5          1.9
147       148.0           6.5          3.0           3.0          2.0
148       149.0           6.2          3.4           3.4          2.3
149       150.0           5.9          3.0           3.0          1.8

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=diff
```python
>>> res = apply(iris.iloc[:,:-1], "diff", axis=1)
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0           NaN           4.1         -1.6          -2.1         -1.2
1           NaN           2.9         -1.9          -1.6         -1.2
2           NaN           1.7         -1.5          -1.9         -1.1
3           NaN           0.6         -1.5          -1.6         -1.3
4           NaN           0.0         -1.4          -2.2         -1.2
..          ...           ...          ...           ...          ...
145         NaN        -139.3         -3.7           2.2         -2.9
146         NaN        -140.7         -3.8           2.5         -3.1
147         NaN        -141.5         -3.5           2.2         -3.2
148         NaN        -142.8         -2.8           2.0         -3.1
149         NaN        -144.1         -2.9           2.1         -3.3

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=ffill
```python
>>> res = apply(iris.iloc[:,:-1], "ffill")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
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

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=fillna
```python
>>> res = apply(iris.iloc[:,:-1], "fillna", value=100)
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
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

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=rank
```python
>>> res = apply(iris.iloc[:,:-1], "rank")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0           1.0          37.0        128.5          18.0         20.0
1           2.0          19.5         70.5          18.0         20.0
2           3.0          10.5        101.0           8.0         20.0
3           4.0           7.5         89.0          31.0         20.0
4           5.0          27.5        133.5          18.0         20.0
..          ...           ...          ...           ...          ...
145       146.0         126.5         70.5         117.5        140.5
146       147.0         104.0         15.5         106.5        119.0
147       148.0         118.0         70.5         117.5        124.5
148       149.0          97.5        119.5         121.5        140.5
149       150.0          82.0         70.5         112.5        110.5

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=shift
```python
>>> res = apply(iris.iloc[:,:-1], "shift", periods=1)
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0           NaN           NaN          NaN           NaN          NaN
1           1.0           5.1          3.5           1.4          0.2
2           2.0           4.9          3.0           1.4          0.2
3           3.0           4.7          3.2           1.3          0.2
4           4.0           4.6          3.1           1.5          0.2
..          ...           ...          ...           ...          ...
145       145.0           6.7          3.3           5.7          2.5
146       146.0           6.7          3.0           5.2          2.3
147       147.0           6.3          2.5           5.0          1.9
148       148.0           6.5          3.0           5.2          2.0
149       149.0           6.2          3.4           5.4          2.3

[150 rows x 5 columns]
```

测试DataFrame参数，func为str=head
```python
>>> res = apply(iris.iloc[:,:-1], "head")
>>> print(res)
```

```
  Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0           1           5.1          3.5           1.4          0.2
1           2           4.9          3.0           1.4          0.2
2           3           4.7          3.2           1.3          0.2
3           4           4.6          3.1           1.5          0.2
4           5           5.0          3.6           1.4          0.2
```

测试DataFrame参数，func为str=tail
```python
>>> res = apply(iris.iloc[:,:-1], "tail")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
145         146           6.7          3.0           5.2          2.3
146         147           6.3          2.5           5.0          1.9
147         148           6.5          3.0           5.2          2.0
148         149           6.2          3.4           5.4          2.3
149         150           5.9          3.0           5.1          1.8
```

测试DataFrame参数，func为str=tail
```python
>>> res = apply(iris.iloc[:,:-1], "tail")
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
145         146           6.7          3.0           5.2          2.3
146         147           6.3          2.5           5.0          1.9
147         148           6.5          3.0           5.2          2.0
148         149           6.2          3.4           5.4          2.3
149         150           5.9          3.0           5.1          1.8

```

测试DataFrame参数，func为自定义函数
```python
>>> res = apply(iris.iloc[:,:-1], lambda x: x+1)
>>> print(res)
```

```
     Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0             2           6.1          4.5           2.4          1.2
1             3           5.9          4.0           2.4          1.2
2             4           5.7          4.2           2.3          1.2
3             5           5.6          4.1           2.5          1.2
4             6           6.0          4.6           2.4          1.2
..          ...           ...          ...           ...          ...
145         147           7.7          4.0           6.2          3.3
146         148           7.3          3.5           6.0          2.9
147         149           7.5          4.0           6.2          3.0
148         150           7.2          4.4           6.4          3.3
149         151           6.9          4.0           6.1          2.8

[150 rows x 5 columns]
```

测试Series参数，func为列表，非聚合函数
```python
>>> res = apply(sepal_length, ["cumsum", lambda x: x+1])
>>> print(res)
```

```
     cumsum  <lambda>
0       5.1       6.1
1      10.0       5.9
2      14.7       5.7
3      19.3       5.6
4      24.3       6.0
..      ...       ...
145   851.6       7.7
146   857.9       7.3
147   864.4       7.5
148   870.6       7.2
149   876.5       6.9

[150 rows x 2 columns]
```

测试Series参数，func为列表，聚合函数
```python
>>> res = apply(sepal_length, ["max", lambda x: x.max()-x.min()])
>>> print(res)
```

```
max         7.9
<lambda>    3.6
Name: Sepal.Length, dtype: float64
```

测试DataFrame参数，func为字典，非聚合函数
```python
>>> res = apply(iris.iloc[:, :-1], {"Sepal.Width": "cumsum", "Sepal.Length": lambda x: x+1})
>>> print(res)
```

```
     Sepal.Width  Sepal.Length
0            3.5           6.1
1            6.5           5.9
2            9.7           5.7
3           12.8           5.6
4           16.4           6.0
..           ...           ...
145        446.7           7.7
146        449.2           7.3
147        452.2           7.5
148        455.6           7.2
149        458.6           6.9

[150 rows x 2 columns]
```

测试DataFrame参数，func为字典，聚合函数
```python
>>> res = apply(iris.iloc[:, :-1], {"Sepal.Width": "sum", "Sepal.Length": lambda x: x.max()-x.min()})
>>> print(res)
```

```
Sepal.Width     458.6
Sepal.Length      3.6
dtype: float64
```

测试DataFrame参数，func为列表，非聚合函数
```python
>>> res = apply(iris.iloc[:, :-1], ["cumsum", lambda x: x+1])
>>> print(res)
```

```
    Unnamed: 0          Sepal.Length          Sepal.Width           \
        cumsum <lambda>       cumsum <lambda>      cumsum <lambda>   
0            1        2          5.1      6.1         3.5      4.5   
1            3        3         10.0      5.9         6.5      4.0   
2            6        4         14.7      5.7         9.7      4.2   
3           10        5         19.3      5.6        12.8      4.1   
4           15        6         24.3      6.0        16.4      4.6   
..         ...      ...          ...      ...         ...      ...   
145      10731      147        851.6      7.7       446.7      4.0   
146      10878      148        857.9      7.3       449.2      3.5   
147      11026      149        864.4      7.5       452.2      4.0   
148      11175      150        870.6      7.2       455.6      4.4   
149      11325      151        876.5      6.9       458.6      4.0   

    Petal.Length          Petal.Width           
          cumsum <lambda>      cumsum <lambda>  
0            1.4      2.4         0.2      1.2  
1            2.8      2.4         0.4      1.2  
2            4.1      2.3         0.6      1.2  
3            5.6      2.5         0.8      1.2  
4            7.0      2.4         1.0      1.2  
..           ...      ...         ...      ...  
145        543.0      6.2       171.9      3.3  
146        548.0      6.0       173.8      2.9  
147        553.2      6.2       175.8      3.0  
148        558.6      6.4       178.1      3.3  
149        563.7      6.1       179.9      2.8  

[150 rows x 10 columns]
```

测试DataFrame参数，func为列表，聚合函数
```python
>>> res = apply(iris.iloc[:, :-1], ["sum", lambda x: x.max()-x.min()])
>>> print(res)
```

```
          Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
sum            11325         876.5        458.6         563.7        179.9
<lambda>         149           3.6          2.4           5.9          2.4
```
