导入模块
```python
>>> from EasyPandas import factor, read
>>> df = read("../data/toothgrowth.txt", textfileparamsdict={"sep": "\t"})
```

基本测试
```python
>>> res = factor(df["supp"])
>>> print(res)
```

```
字符串数据的类别和离散化值对应关系如下
{'discrete_value': [0, 1], 'category': ['VC', 'OJ']}
0     0
1     0
2     0
3     0
4     0
5     0
6     0
7     0
8     0
9     0
10    0
11    0
12    0
13    0
14    0
15    0
16    0
17    0
18    0
19    0
20    0
21    0
22    0
23    0
24    0
25    0
26    0
27    0
28    0
29    0
30    1
31    1
32    1
33    1
34    1
35    1
36    1
37    1
38    1
39    1
40    1
41    1
42    1
43    1
44    1
45    1
46    1
47    1
48    1
49    1
50    1
51    1
52    1
53    1
54    1
55    1
56    1
57    1
58    1
59    1
dtype: int64
```
