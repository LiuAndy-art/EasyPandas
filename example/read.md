导入模块
```python
>>> from EasyPandas import read
```

基本用法
```python
>>> df = read("../data/iris.csv")
>>> print(df.head())
```

```
   Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0           1           5.1          3.5           1.4          0.2  setosa
1           2           4.9          3.0           1.4          0.2  setosa
2           3           4.7          3.2           1.3          0.2  setosa
3           4           4.6          3.1           1.5          0.2  setosa
4           5           5.0          3.6           1.4          0.2  setosa
```

读取其他分隔符
```python
>>> df = read("../data/iris.csv", textfileparamsdict={"sep": ","})
>>> print(df.head())
```

```
   Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0           1           5.1          3.5           1.4          0.2  setosa
1           2           4.9          3.0           1.4          0.2  setosa
2           3           4.7          3.2           1.3          0.2  setosa
3           4           4.6          3.1           1.5          0.2  setosa
4           5           5.0          3.6           1.4          0.2  setosa
```

不指定任何行作为列名
```python
>>> df = read("../data/iris.csv", textfileparamsdict={"header": None})
>>> print(df.head())
```

```
    0             1            2             3            4        5
0  NaN  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  Species
1  1.0           5.1          3.5           1.4          0.2   setosa
2  2.0           4.9            3           1.4          0.2   setosa
3  3.0           4.7          3.2           1.3          0.2   setosa
4  4.0           4.6          3.1           1.5          0.2   setosa
```

指定列名
```python
>>> df = read("../data/iris.csv", textfileparamsdict={"names": ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]})
>>> print(df.head())
```

```
     sepal_length  sepal_width  petal_length  petal_width  species
NaN  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  Species
1.0           5.1          3.5           1.4          0.2   setosa
2.0           4.9            3           1.4          0.2   setosa
3.0           4.7          3.2           1.3          0.2   setosa
4.0           4.6          3.1           1.5          0.2   setosa
```

指定索引
```python
>>> df = read("../data/iris.csv", textfileparamsdict={"index_col": 1})
>>> print(df.head())
```

```
              Unnamed: 0  Sepal.Width  Petal.Length  Petal.Width Species
Sepal.Length                                                            
5.1                    1          3.5           1.4          0.2  setosa
4.9                    2          3.0           1.4          0.2  setosa
4.7                    3          3.2           1.3          0.2  setosa
4.6                    4          3.1           1.5          0.2  setosa
5.0                    5          3.6           1.4          0.2  setosa
```

指定读取的列名
```python
>>> df = read("../data/iris.csv", textfileparamsdict={"usecols": ["Sepal.Length", "Sepal.Width", "Species"]})
>>> print(df.head())
```

```
   Sepal.Length  Sepal.Width Species
0           5.1          3.5  setosa
1           4.9          3.0  setosa
2           4.7          3.2  setosa
3           4.6          3.1  setosa
4           5.0          3.6  setosa
```

指定读取的文件行数
```python
>>> df = read("../data/iris.csv", textfileparamsdict={"names": ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"], "nrows": 3})
>>> print(df.head())
```

```
     sepal_length  sepal_width  petal_length  petal_width  species
NaN  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  Species
1.0           5.1          3.5           1.4          0.2   setosa
2.0           4.9            3           1.4          0.2   setosa
```

将第一列作为行名
```python
>>> df = read("../data/iris.xlsx", excelfileparamsdict={"index_col": 0})
>>> print(df.head())
```

```
   Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
1           5.1          3.5           1.4          0.2  setosa
2           4.9          3.0           1.4          0.2  setosa
3           4.7          3.2           1.3          0.2  setosa
4           4.6          3.1           1.5          0.2  setosa
5           5.0          3.6           1.4          0.2  setosa
```

不将第一列作为行名
```python
>>> df = read("../data/iris.xlsx")
>>> print(df.head())
```

```
   Unnamed: 0  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0           1           5.1          3.5           1.4          0.2  setosa
1           2           4.9          3.0           1.4          0.2  setosa
2           3           4.7          3.2           1.3          0.2  setosa
3           4           4.6          3.1           1.5          0.2  setosa
4           5           5.0          3.6           1.4          0.2  setosa
```

不将第一行作为列名
```python
>>> df = read("../data/iris.xlsx", excelfileparamsdict={"header": None})
>>> print(df.head())
```

