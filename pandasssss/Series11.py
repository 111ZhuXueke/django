import pandas as pd
from pandas import Series,DataFrame

# 用一维数组生成Series
x = Series([1,2,3,4])
print(x)

# 指定Series的index' 可将index理解为行索引
x = Series([1,2,3,4], index=['a','b','c','d'])
print(x.index)
# 通过行索引来取得元素值
print(x['a'])
# 通过索引赋值
x['b'] = 6
print(x)

print(x[['c','a','d']])
# 类似于numpy的布尔索引
print(x[x > 2])
# 类似字典的使用
print('b' in x)

# 使用字典生成Series  并制定额外的index  不匹配的使用NaN表示
exindex = ['a','b','e']
data = {'a':1,'b':2,'c':3}
y = Series(data,index=exindex)
print(y)
# Series.index = [] 设置索引/替换索引
# 相同索引相加 不同行值为NaN Series.name制定Series名称 Series.index.name执行index名称
print(x+y)