<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_request_handler_api/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_request_handler_api

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

The web request base class based on xy_request_handler_base encapsulates common functions for easy and rapid development.

## Source Code Repositories

- <a href="https://github.com/xy-web-service/xy_request_handler_api.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-web-service/xy_request_handler_api.git" target="_blank">Gitee</a>

## Installation

```bash
# bash
pip install xy_request_handler_api
```

## How to use

> For details, please see [Demoes.py](./samples/xy_web_server_demo/source/Runner/RequestHandlerDemo/Demoes.py)
```python
# Demoes.py

from xy_request_handler_api.Api import Api

class Demo(Api):

    def get(self):
        self.write("Hello, xy_request_handler_api !")

```


##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b>
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee</a>

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

##### 2. Verify interface request
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

## License
xy_request_handler_api is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```