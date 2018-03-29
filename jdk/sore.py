
# 1  B
# 2  C
# 3  A
# 4  A
# 5  A
# 6  B
# 7  D
# 8  C
# 9  A
# 10  B
# 11  A
# 12  A
# 13  B
# 14  A
# 15  A
# 16  A
# 17  A
# 18  A
# 19  B
# 20  A
# 21  B
# 22  A
# 23  B
# 24  A
# 25  A
# 26  A
# 27  A
# 28  A

# 29题
primeNums =[]
for num in range(100, 301):
    for divided in range(2, num):
        if num % divided == 0:
            break
    else:
        primeNums.append(num)
for i in range(len(primeNums)):
    if (i + 1) % 8 == 0:
        print()
        print('----1----')
    print(primeNums[i], end = '  ')

# 30题
def fun(i):
    if (i == 1):
        print(str(1),end='')
        return

    z = 0
    for j in range(i):
        z = 2**j
        print(str(z)+" ",end="")

    while(z/2 != 1):
        print(str(int(z/2))+" ",end="")
        z = z/2
    print(str(1),end="")
n = 8
for i in range(1,n+1):
    for space in range(n-i):
        print(' '*2, end='')
    fun(i)
    print()

# 31题
ori_list = [1, 2, 3, 4, 5, 6, 7]
new_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
def detection(ori_list, new_list):
    ls = []
    flag = True
    for li in ori_list:
        if list(new_list).__contains__(li):
            ls.append(li)
            flag = False
    if flag:
        return True
    else:
        return ls

print(detection(ori_list, new_list))

#32 题
def gcd(fiNum, seNum):
    if (fiNum <=  0 or fiNum > 1000) or (seNum <=  0 or seNum > 1000):
        raise Exception('Input positive integer too large')
    commDivisors = []
    for divided in range(1, max(fiNum, seNum)):
        if fiNum % divided == 0 and seNum % divided == 0:
            commDivisors.append(divided)
    return '最大公约数是：%d'%max(commDivisors)
print(gcd(200, 100))

#33题 不会。。。

# 34题
def num(value):
    # 定义表达式 字符串
    strings = "";
    # 定义值
    count = 0;
    for i in range(1, value + 1):
        strings = strings + str(i) + "!+"
        count = count * i;
    # 格式化输出
    print("%s的和是：%d" % (strings[:len(strings) - 1], count))
num(5)

# 35题
def jiami(old):
    new = "";
    try:
        # 获得个位
        g = (int(old[3]) + 5) % 10;
        # 获得十位
        s = (int(old[2]) + 5) % 10;
        # 获得百位
        b = (int(old[1]) + 5) % 10;
        # 获得千位
        q = (int(old[0]) + 5) % 10;
        new = new + str(g);
        new = new + str(b);
        new = new + str(s);
        new = new + str(q);
    except BaseException:
        print("数字有误!");
    finally:
        return new;


print(jiami(input("请输入一个4位整数：")))


# 36题目
class ju:
    def __init__(self, width, longs):
        # 定义宽和长
        self.longs = longs;
        self.width = width;

    def getJi(self):
        # 面积计算公式
        return self.width * self.longs;


class chang(ju):
    def __init__(self, longs, width, height):
        self.height = height
        super().__init__(width, longs);

    def getTiJi(self):
        # 体积计算公式
        return self.longs * self.width * self.height;


ch = chang(10, 5, 4);
print("长方形的低面积和体积是：%d, %d" % (ch.getJi(), ch.getTiJi()))



# 37题
class People:
    def __init__(self,name,sex,age,country):
        self.name = name
        self.age = age
        self.sex = sex
        self.country = country

    def eat(self):
        print("吃饭")

    def sleep(self):
        print("睡觉")

    def work(self):
        print("我叫%s,今年%d岁,国籍%s" % (self.name, self.age,self.country))

class Student(People):

    def __init__(self,name,sex,age,country,school,studentNo):
        # 初始化
        super().__init__(name,sex,age,country)
        self.school = school
        self.studentNo = studentNo

    def work(self):
        print("我叫%s,今年%d岁,我是一名来自%s的学生" % (self.name, self.age,self.school))

class GanBu(Student):
    def __init__(self,name,sex,age,country,school,studentNo,zhiWu):
        super().__init__(name,sex,age,country,school,studentNo)
        self.zhiWu = zhiWu
    def openWork(self):
        print("我叫%s,今年%d岁,我的职务是%s" %(self.name,self.age,self.zhiWu))

if __name__ == "__main__":
    g = GanBu("zxk","男",19,"中国","北风","12138","学生会主席")
    g.openWork();
    s = Student("yuan","女",19,"中国","北风","12139")
    s.work();
    p = People("li","女",19,"中国")
    p.work()
