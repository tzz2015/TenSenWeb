from TenSeeWeb.json_utils import result_handler, is_empty
import requests, json
# 更新用户信息
from app.models import UserModel


def update_user(request):
    openId = request.META.get('HTTP_OPENID')
    realName = request.POST.get('realName')
    avatarUrl = request.POST.get('avatarUrl')
    nickName = request.POST.get('nickName')
    phone = request.POST.get('phone')
    defaults = {'openId': openId}
    UserModel.objects.update_or_create(openId=openId, avatarUrl=avatarUrl, nickName=nickName,
                                       defaults=defaults)
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


# 微信用户登录
def user_login(request):
    code = request.POST.get('code')
    appId = "wxc0e17eb1d875cc6a"
    appSecret = "7af371cf4d648b837d37d3bff67b5707"

    r = requests.get('https://api.weixin.qq.com/sns/jscode2session',
                     params={'appid': appId, 'secret': appSecret, 'js_code': code, 'grant_type': 'authorization_code'})
    key = json.loads(r.text)
    return result_handler(key)
