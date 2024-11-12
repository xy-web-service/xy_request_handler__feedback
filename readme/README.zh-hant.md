<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_request_handler__feedback/readme/README.zh-hant.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_request_handler__feedback

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## 說明

基於xy_request_handler_api的回饋請求業務類，封裝了常用功能，方便快速開發.

## 程式碼庫

| [Github](https://github.com/xy-web-service/xy_request_handler__feedback.git)         | [Gitee](https://gitee.com/xy-opensource/xy_request_handler__feedback.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_request_handler__feedback.git)          |
| ----------- | -------------|---------------------------------------|


## 安裝

```bash
# bash
pip install xy_request_handler__feedback
```

## 使用

##### 1. 引入xy_django_app_feedback模型.(xy_request_handler__feedback依賴該模型,必須引入)

> 詳情請查看 [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Demo",
    "Resource",
    "Media",
    "xy_django_app_information",
    "xy_django_app_resource",  # xy_django_app_feedback将调用xy_django_app_resource的MImage模型
    "xy_django_app_feedback",
]
```


##### 2. 引入xy_request_handler__feedback.

> 詳情請查看 [Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py)

```python
# Runner.py
from xy_request_handler__feedback.Feedbacks import Feedback
# 137行
urls = [
    (r"/", Index),
    (r"/query", Query),
    (r"/add", Add),
    (r"/delete", Delete),
    (r"/update", Update),
    (r"/demo", Demo),
    (r"/feedback", Feedback),
]
# ...
```

```bash
# bash
xy_web_server -w tornado start
# 启动服务后访问 http://127.0.0.1:8400/feedback?username=mobile&email=yuyangit.0515@qq.com&text=hello_world
# 相应结果如下:
# {
#     "data": {},
#     "message": "发送成功",
#     "code": 0
# }
# 开启另一个终端窗口, 执行如下命令
xy_web_server -w django start
# 启动服务后访问 http://127.0.0.1:8401/admin 进入后台后, 访问反馈管理进行验证
```

![反馈图片](./feedback_0.png)


##### 1. 運行 [範例工程](../samples/xy_web_server_demo)

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 以下倉庫

| [Github](https://github.com/xy-web-service/xy_web_server.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_server.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_server.git)          |
| ----------- | -------------|---------------------------------------|

## 許可證
xy_request_handler__feedback 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```