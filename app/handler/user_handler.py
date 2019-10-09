"""
用户操作
"""
from app.service import user_service


def update_user(request):
    return user_service.update_user(request)
