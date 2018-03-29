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
#
# newlist1 = [(x) for x in names if len(x) >4]
# newlist2 = [(x) for x in newlist1 if len(x) >5]
# print(newlist1)
# print(newlist2)
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


# list = [(x,y,z)for x in range(1,5) for y in range(1,5) for z in range(1,5) if (x*100+y*10+z)]
# print(list)


#
# list=[]
# recent_Hours= input('请输入时间（小时：分钟：秒）：')
# list.append(recent_Hours.split(':'))
# hours=list[0][0]
# minutes=list[0][1]
# seconds=list[0][2]
# def new_Hours(a,b,c):
#     s=((a*3600+b*60+c)+330)/3600
#     print(s)
# new_Hours(int(hours),int(minutes),int(seconds))

# 4.约瑟夫环
# （1）一群人围在一起坐成环状（如：N）
# （2）从某个编号开始报数（如：K）
# （3）数到某数（如：M）的时候，此人出列，下一个人重新报数
# （4）一直循环，直到剩余2个人，约瑟夫环结束

# def Joseph_ring(N,K,M): #N为总人数K为开始计数的数M为从开始报数的人到出列人之间的个数
#     list_1=list(range(1,N+1))   #遍历列表元素  从第一个人到第N个人
#     delete=K-1  #用于计算出列的人的下标
#     while True:
#         delete=(delete+M-1)%len(list_1)     #用于计算有人出列后下一个应该出列人的位置
#         del (list_1[delete])
#         if len(list_1)==2:      #当人数剩余2人，约瑟夫环结束
#             print(list_1)
#             break
# Joseph_ring(9,2,3)


# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type,number_served=0):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         self.number_served=number_served
#     def describe_restaurant(self):
#         print('饭店名：%s  烹饪类型：%s'%(self.restaurant_name,self.cuisine_type))
#     def open_restaurant(self):
#         print('本餐馆正在营业！%s '%self.number_served)
# res= Restaurant('重庆小面','川菜')
# res.describe_restaurant()
# res.open_restaurant()
# 012  112
# def fib(n):
#     list1 = []
#     for i in range(0,n):
#         if i == 0:
#             list1.append(0)
#         elif i == 1:
#             list1.append(1)
#         else:
#             list1.append(list1[i-1]+list1[i-2])
#     return list1
# print(fib(10))




# 1.斐波那契数列（Fibonacci sequence）指的是这样一个数列：1、1、2、3、5、8、13、21、34、
# ……在数学上，斐波纳契数列以如下被以递归的方法定义：F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)
# （n>=2，n∈N*）

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     elif n>=2:
#         return fib(n-1)+fib(n-2)
# print(fib(4))

# class testss:
#
#     def __init__(self):
#         ''' 初始化 '''
#         self.name = "zxk"
#         self.age = 11
#     def getMessage(self):
#         ''' 获取信息 '''
#         print(self.name,self.age)
# print(testss.__dict__)

# class dictclass():
#     def __init__(self,dict1):
#         self.dict1=dict1
#     def del_dict(self,key):
#         del self.dict1[key]
#         return self.dict1
#     def get_dict(self,key):
#         key_list=self.dict1.keys()
#         if key in key_list:
#             return key
#         else:
#             print('not found')
#     def get_key(self):
#         return self.dict1.keys()
#     def update_dict(self,dict2):
#         self.dict1.update(dict2)
#         return self.dict1
# dict1={'name':'王晓明','age':'18','hate':'c'}
# dict2={'hobby':'python','address':'上海'}
# dict=dictclass(dict1)
# print(dict.del_dict('hate'))
# dict.get_dict('hobby')
# print(dict.get_key('age'))
# print(dict.update_dict(dict2))


# 题目9：定义一个字典类：dictclass。
# 完成下面的功能：     
# dict = dictclass({你需要操作的字典对象})   
# 1 删除某个key    del_dict(key)     
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"    get_dict(key)   
# 3 返回键组成的列表：返回类型;(list)    get_key()   
# 4 合并字典，并且返回合并后字典的values组成的列表。
#   返回类型:(list) update_dict({要合并的字典})

