from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# 기본 UserAdmin 클래스 사용
admin.site.unregister(User)  # 기본 User 모델 언레지스트
admin.site.register(User, UserAdmin)  # User 모델을 기본 UserAdmin으로 등록