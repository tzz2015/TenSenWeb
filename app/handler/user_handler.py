"""
用户操作
"""
from app.service import user_service


# 更新用户
def update_user(request):
    return user_service.update_user(request)


# 用户列表
def get_user_list(request):
    return user_service.get_user_list()


# 登录
def login(request):
    return user_service.user_login(request)


# 根据openId获取用户信息
def get_user_by_openid(request):
    return user_service.get_user_by_openid(request)