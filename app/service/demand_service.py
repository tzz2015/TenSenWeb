from TenSeeWeb.json_utils import format_data, result_handler
from app.models import DemandModel, UserModel


# 获取需求列表
def get_demand_list():
    demands = DemandModel.objects.all()
    return_list = []
    for demand in demands:
        item = format_data(demand)
        item['form'] = format_data(demand.form)
        return_list.append(item)
    return result_handler(return_list)


# 新增需求
def add_demand(request):
    demand = request.POST.get('demand')
    appId = request.META.get('HTTP_APPID')
    user = UserModel.objects.filter(appId=appId)[0]
    DemandModel.objects.create(demand=demand, start=0, form_id=user.id)
    return result_handler(None)


# 点赞需求
def add_start(request):
    demand_id = int(request.POST.get('id'))
    demand = DemandModel.objects.filter(id=demand_id)
    if demand.__len__() > 0:
        start = demand[0].start + 1
        DemandModel.objects.filter(id=demand_id).update(start=start)
    return result_handler(None)