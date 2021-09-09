from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from myblog.models import SiteInfo, Classes, UserInfo
# Create your views here.

# 当请求index时就会执行下面打函数


def index(request):
    # 在这里写入业务逻辑
    # 在这里读取数据库

    # 站点基础信息
    siteinfo = SiteInfo.objects.all()[1]
    # 菜单分类
    classes = Classes.objects.all()
    # 全部用户
    userlist = UserInfo.objects.all()
    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist,
    }
    return render(request, "index.html", data)  # index.html 默认在templates文件夹下


def classes(request):
    # 站点基础信息
    siteinfo = SiteInfo.objects.all()[1]
    # 菜单分类
    classes = Classes.objects.all()
    # 用户列表

    # 路由传参
    # choosed_id = request.GET['id']
    # print(choosed_id)
    # choosed = Classes.objects.get(id=choosed_id)
    # userlist = UserInfo.objects.filter(belong=choosed)

    # choosed_id = request.GET['id']
    # print(choosed_id)
    # choosed = Classes.objects.filter(id=choosed_id)
    # if choosed:
    #     userlist = UserInfo.objects.filter(belong=choosed[0])
    # else:
    #     # userlist = []
    #     # return HttpResponse("无结果")
    #     # data = {
    #     #     "value": "无结果"
    #     # }
    #     # return JsonResponse(data)
    #     return redirect("/")

    try:
        choosed_id = request.GET['id']
        print(choosed_id)
        choosed = Classes.objects.filter(id=choosed_id)
    except:
        return redirect("/")

    if choosed:
        userlist = UserInfo.objects.filter(belong=choosed[0])
    else:
        userlist = []

    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist,
    }
    return render(request, "classes.html", data)
