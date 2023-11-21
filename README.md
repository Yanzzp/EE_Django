# EE_Django

### 云端：

[EE_Django(yanzzp.xyz)](http://yanzzp.xyz:8002/)端口:8002

```sh
# 自动将本地分支硬重置到到git origin/main
cd ./shell
./auto_pull.sh
# 一键启动云服务器
./run_server.sh
```



### 本地部署教程：

首先先创建一个虚拟环境，激活虚拟环境



输入以下命令来安装指定的库
``` shell
pip install -r requirement.txt
```



输入以下命令来在本地运行服务器

``` shell
python manage.py runserver
```

### Windows下使用git bash

``` shell
# 安装git并添加git命令到终端中
# 使用以下命令来简单的push
./puth.bat  #默认提交信息为"update"
# 或者
./puth.bat "提交信息或者巴拉巴拉"

