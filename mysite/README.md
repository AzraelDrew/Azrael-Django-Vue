## 安装 Django

```shell
pip3 install django
```

## 使用 django

```shell
mkdir DjangoProject

cd DjangoProject

django-admin startproject mysite

cd mysite

python3 manage.py runserver

python3 manage.py startapp myblog

python3 manage.py makemigrations

python3 manage.py migrate
```

## MTV

- 访问地址 -> url.py -> views.py -> templates

## 创建管理员

```shell
python3 manage.py createsuperuser

```

## 数据合并到 mysql

```shell
python3 manage.py migrate --database mysql
```

## djangorestframework

```shell
pip3 install djangorestframework


在myblog下新建api.py
```

### Cors跨源请求

```shell
pip3 install django-cors-headers

在setting.py中的INSTALLED_APP中添加
'corsheaders'

在setting.py中的MIDDLEWARE中添加
"corsheaders.middleware.CorsMiddleware",
"django.middleware.common.CommonMiddleware",

在setting.py末尾添加
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

```

