with open("../filter.py", "rt", encoding="utf8") as fp: exec(fp.read())
with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
iris = read("../data/iris.xlsx")
s = pd.Series([i for i in range(100)])
res = filter(s, "in [90, 99]")
print(res)
s = pd.Series([i for i in range(100)])
res = filter(s, "not in [90, 99]")
print(res)
