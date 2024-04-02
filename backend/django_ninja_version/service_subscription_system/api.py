from ninja import NinjaAPI
from django.contrib.auth.decorators import login_required, permission_required

api = NinjaAPI()

@api.get("hello")
def hello_world(request):
    return {"hello": "world"}

@api.get("welcome/")
def welcome(request):
    print(request.user)
    print(request.session.items())
    if request.user.is_authenticated:
        return {"hello": request.user.username}
    else:
        return {"msg": "please login"}

# 好像没登录也可以得到return的返回
@login_required(login_url="/api/login/")
@api.get("blog/")
def view_blog(request):
    print(request.user)
    return {"msg": "ok"}
############
############
@api.get("welcome2/")
def welcome2(request):
    if request.user.is_authenticated:
        print(request.user)
        return {"hello": request.user.username}
    else:
        return {"msg": "please login"}