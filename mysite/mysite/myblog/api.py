from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password
from myblog.models import Classes, UserInfo
from myblog.toJson import Classes_data, UserInfo_data
import json


@api_view(['GET', 'POST'])
def api_test(request):
    # if request.method == 'POST':
    #     return Response("post")
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
            data_item["userlist"].append(user_data)
        data['classes'].append(data_item)
    # data = json.dumps(data)
    return Response(data)

@api_view(['GET', 'POST'])    
def getMenuList(request):
    allClasses = Classes.objects.all()

    # 整理数据为json
    data=[]
    for c in allClasses:
        # 设计单条数据的结构
        data_item={
        "id":c.id,
        "text":c.text
        }
        data.append(data_item)
    return Response(data)

@api_view(["GET","POST"])   
def getUserList(request):
    # allClasses
    menuId = request.GET["id"]
    menu = Classes.objects.get(id =menuId)
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
