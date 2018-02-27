# dic1 = {"str":"str","str1":"str1"}
# print(dic1.items())

def fun(list1):
    list02 = []
    temp = []
    j = list1[0]
    temp.append(j)
    for i in list1[1:]:
        if j == i:
            temp.append(i)
        else:
            list02.append(temp)
            temp = []
            temp.append(i)
        j = i
    list02.append(temp)
    return list02

list01 = [1,1,0,2,2,2,4,3,3,4,2,0,0]
# print(fun(list01))
k = 0;
for i in list01:
    if k == 0:
        del list01[1]
    k = k + 1;
# print(list01)

def bubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) -1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        return nums

def fun():
    list01 = input().split(',')
    print(bubbleSort(list01))
#
# fun();

def count(num,str):
    str = str + 1
    if str > 6:
        return num;
    else:
        num = (num + 1) * 2;
        return count(num,str)

couts = count(1,1)

for i in range(6):
    if i == 5:
        print(couts)
        break
    couts = couts / 2 - 1