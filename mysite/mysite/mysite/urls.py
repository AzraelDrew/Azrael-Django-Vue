"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings  # 导入路由配置
from django.conf.urls.static import static  # 静态资源
from myblog import views, api
# 路由配置(被允许的访问)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),  # 当访问index/时会去views.py中寻找index这个函数
    path('', views.index),  # 首页路由
    path('classes/', views.classes),
    # api接口1
    path('api/', api.api_test),
    path("get-menu-list/",api.getMenuList),
    path("get-user-list/",api.getUserList),
    path("login/",api.toLogin),
    path("register/",api.toRegister),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDID_URL, document_root=settings.MEDID_ROOT)
