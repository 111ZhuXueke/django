import re
import random
import math
# 设 a 列表存在6个整数
a = [1,2,3,4,5,6]
def getList(b,a,i):
    b.append(a[i+1] - a[i])
    # 若 i 的下标为4，表示会进行最后一次相减，然后退出
    if i == len(a) - 2:
        return b;
    # 下次相减的数应为当前下标的后两位，也就是第三位数
    return getList(b,a,i + 2)
list1 = []
# print(getList(list1,a,0))

# tup1 = (68,87,92,100,76,88,54,89,76,61)
# print(tup1[2])
# print(tup1[0:6])
# dic1 = {}
# dic2 = {}
# for i in range(2):
#     str = input("请输入你的名字：")
#     phone = input("请输入你的联系电话：")
#     addr = input("请输入你的住址：")
#     dic2.setdefault("phone",phone)
#     dic2.setdefault("addr", addr)
#     dic1.setdefault(str,dic2)
#     dic2 = {}
# print(dic1)

# # 加法
# def add(a,b):
#     return a+b;
#
# # 减法
# def reduce(a,b):
#     return a - b;
#
# # 除法
# def division(a,b):
#     return a / b;
#
# # 乘法
# def ride(a,b):
#     return a*b;
#
# def switch(str,a,b):
#     if str == "+":
#         print(add(a,b))
#     elif str == "-":
#         print(reduce(a,b))
#     elif str == "*":
#         print(ride(a,b))
#     elif str == "/":
#         print(switch(a,b))
#     else:
#         print("输入有误！请重新输入")
#         str = input("请输入运算法则（+-*/）：")
#         switch(str,a,b)
# first = input("请输入第一个数字：")
# seconed = input("请输入第二个数字：")
# str = input("请输入运算法则（+-*/）：")
# switch(str,int(first),int(seconed))

# a = input("请输入一个字符串:")
# a = a.upper();
# count = 1;
# value = a[0];
# for i in range(len(a)):
#     if value == a[i]:
#         count = count + 1
#     else:
#         print(str(value) + " 一共出现" + str(count) + "次")
#         count = 1
#     value = a[i];
#     if i == len(a)-1:
#         print(str(value) + " 一共出现" + str(count) + "次")

# list3 = []
# tea = input("请输入技术老师名称：")
# list3.append(tea)
# classRen = input("请输入班主任名称：")
# classRen.lower()
# classRen.upper()
# name = ""
# while 1==1:
#     name = input("请输入同学名称(输入 n 结束)：")
#     if name == "n":
#         break;
#     list3.append(name);
# list3.append(classRen)
# for i in range(len(list3)):
#     if i == 0 or i == len(list3) - 1:
#         continue;
    # print("你好" + list3[i] + "同学")


# values = "s.d.d.f.f"
# print(values.split("."))
# print(values.split())

favorite_places = {"zxk":{"play":"运动"},"xkz":{"music":"音乐","humor":"幽默"},"kxz":{"music":"音乐","humor":"幽默","code":"敲代码"}}
# print(favorite_places)

dog = {"animal":"狗狗","master":"zxk"}
cat = {"animal":"猫咪","master":"kxz"}
pets = [dog,cat]
# for i in pets:
#     print("我是%s 我的主人是 %s" %(i["animal"],i["master"]))

# 列表
# list1 = [1,2,3]
# list1.append(4)
# list1[0]=0
# list1.remove(0)
# # print(list1[0])
#
# # 元祖
# tup1 = (1,2,3,[1,2])
# tup1[3][0] = 2
# print(tup1[3])
#
# # 集合
# set1 = {1,2,3}
# set1.add(4)
# set1.remove(1)
# set1.update("hello")
# print(set1)
#
# # 字典
# dic1 = {"str":"hello"}
# dic1["music"]="Drean It Possible"
# print(dic1["music"])
# dic1["music"]="You're The One"
# del dic1["str"]
# print(dic1)

# def add(a,b):
#     return a+b;
# def subtraction(a,b):
#     return a-b;
# def multiplication(a,b):
#     return a*b;
# def division(a,b):
#     return a/b;
#
# first = int(input("请输入第一个数："))
# two = int(input("请输入第二个数："))
# stss = input("请输入操作（+-*/）：")
# if stss == "+":
#     print(add(first,two))
# elif stss == "-":
#     print(subtraction(first,two))
# elif stss == "*":
#     print(multiplication(first,two))
# elif stss == "/":
#     print(division(first,two))
# else:
#     print("输入有误!")

# list2 = ["我是","一只","小小鸟","想要飞却","总也飞不高"]
# for i in list2:
#     print(i,end="")
# dic1 = {"age":19,"name":"zxk","like":"音乐、运动"}
# # print("我叫" + dic1["name"] + "，今年" + str(dic1["age"]) + "岁，最喜欢" + dic1["like"])
# def double(matched):
#     # 用正则表达式去匹配一个组、将匹配到的结果转换为 int，最后转换为字符串输出
#     value = float(matched.group('strs'))
#     return str(int(value))
# s = 'a2.3g4hGd5.67'
# print(s)
# # P<name> 表示对一个组根据表达式进行匹配
# a = (re.sub('(?P<strs>(\d+(\.\d+)?)+)', double, s)).upper();
# b = [(x) for x in a]
# print(b)

