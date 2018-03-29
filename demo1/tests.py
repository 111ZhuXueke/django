# 题目2：用Python编写程序，输入一年份，判断该年份是否是闰年(366)并输出结果。 
#        注：凡符合下面两个条件之一的年份是闰年。 
#   （1） 能被4整除但不能被100整除。 
#   （2） 能被400整除。
year=0      #输入年份
try:
    year=int(input('请输入一年份：'))      #输入年份
except ValueError:
    print('数字输入无效！')
if (year%4==0 and year%100!=0) or year%400==0:  #判断年份是否是闰年
    print('%d是闰年！'%year)
else:
    print('%d不是闰年'%year)