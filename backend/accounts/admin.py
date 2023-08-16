# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# UserProfile 모델에 대한 Admin 설정
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # 필드 목록 표시
    search_fields = ('username', 'email')  # 검색 가능한 필드

# UserProfileAdmin을 사용자(User) 모델의 Admin으로 등록
admin.site.unregister(User)  # 기본 User 모델 언레지스트
admin.site.register(User, UserAdmin)  # User 모델을 기본 UserAdmin으로 등록
admin.site.register(UserProfile, UserProfileAdmin)  # UserProfile 모델을 UserProfileAdmin으로 등록