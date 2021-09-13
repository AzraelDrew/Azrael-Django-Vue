from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password
from myblog.models import Classes, UserInfo ,SiteInfo
from myblog.toJson import Classes_data, UserInfo_data
import json


# api接口
@api_view(['GET', 'POST'])
def api_test(request):
    # 获取所有分类
    classes = Classes.objects.all()
    # print(classes)
    # classes_data = Classes_data(classes, many=True)  # many=True  序列化多条数据
    # userlist = UserInfo.objects.all()
    # userlist_Data = UserInfo_data(userlist, many=True)  # many=True
    # data = {
    #     'classes': classes_data.data,
    #     'userlist': userlist_Data.data,
    # }

    data = {
        'classes': [

        ]
    }
    for c in classes:
        data_item = {
            "id": c.id,
            "text": c.text,
            "userlist": [],
        }
        userlist = c.userinfo_classes.all()
        for user in userlist:
            user_data = {
                'id': user.id,
                "nickName": user.nickName,
                "headImg": str(user.headImg)
            }
            data_item["userlist"].append(user_data)   #将user_data添加到data_item
        data['classes'].append(data_item)
    return Response(data)

# 获取菜单列表
@api_view(['GET', 'POST'])    
def getMenuList(request):
    # 获取所有分类
    allClasses = Classes.objects.all()
    # 获取id=1网站信息
    siteinfo = SiteInfo.objects.get(id=1)
    siteinfo_data={
    "sitename":siteinfo.title,
    "logo":"http://localhost:8000/"+str(siteinfo.logo) #强制转换为字符串
    }
    # 整理数据为json
    menu_data=[]
    for c in allClasses:
        # 设计单条数据的结构
        data_item={
        "id":c.id,
        "text":c.text
        }
        menu_data.append(data_item)
    data={
    "menu_data":menu_data,
    "siteinfo":siteinfo_data,
    }
    return Response(data)

# 获取用户列表
@api_view(["GET","POST"])   
def getUserList(request):
    # allClasses
    menuId = request.GET["id"]
    menu = Classes.objects.get(id=menuId)
    print(menu)
    userlist = UserInfo.objects.filter(belong=menu)
    print(userlist)

    # 开始整理数据
    data=[]
    for user in userlist:
        data_item={
        "id":user.id,
        "headImg":str(user.headImg),
        "nickName":user.nickName
        }
        data.append(data_item)
    return Response(data)


# 登录验证
@api_view(["POST"])
def toLogin(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    # 查询用户数据库
    user = User.objects.filter(username=username)
    if len(user)>0:
        # print(user)
        # auth_user = authenticate(username=username,password=password)
        # print(auth_user)
        user_pwd = user[0].password
        # 验证密码
        auth_pwd = check_password(password,user_pwd)
        print(auth_pwd)
        if auth_pwd:
            # 更新或创建token
            token = Token.objects.update_or_create(user=user[0])
            # 获取token
            token = Token.objects.get(user = user[0])
            print(token.key)
            data={
            'token':token.key
            }
            return Response(data)
        else:
            return Response("pwdeer")
    else:
        return Response("none")
    return Response("esk")

# 注册
@api_view(["POST"])
def toRegister(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    print(username,password,password2)
    # 用户是否存在
    user = User.objects.filter(username=username)
    if user:
        return Response("sameName")
    else:
        # 创建用户
        newPwd = make_password(password,username)
        print(newPwd)
        newUser = User(username=username,password=newPwd)
        newUser.save()
    return Response("ok")

# 上传logo
@api_view(["POST","PUT"])
def uploadLogo(request):
    if request.method == "PUT":
        sitename = request.POST["sitename"]
        print(sitename)
        old_info = SiteInfo.objects.get(id=1)
        old_info.title = sitename
        new_info = SiteInfo.objects.get(id=2)
        old_info.logo = new_info.logo
        old_info.save()
        return Response("OK")
    img = request.FILES['logo']
    print(img)
    test_siteLogo = SiteInfo.objects.get(id=2)
    test_siteLogo.logo = img
    test_siteLogo.save()
    data={
    "img":str(test_siteLogo.logo)
    }
    return Response(data)