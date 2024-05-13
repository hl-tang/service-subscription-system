from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from ninja import NinjaAPI, Router
from ninja import Form, Query
from django.http import HttpRequest, HttpResponse
# from django.core.exceptions import ValidationError
import hashlib  # 导入哈希库

from django.contrib.auth.models import User
# from .models import User
from .schemas import RegisterIn, LoginIn

user_login_api = Router()

# 为什么访问http://127.0.0.1:8000/api/auth_login/的时候("/auth_login/")，("/login/")的处理函数也输出了？

# 使用自带的auth_user表     from django.contrib.auth.models import User
@user_login_api.post("/auth_register/")
def auth_register(request, payload: RegisterIn):
    if User.objects.filter(username=payload.username).exists():
        return {"message": "Username already exists"}
    user = User.objects.create_user(username=payload.username, password=payload.password)
    # create_user()密码会自动哈希, 但这个create_user()只有自带的auth_user表有
    # user = User.objects.create(username=payload.username, password=payload.password)
    return {"message": "User created successfully", "username": user.username, "pwd": user.password}

@user_login_api.post("/auth_login/")
# def auth_login(request, username: str, password: str): #这种写法带query parameter, url为login/?username=string&password=string
def auth_login(request: HttpRequest, response: HttpResponse, payload: LoginIn): #这样用payload参数代表request body   url为login/
    print(f"username: {payload.username}, password: {payload.password}")
    # authenticate()自动调用create_user()时同样的哈希计算
    user = authenticate(request, username=payload.username, password=payload.password) #就是检查用户名对应的口令
    print(user)
    print(type(user))
    if user is not None:
        login(request, user) #就是Session表里添加一条记录,同时把SessionID的Cookie发到发起请求的client
        # 怎么设置cookie 看django-ninja的文档 https://django-ninja.dev/guides/response/temporal_response/
        # 主要是 response: HttpResponse
        response.set_cookie("cookie", "delicious") #浏览器还是没有cookie !!!(前端需要设置axios.defaults.withCredentials = true;)
        # request.session["info"] = {"id": user.id, "username": user.username} #其实login(request, user)内部就是做了session的处理
        # response.set_cookie("info", {"id": user.id, "username": user.username}) #看了眼其他网站的cookie没有把Value设置成对象的，这样前端也不好提取
        response.set_cookie("username", user.username)
        return {"message": "Login successful", "username": user.username}
    else:
        return {"message": "Invalid credentials"}

@user_login_api.get("/auth_logout/")
def auth_logout(request, response: HttpResponse):
    print(request.user)
    logout(request) #把login()做的事情抵消了,session表删掉这个用户的session,删掉client的sessionid的cookie
    response.delete_cookie('username') #然后前端浏览器真的把这个cookie删了
    print(request.user)
    return {"message": "Logged out successfully", "username": request.user.username}

# 以上是用django.contrib.auth自带的，以及User模型
#######################
#######################
# 以下手撸

# 自己撸, User models也不用自带的auth_user, 包括自己的authenticate()
""" @user_login_api.post("/register/")
def register(request, payload: RegisterIn):
    if User.objects.filter(username=payload.username).exists():
        return {"message": "Username already exists"}
    hashed_pwd = hashlib.sha256(payload.password.encode()).hexdigest()
    user = User.objects.create(username=payload.username, password=hashed_pwd)
    return {"message": "User created successfully", "username": user.username, "pwd": user.password}

@user_login_api.post("/login/")
def login(request, payload: LoginIn):
    print(f"username: {payload.username}, password: {payload.password}")
    hashed_pwd = hashlib.sha256(payload.password.encode()).hexdigest()
    user = User.objects.filter(username=payload.username, password=hashed_pwd).first()
    print(user)
    print(type(user))
    if user is not None:
        # 怎么手撸login
        # 服务端生成随机字符串；发送给浏览器写到cookie中；服务端写入到session中
        request.session["info"] = {"id": user.id, "username": user.username}
        # response.set_cookie('username', user.username, max_age=3600 * 24 * 15)
        return {"message": "Login successful", "username": user.username}
    else:
        return {"message": "用户名密码不一致"} """
