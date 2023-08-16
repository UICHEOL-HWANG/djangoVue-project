# accounts/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    # 기타 필드들 및 메서드들 추가

    def __str__(self):
        return self.username