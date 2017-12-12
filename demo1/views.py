from django.shortcuts import render
from demo1.models import users
import socket,sys
# Create your views here.
## 用户登录
def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        try:
            user = users.objects.get(name=uname, password=pwd)
            request.session["user"] = user.name
            userlist = users.objects.all()
            return render(request, 'index.html', {'userlist': userlist})
        except ValueError:
            return render(request, 'login.html', {'status': '用户名或密码错误!'})
    else:
        return render(request,'login.html')

## 新增用户
def saveUsers(request):
    if request.method == 'POST':
        name = request.POST['name']
        pwd = request.POST['pwd']
        address = request.POST['address']
        users(name=name,password=pwd,address=address).objects.create()
        return render(request, 'addUser.html?change=success')
    return render(request,'addUser.html')

def myWebInternet(request):
    port = 80
    host = sys.argv[1]
    filename = sys.argv[2]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.sendall(filename + "\r\n")

    while 1:
        buf = s.recv(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)