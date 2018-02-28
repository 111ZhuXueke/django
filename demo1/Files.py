def fun():
    try:
        fileName = input("请输入要打开的文件:\n")
        with open("test.txt", 'w', encoding='utf-8') as files:
            str = input("请输入要写入的内容（#号结束）：")
            while ("#" != str):
                files.write(str)
                str = input("请输入要写入的内容（#号结束）：")
        print("已结束！")
    except BaseException:
        print("文件写入失败，已退出！")
# fun()

def digui(n):
    if n < 3:
        return 1
    else:
        return digui(n-1) + digui(n-2)
# print(digui(8))

def high(h):
    count = h
    for i in range(10):
        h = h / 2
        count = count + h * 2
    print("总距离 %f %f" % (count,h))
high(100)