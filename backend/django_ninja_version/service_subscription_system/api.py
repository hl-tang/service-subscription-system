from ninja import NinjaAPI, Schema
from django.contrib.auth.decorators import login_required, permission_required
from ninja.errors import ValidationError
from django.http import HttpRequest, HttpResponse

api = NinjaAPI()

# @api.exception_handler(ValidationError)
# def validation_errors(request, exc):
#     return HttpResponse("Invalid input", status=422)

@api.get("hello")
def hello_world(request):
    return {"hello": "world"}

class Message(Schema):
    msg: str

class WelcomeOut(Schema):
    hello: str

@api.get("welcome/", response={200: WelcomeOut, 401: Message})
def welcome(request):
    print(request.user)
    print(request.session.items())
    if request.user.is_authenticated:
        return 200, {"hello": request.user.username}
    else:
        return 401, {"msg": "please login"}

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