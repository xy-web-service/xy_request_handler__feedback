<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_request_handler__feedback/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_request_handler__feedback

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

Feedback request business class based on xy_request_handler_api, encapsulating common functions for fast development.

## Source Code Repositories

- <a href="https://github.com/xy-web-service/xy_request_handler__feedback.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-opensource/xy_request_handler__feedback.git" target="_blank">Gitee</a>  
- <a href="https://gitcode.com/xy-opensource/xy_request_handler__feedback.git" target="_blank">GitCode</a>  

## Installation

```bash
# bash
pip install xy_request_handler__feedback
```

## How to use

##### 1. Import the xy_django_app_feedback model. (xy_request_handler__feedback depends on this model and must be imported)

> For details, please see [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

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


##### 2. Import xy_request_handler__feedback.

> For details, please see [Runner.py](../samples/xy_web_server_demo/source/Runner/Runner.py)

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

##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b>
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github</a>  
> - <a href="https://gitee.com/xy-opensource/xy_web_server.git" target="_blank">Gitee</a>  
> - <a href="https://gitcode.com/xy-opensource/xy_web_server.git" target="_blank">GitCode</a>  

## License
xy_request_handler__feedback is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```