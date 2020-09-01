'''
移动端书取得爬取

常见抓包工具：
    - fiddler，青花瓷，miteproxy

- 1.配置下fiddler的端口
- 2.将手机和fiddler所在的电脑处在同一网段下（pc开启wifi，手机连接）
- 3.在手机中访问fiddler的ip+port：192.168.xxxx.xxxx：50816，在当前网页中点击对应链接下载证书
- 4.在手机中安装并信任证书
- 5.设置手机网络代理：开启代理==》fiddler对应pc端的ip地址和fiddler端口号
'''
# frida 框架
# hook 啥意思？
