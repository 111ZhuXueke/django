import matplotlib.pylab as plt
import numpy as n
from pylab import *
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

# axex: 设置坐标轴边界和表面的颜色、坐标刻度值大小和网格的显示
# backend: 设置目标暑促TkAgg和GTKAgg
# figure: 控制dpi、边界颜色、图形大小、和子区( subplot)设置
# font: 字体集（font family）、字体大小和样式设置
# grid: 设置网格颜色和线性
# legend: 设置图例和其中的文本的显示
# line: 设置线条（颜色、线型、宽度等）和标记
# patch: 是填充2D空间的图形对象，如多边形和圆。控制线宽、颜色和抗锯齿设置等。
# savefig: 可以对保存的图形进行单独设置。例如，设置渲染的文件的背景为白色。
# verbose: 设置matplotlib在执行期间信息输出，如silent、helpful、debug和debug-annoying。
# xticks和yticks: 为x,y轴的主刻度和次刻度设置颜色、大小、方向，以及标签大小。

# xlim ylim 确定坐标范围
# x = n.arange(-5.0,5.0,0.02)
# y = np.sin(x)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(x,y)
#
# plt.subplot(212)
# xlim(-2.5,2.5)
# ylim(-1,1)
# plt.plot(x,y)
# plt.show()

# 叠加图
# t = n.arange(0.,5.,0.2)
# plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
# plt.show()

# plt.figure()
# plt.figure(1)
# plt.subplot(211)
# plt.plot([1,2,3])
# plt.subplot(212)
# plt.plot([4,5,6])
#
#
# plt.figure(2)
# plt.plot(n.arange(4,7))
#
# plt.figure(1)
# plt.subplot(211)
# plt.title('easy as 1,2,3')
# plt.show()

# plt.text() 文字说明

# mu,singma = 100,15
# x = mu + singma * np.random.randn(10000)
#
# n,bins,patches = plt.hist(x,50,normed=1,facecolor='g',alpha = 0.75)
#
# plt.xlabel('Smarts')
# plt.ylabel('histogram of IQ')
# plt.text(60,.025,r'$\mu=100,\ \singma=15$')
# plt.axis([40,160,0,0.03])
# plt.grid(True)
# plt.show()

# plt.annotate() 文本注释

ax = plt.subplot(111)
t = n.arange(0.0,5.0,0.01)
s = n.cos(2*n.pi*t)
line, = plt.plot(t,s,lw=2)
plt.annotate('local max',xy = (2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.05),)
plt.ylim(-2,2)
plt.show()