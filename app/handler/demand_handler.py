from app.service import demand_service


# 需求列表
def demand_list(request):
    return demand_service.get_demand_list()


# 增加需求
def add_demand(request):
    return demand_service.add_demand(request)


# 点赞
def add_start(request):
    return demand_service.add_start(request)
