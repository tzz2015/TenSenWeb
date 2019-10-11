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
from app.handler import user_handler, home_handler, demand_handler
from app.views import upload
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload', upload),
    path(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    path('updateUser', user_handler.update_user),
    path('banner', home_handler.request_banner),
    path('feeling', home_handler.request_feeling),
    path('demands', demand_handler.demand_list),
    path('add_demand', demand_handler.add_demand),
    path('add_start', demand_handler.add_start),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
