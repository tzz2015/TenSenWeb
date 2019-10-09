from TenSeeWeb.json_utils import result_handler, is_empty

# 更新用户信息
from app.models import UserModel


def update_user(request):
    appId = request.POST.get('appId')
    realName = request.POST.get('realName')
    avatarUrl = request.POST.get('avatarUrl')
    nickName = request.POST.get('nickName')
    defaults = {'appId': appId}
    UserModel.objects.update_or_create(appId=appId, avatarUrl=avatarUrl, nickName=nickName,
                                       defaults=defaults)
    if not is_empty(realName):
        UserModel.objects.filter(appId=appId).update(realName=realName)
    user = UserModel.objects.filter(appId=appId).values()
    return result_handler(user[0])
