"""TenSeeWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from TenSeeWeb import settings
from .middleware.ExceptionMiddleware import permission_denied, page_not_found, page_error
from app.handler import user_handler, home_handler, demand_handler
from app.views import upload, send_email
from django.contrib.staticfiles.urls import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload', upload),
    path('send_email', send_email),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    path('updateUser', user_handler.update_user),
    path('userList', user_handler.get_user_list),
    path('userByOpenId', user_handler.get_user_by_openid),
    path('login', user_handler.login),
    path('banner', home_handler.request_banner),
    path('update_banner', home_handler.update_banner),
    path('feeling', home_handler.request_feeling),
    path('update_feeling', home_handler.update_feeling),
    path('demands', demand_handler.demand_list),
    path('add_demand', demand_handler.add_demand),
    path('add_start', demand_handler.add_start),
    path('delete_demand', demand_handler.delete_demand),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = permission_denied
handler404 = page_not_found
handler405 = permission_denied
handler500 = page_error
