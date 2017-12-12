from pandas import DataFrame,Series
import numpy as n

# 使用字典生成DataFrame key为列名称
data = {'state':['ok', 'ok', 'good', 'bad'],
        'year':[2000, 2001, 2002, 2003],
        'pop':[3.7, 3.6, 2.4, 0.9]}
# columns指定列索引 不匹配的列为NaN  index指定行索引
DataFrame(data, columns=['year','state','pop','debt'],index=['one','two','three','four'])
# result
#        year state  pop debt
# one    2000    ok  3.7  NaN
# two    2001    ok  3.6  NaN
# three  2002  good  2.4  NaN
# four   2003   bad  0.9  NaN

x = DataFrame(data, columns=['year','state','pop','debt'],index=['one','two','three','four'])
x['state'] # ==> x.state 返回名称为state的 Series as 列
# result
# one        ok
# two        ok
# three    good
# four      bad
# Name: state, dtype: object

x.ix['three']  # ix[] 区分[],进行行索引的数据显示
# result
# year     2002
# state    good
# pop       2.4
# debt      NaN
# Name: three, dtype: object

# x['dept'] = 16.5  #修改整列数据
# result
#        year state  pop debt  dept
# one    2000    ok  3.7  NaN  16.5
# two    2001    ok  3.6  NaN  16.5
# three  2002  good  2.4  NaN  16.5
# four   2003   bad  0.9  NaN  16.5

x.debt = n.arange(4) # 用numpy数组修改元素
# result
#        year state  pop  debt
# one    2000    ok  3.7     0
# two    2001    ok  3.6     1
# three  2002  good  2.4     2
# four   2003   bad  0.9     3

val = Series([-1.2,-1.5,-1.7,0], index=['one','two','four','six'])
x.debt = val # 使用Series修改元素，DataFrme的行索引不变
# result
#        year state  pop  debt
# one    2000    ok  3.7  -1.2
# two    2001    ok  3.6  -1.5
# three  2002  good  2.4   NaN
# four   2003   bad  0.9  -1.7

x['gain'] = (x.debt>0) # 类似numpy的布尔索引  ——》添加新列
# result
#        year state  pop  debt   gain
# one    2000    ok  3.7  -1.2  False
# two    2001    ok  3.6  -1.5  False
# three  2002  good  2.4   NaN  False
# four   2003   bad  0.9  -1.7  False

# 使用切片初始化数据，未被匹配的数据未NaN
pdata = {'state':x['state'][:2],'pop':x['pop'][:3]}
y = DataFrame(pdata)    # 以行数多的列为主，行数少的列未匹配的数据未NaN
# result
#        pop state
# one    3.7    ok
# three  2.4   NaN
# two    3.6    ok

y.index.name = '序号'   # 指定索引名称
y.columns.name = '信息' # 指定列名称
# result
# 信息     pop state
# 序号
# one    3.7    ok
# three  2.4   NaN
# two    3.6    ok