# num1 = int(input("请输入8位以内的正整数："))
# length = len(str(num1))
# if length >=8:
#     print("超过8位,请重新输入！")
# else:
#     print("输入整数为" + str(length) + "位数," + "逆序输出为:" + str(num1)[::-1])

# higth = int(input("请输入高度："))
# count = 100
# for i in range(10):
#     higth = higth / 2
#     count = count + higth
# print("共经过:" + str(count) + "米，第10次反弹:" + str(float(higth)))

# def number(str1):
#     pattern = re.compile(r'\d+')  # 查找数字
#     result1 = pattern.findall(str1)
#     return len(result1)
# def english(str1):
#     pattern = re.compile(r'[a-z]+')  # 查找字母
#     result1 = pattern.findall(str1)
#     return len(result1)
# def white(str1):
#     pattern = re.compile(r'\s+')  # 查找空格
#     result1 = pattern.findall(str1)
#     return len(result1)
# str1s = input("请输入一串字符串：") ## aa22 #
# print("数字次数为:" + str(number(str1s)) + ",字母次数：" + str(english(str1s)) + "，空格为:" + str(white(str1s)))
# print("其他字符次数为:" + str(len(str1s) - number(str1s) - english(str1s) - white(str1s)))

# score = int(input("请输入成绩："))
# if score >= 90:
#     print("A")
# elif score >=60:
#     print("B")
# else:
#     print("C")
# begin = int(input("请输入随机数开始范围数字："))
# end = int(input("请输入随机数结束范围数字："))
# me = int(input("请输入要比对的数字："))
# values = random.randint(begin,end)
# if me > values:
#     print("win")
# elif me < values:
#     print("fail")
# else:
#     print("平局")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i) +"*"+str(j) + "=" +str(i*j)+" ",end="")
#     print()
# num1 = int(input("请输入最大值:"))
# count =0
# for i in range(num1):
#     if i % 3 ==0 or i % 17 ==0:
#         count = count + i
# print(count)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(10 - i) +"*"+str(10 - j) + "=" +str((10 - i)* (10 - j))+" ",end="")
#     print()
# widths = 5
# for i in range(widths):
#     if i == 0 or i == widths-1:
#         print("* "*(widths*2-1))
#     else:
#         print("*" + " "*((widths*3-1)) + " *")

# num = 1;
# while num > 0:
#     str = input("老婆你爱我吗？")
#     if str == "爱":
#         num = 0

# L = [75,98,59,81,66,43,69,85]
# list1 = []
# for i in L:
#     if i >= 60:
#         list1.append(i)
# L = list1
# print(L)
# i = 0
# count = 0;
# while i<100:
#     if i % 2 == 0:
#         i = i + 1
#         continue;
#     else:
#         count = count + i
#         i = i + 1
# print(count)

# i = 1
# num = 2
# count = 2
# while True:
#     if i == 21:
#         break;
#     count = count + num * i
#     i = i+1
# print(count+1)

# names = ['Tom','Billy','Jefferson',"Andrew","Wesley","Steven","joe","Alice",'Jill',"Ana","Wendy","Jennifer","Sherry",'Eva']
# newlist1 = []
# newlist2 = []
# for i in names:
#     if len(i) > 4:
#         newlist1.append(i)
# for i in newlist1:
#     if len(i) >=5:
#         newlist2.append(i.upper())
#
# print("大于4的名字：" + str(newlist1))
# print("大于5的名字：" + str(newlist2))

# a = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         a[i] = a[i]*a[i]*a[i]
# print(a)




# def isPrime(n):
#     if n <= 1:
#         return "不是素数"
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return "不是素数"
#     return "是素数"
#
# print(isPrime(5))

# num2 = input("请输入一个5位数字：")
# while len(num2) != 5:
#     print("输入有误，请重新输入!")
#     num2 = input("请输入一个5位数字：")
# if num2[0] == num2[4] and num2[1] == num2[3]:
#     print("是回文数")
# else:
#     print("不是回文数")

# favourite_places={'张三':'lodon','李四':['上海'],'王五':['重庆','广州','深圳']}
# prefer_Places=input('请输入你最喜欢的城市：')
# state = 1  ## 0 表示 存在、0表示不存在
# for key,values in favourite_places.items():
#     if  prefer_Places in values:
#         print(key,values)
#         state = 1
#         break
#     else:
#         state = 0;
# if state == 0:
#     print("信息不详")
#
# for i in range(10):
#     print(i)
# for i in range(10):
#     print(1)

# result1 = random.randint(1,3)
# num1 = int(input("请输入剪刀(1)、石头(2)、布(3)："))
# while 1==1:
#     if num1 - result1 == 1 or num1 - result1 == -2:
#         print("胜利了")
#     elif num1 - result1 == -1 or num1 - result1 == 2:
#         print("输了")
#     else:
#         print("平局")
#     vals = input("输入y继续，输入n退出...")
#     if vals == "n":
#         break;
#     result1 = random.randint(1, 3)
#     num1 = int(input("请输入剪刀(1)、石头(2)、布(3)："))


# list = [(x,y,z)for x in range(1,5) for y in range(1,5) for z in range(1,5) if (x*100+y*10+z)]
# print(list)
