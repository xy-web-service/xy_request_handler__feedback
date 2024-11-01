<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:23
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:38
 * @FilePath: /xy_request_handler_api/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_request_handler_api

- [简体中文](readme/README_zh_CN.md)
- [繁体中文](readme/README_zh_TW.md)
- [English](readme/README_en.md)

## 说明

基于xy_request_handler_base的api请求基类，封装了常用功能，方便快速开发.

## 源码仓库

- <a href="https://github.com/xy-web-service/xy_request_handler_api.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-web-service/xy_request_handler_api.git" target="_blank">Gitee地址</a>

## 安装

```bash
# bash
pip install xy_request_handler_api
```

## 使用

> 详情请查看 [Runner.py](./samples/xy_web_server_demo/source/Runner/Runner.py)
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
# 启动服务后访问 http://127.0.0.1:8400/feedback?username=im_test
# 开启另一个终端窗口, 执行如下命令
xy_web_server -w django start
# 启动服务后访问 http://127.0.0.1:8401/admin 进入后台后, 访问反馈管理进行验证
```

##### 运行 [样例工程](./samples/xy_web_server_demo)

> 样例工程具体使用方式请移步 <b style="color: blue">xy_web_server.git</b> 下列仓库
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github地址</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee地址</a>

```bash
# bash

# 当前目录为xy_request_handler_api的git本地仓库所在目录
# 切换到工程目录
cd ./samples/xy_web_server_demo

# 启动样例工程的Tornado服务
xy_web_server -w tornado start

# 默认启动的Tornado服务url地址是: http://127.0.0.1:8400
# 浏览器打开访问 http://127.0.0.1:8400/demo 进行验证
```

##### 2. 检验接口请求
```python
# Python解释器
# 以下是示例代码，需要在您的应用中实现
# 用来进行测试接口请求
# Python解释器运行以下代码
import requests
post_json_data = {"test":"post json data text"}
url = "http://127.0.0.1:8400/demo"
resp = requests.post(url, json=post_json_data)
resp_json = resp.json()
{'code': 0,
 'message': '请求成功',
 'data': {'resp_data_json': {'test': 'post json data text'}}}
```


## 许可证
xy_request_handler_api 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 捐赠
如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./readme/Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```