from TenSeeWeb.json_utils import result_handler, is_empty, format_data
from app.models import BannerModel, FeelingsModel
import logging

logger = logging.getLogger('log')


# banner列表
def get_banner_list():
    return result_handler(BannerModel.objects.all().order_by('priority'))


# 语录列表
def get_feeling_list():
    feelings = FeelingsModel.objects.all().order_by('-id')
    return_list = []
    for feeling in feelings:
        item = format_data(feeling)
        item['form'] = format_data(feeling.form)
        return_list.append(item)
    return result_handler(return_list)
