# pandas 的基本功能
from pandas import Index,Series,DataFrame
import numpy as n

# 对列/行索引重新指定索引（删除/增加：行/列）：reindex函数
x = Series([4,5,7], index=['a','b','c'])
y = x.reindex(['a','b','c','d']) # 重新指定索引
# result
# a    4.0
# b    5.0
# c    7.0
# d    NaN
# dtype: float64
x.reindex(['a','b','c','d'], fill_value=0) # fill_value指定不存在元素NaN的默认值
# result
# a    4
# b    5
# c    7
# d    0
# dtype: int64

x = Series(['blue','purple'],index=[0,4]) # 指定索引开始以及结束的位置
x.reindex(range(4),method='ffill') # 重新指定索引并指定填充NaN的方法，ffill前向填充
# result
# 0      blue
# 1      blue
# 2    purple
# 3    purple
# dtype: object

x = DataFrame(n.arange(9).reshape(3,3),index=['a','c','d'],columns=['A','B','C'])
# result
#    A  B  C
# a  0  1  2
# c  3  4  5
# d  6  7  8
x = x.reindex(['a','b','c','d'],method='bfill')  # bfill 后向填充
# 填充前
#      A    B    C
# a  0.0  1.0  2.0
# b  NaN  NaN  NaN
# c  3.0  4.0  5.0
# d  6.0  7.0  8.0
# 填充后
#    A  B  C
# a  0  1  2
# b  3  4  5
# c  3  4  5
# d  6  7  8

states = ['A','B','C','D']
x = x.reindex(columns = states, fill_value=0)
# result  替换列索引，填充NaN值为0
#    A  B  C  D
# a  0  1  2  0
# b  3  4  5  0
# c  3  4  5  0
# d  6  7  8  0

x.ix[['a','b','c','d'],states]
# result 获取指定行索引的states/表示全部列 的值
#    A  B  C  D
# a  0  1  2  0
# b  3  4  5  0
# c  3  4  5  0
# d  6  7  8  0

# 删除（丢弃）整一行/列的元素：drop函数
x = Series(n.arange(4), index=['a','b','c','d'])
x.drop('c')
# result    删除 行索引为c的行
# a    0
# b    1
# d    3
# dtype: int32

x = DataFrame(n.arange(16).reshape(4,4),index=['a','b','c','d'],columns=['A','B','C','D'])
x.drop(['A','B'], axis=1) # axis = 0表示跨行 1表示跨列
# result 在列的维度上删除AB两列
#     C   D
# a   2   3
# b   6   7
# c  10  11
# d  14  15

x.drop('a',axis=0)
# result  在行的维度上删除索引a行
#     A   B   C   D
# b   4   5   6   7
# c   8   9  10  11
# d  12  13  14  15


# DataFrame 索引、选取和过滤
x = Series(n.arange(4), index=['a','b','c','d'])
x[x<2]
# result 布尔索引
# a    0
# b    1
# dtype: int32

x['a':'c']
# result 闭区间 Series的数组切片
# a    0
# b    1
# c    2
# dtype: int32

x['a':'c'] = 5
# result 通过切片修改值
# a    5
# b    5
# c    5
# d    3

data = DataFrame(n.arange(16).reshape(4,4),index=['a','b','c','d'],columns=['A','B','C','D'])
data[:2] # 切片索引，选择行
# result
#    A  B  C  D
# a  0  1  2  3
# b  4  5  6  7

data.ix[:2,['A','B']]
# result 指定行和列索引
#    A  B
# a  0  1
# b  4  5

data.ix[['a','b'],[3,0,1]]
# result   行：字典索引，列：数组索引
#    D  A  B
# a  3  0  1
# b  7  4  5

data.ix[2]
# result  打印第二行
# A     8
# B     9
# C    10
# D    11

data.ix[:'b','A']
# result  行从开始到b，第A列
# a    0
# b    4
# Name: A, dtype: int32

data[data.A > 5]
# result  根据条件选择行
#     A   B   C   D
# c   8   9  10  11
# d  12  13  14  15

# 算术运算和数据对齐
x = DataFrame(n.arange(9.).reshape((3,3)),index=['a','b','c'],columns=['A','B','C'])
y = DataFrame(n.arange(12).reshape((4,3)),index=['a','b','c','d'],columns=['A','B','C'])
x+y
# result  不重叠部分为NaN，重叠部分元素运算
#       A     B     C
# a   0.0   2.0   4.0
# b   6.0   8.0  10.0
# c  12.0  14.0  16.0
# d   NaN   NaN   NaN

x.add(y,fill_value = 0)
# result  对x/y的不重叠部分填充，不是对结果NaN填充
#       A     B     C
# a   0.0   2.0   4.0
# b   6.0   8.0  10.0
# c  12.0  14.0  16.0
# d   9.0  10.0  11.0

frame = DataFrame(n.arange(9).reshape((3,3)),index=['a','b','c'],columns=['A','B','C'])
series = frame.ix[0]

frame - series
# result  默认按行运算
#    A  B  C
# a  0  0  0
# b  3  3  3
# c  6  6  6

series2 = Series(range(4),index=['A','B','C','D'])
frame + series2
# result 按行运算：缺失列为NaN
#    A  B   C   D
# a  0  2   4 NaN
# b  3  5   7 NaN
# c  6  8  10 NaN

series3 = frame.A
frame.sub(series3,axis = 0)
# result 按列运算。此处axis为1,则所有值为NaN
#    A  B  C
# a  0  1  2
# b  0  1  2
# c  0  1  2

# numpy函数应用与映射
frame = DataFrame(n.arange(9).reshape(3,3),index=['a','b','c'],columns=['A','B','C'])
n.square(frame)
# result  对frame进行幂运算
#     A   B   C
# a   0   1   4
# b   9  16  25
# c  36  49  64

# 匿名函数
series = frame.max()
# result  每列的最大值
# A    6
# B    7
# C    8
# dtype: int32

f = lambda x: x.max() - x.min()
frame.apply(f)
# result  作用到行
# A    6
# B    6
# C    6
# dtype: int64

frame.apply(f,axis=1)
# result 作用到列
# a    2
# b    2
# c    2
# dtype: int64

def f(x):
    return Series([x.min(),x.max()],index=['min','max'])
frame.apply(f)
# result 求每一行的最大、最小值
#      A  B  C
# min  0  1  2
# max  6  7  8

_format = lambda  x: '%.2f' % x
frame.applymap(_format)
# result 针对dataframe做出改变
#       A     B     C
# a  0.00  1.00  2.00
# b  3.00  4.00  5.00
# c  6.00  7.00  8.00

frame.A = frame['A'].map(_format)
print(frame)
# result 针对Series
#       A  B  C
# a  0.00  1  2
# b  3.00  4  5
# c  6.00  7  8
# Name: A, dtype: object