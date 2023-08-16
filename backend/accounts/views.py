# accounts/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserProfile

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        # 회원가입 로직 수행
        user = UserProfile(username=username, email=email)
        user.save()

        response_data = {'message': '회원가입이 성공적으로 완료되었습니다.'}
        return JsonResponse(response_data)