from TenSeeWeb.json_utils import result_handler, is_empty, error_handler
import requests, json
# 更新用户信息
from app.models import UserModel


def update_user(request):
    openId = request.META.get('HTTP_OPENID')
    realName = request.POST.get('realName')
    avatarUrl = request.POST.get('avatarUrl')
    nickName = request.POST.get('nickName')
    phone = request.POST.get('phone')
    tag = request.POST.get('tag')

    find_user = UserModel.objects.filter(openId=openId)
    if find_user.__len__() > 0:
        UserModel.objects.filter(openId=openId).update(avatarUrl=avatarUrl, nickName=nickName, tag=tag)
    else:
        UserModel.objects.create(openId=openId, avatarUrl=avatarUrl, nickName=nickName, tag=tag)

    if not is_empty(realName):
        UserModel.objects.filter(openId=openId).update(realName=realName)

    if not is_empty(phone):
        UserModel.objects.filter(openId=openId).update(phone=phone)

    user = UserModel.objects.filter(openId=openId).values()
    return result_handler(user[0])


# 用户列表
def get_user_list():
    user_list = UserModel.objects.all().order_by('-id')
    return result_handler(user_list)


# 根据openId查询用户
def get_user_by_openid(request):
    openId = request.META.get('HTTP_OPENID')
    user = UserModel.objects.filter(openId=openId).values()
    if user.__len__() > 0:
        return result_handler(user[0])
    else:
        return error_handler('请先登录')


# 删除用户
def delete_user(request):
    user_id = int(request.POST.get('id', default=0))
    UserModel.objects.filter(id=user_id).delete()
    return error_handler(None)


# 微信用户登录
def user_login(request):
    code = request.POST.get('code')
    appId = "wxc0e17eb1d875cc6a"
    appSecret = "7af371cf4d648b837d37d3bff67b5707"

    r = requests.get('https://api.weixin.qq.com/sns/jscode2session',
                     params={'appid': appId, 'secret': appSecret, 'js_code': code, 'grant_type': 'authorization_code'})
    key = json.loads(r.text)
    return result_handler(key)
