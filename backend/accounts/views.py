from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password1 = data.get("password1")
        password2 = data.get("password2")

        if password1 != password2:
            response_data = {"message": "비밀번호가 일치하지 않습니다."}
            return JsonResponse(response_data, status=400)

        user = User(username=username, email=email)
        user.set_password(password1)
        user.save()

        response_data = {"message": "회원가입이 성공적으로 완료되었습니다."}
        return JsonResponse(response_data)


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            response_data = {
                "message": "로그인 성공",
                "user": {"id": user.id, "email": user.email},
            }
            return JsonResponse(response_data)
        else:
            response_data = {"message": "로그인 실패. 이메일과 비밀번호를 확인하세요."}
            return JsonResponse(response_data, status=400)


@csrf_exempt
def user_logout(request):
    if request.method == "POST":
        logout(request)
        response_data = {"message": "로그아웃 성공"}
        return JsonResponse(response_data)