from app.service import home_service


# Banner列表
def request_banner(request):
    return home_service.get_banner_list()


# Banner列表
def update_banner(request):
    return home_service.update_banner(request)


# 感言列表
def request_feeling(request):
    return home_service.get_feeling_list()


# 感言列表
def update_feeling(request):
    return home_service.update_feeling(request)
