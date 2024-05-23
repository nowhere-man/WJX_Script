## 项目介绍

使用**selenium**实现自定义的批量刷问卷星问卷，题型涉及：单选、多选、排序、量表、填空

**主要功能**：

1. 自定义选项比例，如[男:女]=[7:3]
2. 选项之间相互关联，如男生更倾向于工科，则男生的专业选择[理工类:文史类] = [8:2]，女生的专业选择[理工类:文史类] = [2:8]
3. 可以更换ip填写问卷，北京、陕西、湖南等...

## 配置步骤

1.查看chrome浏览器版本（125.0）

![image](https://github.com/paipaix1/WJX_Script/assets/156734592/901997b7-320b-4bac-a82e-32dbf48addcd)


2.进入网站：[Chrome for Testing availability (googlechromelabs.github.io)](https://googlechromelabs.github.io/chrome-for-testing/)下载对应版本的Stable的chromedriver Win64

![image](https://github.com/paipaix1/WJX_Script/assets/156734592/1fc5dcb0-2cb2-41f3-abfd-d90c88a6e38b)


3.解压chromedriver.exe文件，放置在chrome的安装目录下

![image](https://github.com/paipaix1/WJX_Script/assets/156734592/b5de895e-6180-410d-b325-5120635f60ff)


4.设置环境变量，在系统变量的path中添加Application的路径，如C:\Program Files\Google\Chrome\Application

5.如果selenium打开网页闪退，将selenium的版本降为4.1.1。运行结束，浏览器自动关闭是正常现象。

## **使用步骤**

**1.在Config.py中自定义配置**

​	self.batch：设置想要刷的问卷数量

​	self.proxy：是否使用ip代理

​	self.questions：对每个问题进行配置

**2.运行ZM_IP.py获取ip地址存入ip.json**

​	put_request函数：选择不同ip地理位置

​	如果运行没问题，进入下一步

​	如果有问题手动获取ip网站(选择json格式)，写入ip.json

**3.运行Single_Test.py单次刷问卷进行测试**

**4.运行Run.py即可完成批量刷问卷**

注意：如果网页加载过慢，大抵是ip质量不行，选用时效长的ip即可
