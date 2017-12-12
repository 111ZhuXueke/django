from pandas import Index,Series,DataFrame
import numpy as n
x = Series(range(3), index=['a','b','c'])
(x.index[:2])
#result Index(['a', 'b'], dtype='object') 获取Index对象并进行切片处理

index = Index(n.arange(3))
obj = Series([1.5,-2.5,0],index=index)  # 构造Index(索引)对象
# result
# 0    1.5
# 1   -2.5
# 2    0.0
# dtype: float64

obj.index is index is True # obj.index ==> index  <> Index

data = {'pop':{2.4, 2.9},
        'year':{2001, 2002} }
x = DataFrame(data)  # 索引默认0和1
print('pop' in x.columns)   # 判断列是否存在
print(1 in x.index)         # 判断行索引是否存在
# result
# True
# True