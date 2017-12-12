import numpy as np

x = np.array(((1,2,3),(4,5,6)))
y = np.array([[1,2,3],[4,5,6]])
print(y)
y[0] =10
print(x)
# print(x[0,3])  x=0  索引3  4
# print(x[1,3])  x=1  索引3  8
# print(x[2,3])  x=2  索引3  12
## 数组切片
y=x[:,1]
# y[0]=10  改变y将会改变x
# print(x)
print(y)

# print(y) : 表示(x的所有值) 索引为1，  2、6、10

# 改变array的数据类型
# numeric_strings2 = np.array(['1.23','2.34','3.45'])
# print(numeric_strings2.astype(str))

# bool类型
names = np.array(['bob','sdf','bob','sdr'])
print(names == 'bob')

## 条件筛选
data = np.array([[ 0.36762706, -1.55668952,0.84316735, -0.116842],
       [ 1.34023966,  1.12766186,  1.12507441, -0.68689309],
       [ 1.27392366, -0.43399617, -0.80444728,  1.60731881],
       [ 0.23361565,  1.38772715,  0.69129479, -1.19228023],
       [ 0.51353082,  0.17696698, -0.06753478,  0.80448168],
       [ 0.21773096,  0.60582802, -0.46446071,  0.83131122],
       [ 0.50569072,  0.04431685, -0.69358155, -0.9629124 ]])
data[data < 0] = 0
print(data)

np.savetxt("data.txt",data)
# 保存加载数组二进制文件
# arr = np.arange(10)
# print(arr)
# np.save("some_array",arr)
# print(np.load("some_array.npy"))
nexts = np.loadtxt("data.txt")
print(nexts)

a = np.zeros(2,2,2)
print(a.ndim) #数组的维数
print(a.shape) #数组每一维数的大小
print(a.size)  #数组的元素个数
print(a.itemsize) #每个元素所占的字节数