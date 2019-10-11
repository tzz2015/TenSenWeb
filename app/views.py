from django.shortcuts import render
from TenSeeWeb.json_utils import format_data, result_handler

# Create your views here.
from TenSeeWeb import settings
import os


def upload(request):
    """
    上传文件
    :param request:
    :return:
    """
    file = request.FILES.get("file")
    f = open(os.path.join(settings.MEDIA_ROOT, "upload", file.name), "wb")
    for chunk in file.chunks():
        f.write(chunk)
    f.close()
    return result_handler(os.path.join(settings.MEDIA_URL, "upload", file.name))
