import smtplib
from email.header import Header
from email.mime.text import MIMEText

from django.http import HttpResponse
from TenSeeWeb.json_utils import format_data, result_handler

from TenSeeWeb import settings
import os

import logging

log = logging.getLogger('django')


def default(request):
    return result_handler('老铁，你来了，我看，你来了就别走了😏')


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


def send_email(request):
    """
       测试邮箱
       :param request:
       :return:
       """
    send_email_msg("测试邮件发送")
    return HttpResponse('测试邮件已发出请注意查收')


def send_email_msg(msg):
    # 第三方 SMTP 服务
    mail_host = settings.EMAIL_HOST  # 设置服务器
    mail_user = settings.DEFAULT_FROM_EMAIL  # 用户名
    mail_pass = settings.EMAIL_HOST_PASSWORD  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

    sender = settings.DEFAULT_FROM_EMAIL
    receivers = ['1374329135@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("ppyy", 'utf-8')
    message['To'] = Header("you", 'utf-8')

    subject = '错误上报'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
