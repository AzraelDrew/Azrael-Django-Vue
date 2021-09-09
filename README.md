## 安装 Nginx

```shell
sudo apt install nginx
```

## 查看 nginx 是否安装成功

```shell
nginx -v

/usr/sbin/nginx：主程序
/etc/nginx：存放配置文件
/usr/share/nginx：存放静态文件
/var/log/nginx：存放日志
```

## 命令

```shell
sudo service nginx start

sudo service nginx stop

sudo service nginx restart

如果安装了apache页面会变为apache的页面

```

## 配置

```shell
sudo vim /etc/nginx/sites-available/default
```
