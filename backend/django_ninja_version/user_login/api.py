from ninja import NinjaAPI, Router
from django.contrib.auth import authenticate, login, logout
from ninja import Form, Query
from .models import User
from django.core.exceptions import ValidationError
import hashlib  # 导入哈希库

user_login_api = Router()


""" @user_login_api.post("/register/")
def register_user(request, username: str = Form(...), password: str = Form(...)):
    if User.objects.filter(username=username).exists():
        return {"message": "Username already exists"}
    user = User.objects.create_user(username=username, password=password)
    return {"message": "User created successfully"}

@user_login_api.post("/login/")
def login_user(request, username: str, password: str):
    print(f"username: {username}, password: {password}")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}

@user_login_api.get("/logout/")
def logout_user(request):
    logout(request)
    return {"message": "Logged out successfully"}

@user_login_api.get("/protected/")
def protected_route(request):
    if not request.user.is_authenticated:
        return 401, {"message": "Unauthorized"}
    return {"message": "Welcome to protected route!"} """

@user_login_api.post("/register/")
def register(request):
    if request.method == 'POST':  # 当请求方式为 POST 时
        input_username = request.POST.get('username')  # 从表单中获取用户名
        _input_password_1 = request.POST.get('password')  # 从表单中获取密码
        # _input_password_2 = request.POST.get('confirmPassword')  # 从表单中获取确认密码

        # # 检查密码和确认密码是否一致
        # if _input_password_1 != _input_password_2:
        #     raise ValidationError("密码和确认密码不一致，请重新输入")  # 抛出检验错误异常

        # 检查用户名是否已存在
        if User.objects.filter(username=input_username).exists():
            raise ValidationError('用户名已存在，请换一个用户名试试。')  # 如果存在相同用户名，抛出检验错误异常

        # input_password = hashlib.md5(_input_password_1.encode()).hexdigest()  # 使用 MD5 哈希加密密码
        # 利用 User 模型的 create 方法创建用户
        user = User.objects.create(
            username=input_username, password=_input_password_1)
        user.save()  # 保存用户
        # return render(request, 'login.html')  # 返回已渲染模板 login.html，进行重定向
    # else:
        # 如果不是 POST 请求，返回已渲染模板 register.html
        # return render(request, 'register.html')

@user_login_api.post("/login/")
def login(request):
    if request.method == 'POST':  # 当请求方式为 POST 时，表示用户正在登录
        input_username = request.POST.get('username')  # 从表单中得到用户名
        _input_password = request.POST.get('password')  # 从表单中得到密码
        input_password = hashlib.md5(
            _input_password.encode()).hexdigest()  # 使用 MD5 哈希加密密码
        user = User.objects.filter(
            username=input_username).first()  # 从数据库中首先查询用户信息

        if not user or user.password != input_password:  # 如果用户不存在或者输入的哈希密码与数据库中不符合
            raise ValidationError("用户名或密码匹配不一致")  # 抛出检验错误异常
        # 返回已渲染模板 index.html，同时把用户名放置于 context 中传递给 index.html 以渲染页面

        # return render(request, 'index.html', context={"username": user.username})
    # else:
        # return render(request, 'login.html')  # 如果不是 POST 请求，返回已渲染模板 login.html
