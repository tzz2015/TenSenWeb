from app.service import home_service


# Banner列表
def request_banner(request):
    return home_service.get_banner_list()


# Banner列表
def update_banner(request):
    return home_service.update_banner(request)


# 删除Banner
def delete_banner(request):
    return home_service.delete_banner(request)


# 感言列表
def request_feeling(request):
    return home_service.get_feeling_list()


# 感言列表
def update_feeling(request):
    return home_service.update_feeling(request)


# 删除Banner
def delete_feeling(request):
    return home_service.delete_feeling(request)


# tabBar开关
def switch_tab_bar(request):
    return home_service.switch_tab_bar(request)
