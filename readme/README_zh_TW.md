<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_request_handler_api/readme/README_zh_TW.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_request_handler_api

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 說明

基於xy_request_handler_base的web請求基類，封裝了常用功能，方便快速開發.

## 程式碼庫

- <a href="https://github.com/xy-web-service/xy_request_handler_api.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-web-service/xy_request_handler_api.git" target="_blank">Gitee位址</a>

## 安裝

```bash
# bash
pip install xy_request_handler_api
```

## 使用

> 詳情請查看 [Demoes.py](./samples/xy_web_server_demo/source/Runner/RequestHandlerDemo/Demoes.py)

```python
# Demoes.py

from xy_request_handler_api.Api import Api

class Demo(Api):

    def get(self):
        self.write("Hello, xy_request_handler_api !")

```

##### 1. 運行 [範例工程](../samples/xy_web_server_demo)

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 以下倉庫
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github位址</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee位址</a>

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

##### 2. 檢驗介面請求
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

## 許可證
xy_request_handler_api 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```