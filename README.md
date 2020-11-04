# crawlergo&xray 分布式

360 0Kee-Team 的 crawlergo动态爬虫 结合 长亭XRAY扫描器的被动扫描功能 (其它被动扫描器同理)

https://github.com/0Kee-Team/crawlergo

https://github.com/chaitin/xray

## 用法 

crawlergo及launcher脚本部署于本地，xray部署于多个分布式节点

#### 1. 下载xray最新的release, 下载crawlergo最新的release

注意,是下载编译好的文件而不是git clone它的库

#### 2. 把launcher.py和targets.txt放在crawlergo.exe同目录下

#### 3. 使用多台服务器，配置好并启动xray被动扫描，端口为自定义，同时修改proxy.txt文件中的地址及端口，一个一行

配置参数详见XRAY官方文档

#### 4. 配置好launcher.py的cmd变量中的crawlergo爬虫配置(主要是chrome路径改为本地路径)

配置参数详见crawlergo官方文档

#### 5. 把目标url写进targets.txt,一行一个url

#### 6. 用python3运行launcher.py ( XRAY被动扫描为启动的状态 )

https://github.com/aydcyhr/crawlergo&xray-Distributed
