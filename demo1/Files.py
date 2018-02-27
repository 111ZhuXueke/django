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
fun()