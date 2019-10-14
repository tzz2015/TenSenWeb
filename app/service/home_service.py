from TenSeeWeb.json_utils import result_handler, is_empty, format_data
from app.models import BannerModel, FeelingsModel
import logging

logger = logging.getLogger('log')


# banner列表
def get_banner_list():
    return result_handler(BannerModel.objects.all().order_by('priority'))


# 语录列表
def get_feeling_list():
    feelings = FeelingsModel.objects.all().order_by('id')
    return_list = []
    for feeling in feelings:
        item = format_data(feeling)
        item['form'] = format_data(feeling.form)
        return_list.append(item)
    return result_handler(return_list)


# 更新轮播图
def update_banner(request):
    id = int(request.POST.get('id', default=0))
    imageUrl = request.POST.get('imageUrl')
    des = request.POST.get('des')
    priority = int(request.POST.get('priority', default=0))
    desColor = request.POST.get('desColor', default='#ffffff')
    if id > 0:
        BannerModel.objects.filter(id=id).update(imageUrl=imageUrl, des=des, priority=priority, desColor=desColor)
    else:
        BannerModel.objects.create(imageUrl=imageUrl, des=des, priority=priority, desColor=desColor)
    return result_handler(None)


# 更新感言
def update_feeling(request):
    id = int(request.POST.get('id', default=0))
    word = request.POST.get('word')
    form_id = int(request.POST.get('form_id', default=1))
    if id > 0:
        FeelingsModel.objects.filter(id=id).update(word=word, form_id=form_id)
    else:
        FeelingsModel.objects.create(word=word, form_id=form_id)
    return result_handler(None)