```
     0             1            2             3            4        5
0  NaN  Sepal.Length  Sepal.Width  Petal.Length  Petal.Width  Species
1  1.0           5.1          3.5           1.4          0.2   setosa
2  2.0           4.9            3           1.4          0.2   setosa
3  3.0           4.7          3.2           1.3          0.2   setosa
4  4.0           4.6          3.1           1.5          0.2   setosa
```

将第一列作为行名且指定列名
```python
>>> df = read("../data/iris.xlsx", excelfileparamsdict={"index_col": 0, "names": ["v1", "v2", "v3", "v4", "v5"]})
>>> print(df.head())
```

```
   v1   v2   v3   v4      v5
1  5.1  3.5  1.4  0.2  setosa
2  4.9  3.0  1.4  0.2  setosa
3  4.7  3.2  1.3  0.2  setosa
4  4.6  3.1  1.5  0.2  setosa
5  5.0  3.6  1.4  0.2  setosa
```

指定要读取的列
```python
>>> df = read("../data/iris.xlsx", excelfileparamsdict={"usecols": ["Sepal.Length", "Sepal.Width", "Species"], "index_col": 0})
>>> print(df.head())
```

```
              Sepal.Width Species
Sepal.Length                     
5.1                   3.5  setosa
4.9                   3.0  setosa
4.7                   3.2  setosa
4.6                   3.1  setosa
5.0                   3.6  setosa
```

指定读取的行数
```python
>>> df = read("../data/iris.xlsx", excelfileparamsdict={"usecols": ["Sepal.Length", "Sepal.Width", "Species"], "nrows": 50})
>>> print(df.head())
```

```
   Sepal.Length  Sepal.Width Species
0           5.1          3.5  setosa
1           4.9          3.0  setosa
2           4.7          3.2  setosa
3           4.6          3.1  setosa
4           5.0          3.6  setosa
```

读取xls文件
```python
>>> df = read("../data/womenexport.xls")
>>> print(df.head())
```

```
   Unnamed: 0  height  weight
0           1    58.0   115.0
1           2    59.0   117.0
2           3    60.0   120.0
3           4    61.0   123.0
4           5    62.0   126.0
```

测试pkl参数
```python
>>> df = read("../data/iris.pkl")
>>> print(df.head())
```

```
   Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
```

测试dta参数
```python
>>> df = read("../data/auto.dta")
>>> print(df.head())
```

```
            make  price  mpg  rep78  headroom  trunk  weight  length  turn  \
0    AMC Concord   4099   22    3.0       2.5     11    2930     186    40   
1      AMC Pacer   4749   17    3.0       3.0     11    3350     173    40   
2     AMC Spirit   3799   22    NaN       3.0     12    2640     168    35   
3  Buick Century   4816   20    3.0       4.5     16    3250     196    40   
4  Buick Electra   7827   15    4.0       4.0     20    4080     222    43   

   displacement  gear_ratio   foreign  
0           121        3.58  Domestic  
1           258        2.53  Domestic  
2           121        3.08  Domestic  
3           196        2.93  Domestic  
4           350        2.41  Domestic  
```

测试xpt参数
```python
>>> df = read("../data/hh.xpt")
>>> print(df.head())
```

```
               MAKE   PRICE   MPG  REP78  HEADROOM  TRUNK  WEIGHT  LENGTH  \
0    b'AMC Concord'  4099.0  22.0    3.0       2.5   11.0  2930.0   186.0   
1      b'AMC Pacer'  4749.0  17.0    3.0       3.0   11.0  3350.0   173.0   
2     b'AMC Spirit'  3799.0  22.0    NaN       3.0   12.0  2640.0   168.0   
3  b'Buick Century'  4816.0  20.0    3.0       4.5   16.0  3250.0   196.0   
4  b'Buick Electra'  7827.0  15.0    4.0       4.0   20.0  4080.0   222.0   

   TURN  DISPLACE  GEAR_RAT       FOREIGN  
0  40.0     121.0      3.58  5.397605e-79  
1  40.0     258.0      2.53  5.397605e-79  
2  35.0     121.0      3.08  5.397605e-79  
3  40.0     196.0      2.93  5.397605e-79  
4  43.0     350.0      2.41  5.397605e-79
```

测试sav参数
```python
>>> df = read("../data/iris.sav")
>>> print(df.head())
```

```
   Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
```