# class dictclass:
#     # 初始化方法
#     def __init__(self,dict1):
#         self.dict1 = dict1;
#
#     # 删除指定key
#     def del_dict(self,key):
#         del self.dict1[key]
#         return self.dict1;
#
#     # 键是否存在
#     def get_dict(self,key):
#         try:
#             return self.dict1[key];
#         except KeyError:
#             return "not found"
#
#     # 返回键列表
#     def get_key(self):
#         return list(self.dict1.keys());
#
#     # 合并列表，返回合并的列表values 值列表
#     def update_dict(self,targetDic):
#         result = self.dict1.copy();
#         result.update(targetDic);
#         return list(result.values());
#
# dict1 = {"name":"zxk","age":"18"}
# dict2 = {"address":"shanghai"}
# dict3 = dictclass(dict1);
# print("删除 age key：" + str(dict3.del_dict("age")));
# print("age 是否存在：" + str(dict3.get_dict("age")));
# print(dict3.get_key())
# print(dict3.update_dict(dict2))
#
# class bank():
#     dict={}
#     def __init__(self):
#         print('欢迎光临')
#     def new_Account(self):  #开户操作
#         print('欢迎选择开户服务')
#         user_name=input('请输入用户名：')
#         id_card=input('开户卡号：')
#         for k,v in bank.dict.items():
#             print(v)
#             if id_card in v:
#                 print('卡号重复，请重新输入卡号：')
#         password=input('请输入密码：')
#         flag=True   #用于判断while循环
#         while flag:
#             money=input('请输入您开户的金额（不低于50元，金额将转做您的余额）：')
#             if int(money) <50:
#                 print('金额小于50，请重新输入')
#             else:
#                 print('恭喜你开户成功！用户名：%s 卡号：%d 密码：%d 余额：%d元'%(user_name,int(id_card),int(password),int(money)))
#                 bank.dict[user_name]=[id_card,password,int(money)]  #将新信息储存在字典bank.dict中
#                 flag=False
#
#     def save(self):  # 存钱服务
#         flag = True  # 用于判断while循环
#         while flag:
#             id_card = input('开户卡号：')
#             password = input('请输入密码：')
#             if id_card == '' or password == '':
#                 print('账号或密码为空 请重新输入')
#             else:
#                 for k, v in bank.dict.items():
#                     if id_card in v and password in v[1]:  #
#                         flag = False
#                     else:
#                         print('该用户未开户')
#         for k, v in bank.dict.items():  # 存钱流程
#             if id_card in v:
#                 save_money = input('存款金额(只收取100元钞票):')
#                 v[2] += int(save_money)
#                 print('存款成功，余额%d' % v[2])
#                 break
#
#     def get(self):  # 取钱服务
#         flag = True  # 用于判断while循环
#         while flag:  # 登录账户
#             id_card = input('开户卡号：')
#             password = input('请输入密码：')
#             if id_card == '' or password == '':
#                 print('账号或密码为空 请重新输入')
#             else:
#                 for k, v in bank.dict.items():
#                     if id_card in v and password in v[1]:
#                         flag = False
#                     else:
#                         print('该用户未开户')
#         flag = True
#         for k, v in bank.dict.items():  # 取钱流程
#             while flag:
#                 get_money = int(input('取款金额（只提供100元钞票）：'))
#                 if get_money <= v[2]:
#                     v[2] -= get_money
#                     print('取款成功，卡内余额为：%d' % v[2])
#                     flag = False
#                 else:
#                     print('卡内余额不足，请重新输入')
#
#     def info(self):  # 查询服务
#         question = input('是否查询所有用户信息（y是）：')
#         if question == 'y':
#             for k, v in bank.dict.items():
#                 print('用户姓名：%s 卡号：%s 密码：%s 余额：%d' % (k, v[0], v[1], int(v[2])))
#         else:
#             user_name = input('输入需要查询的用户名：')
#             for k, v in bank.dict.items():
#                 if user_name == k:
#                     print('用户名：%s卡号：%s 余额：%d ' % (user_name, v[0], int(v[2])))
#                 else:
#                     print('用户信息不存在')
#
#
# bank1 = bank();
#
# bank1.new_Account();
# bank1.new_Account();