import os
from socket import gethostbyname,gethostname

host = gethostbyname(gethostname())
os.system('arp -a > temp.txt')
i = 0
print(host[:4])
with open('temp.txt') as fp:
    for line in fp:
        line = line.split()[:2]
        # 过滤第一个 []、第二个 [借口\192.168.254.47]/本机、第三个 [Internet, 地址]
        if line and line[0].startswith(host[:4]) and (not line[0].endswith('255')):
            print(line)
            i = i + 1
print(i)