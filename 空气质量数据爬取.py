###################################################
'''

分析：
    - 1.改变页面中的查询条件，点击查询按钮，通过抓包工具捕获相关的数据包
    - 2.该数据包中发现： post请求携带一个动态变化且加密的请求参数 d，并且请求到的数据也是一组密文数据
    - 3.该请求是ajax请求
    - 4.通过火狐定位到搜索按钮绑定的click点击事件（getData）
    - 5.剖析getData函数的实现：
        - type=='hour'
        - getAQIData():getWeatherData()：发现了这两个函数的调用
    - 6.getgetAQIData()和 getWeatherData()函数的剖析：
        - 这两个函数的实现几乎一致，只有，method变量赋值不同：GETDETAIL、GETCITYWEATHER
        - param的字典：有4个键值对（city,startime,endtime,type)
        - 调用了getServerData(method,param,匿名函数,0.5)函数
    - 7.剖析getServerData函数的实现：
        - 在谷歌浏览器中抓包，做全局搜索，定位到getServerData函数的实现。但该函数被加密。该加密方式叫做JS混淆
    - 8.JS反混淆：将js混淆的密文以原文的形式展示。  https://www.jisuan.mobi/p6Hm3bB1Bbm66xiS.html
    - 9.getServerData反混淆后的代码进行剖析：
        - getParam(method,objct):该方法的参数二object==param，并且该函数的返回值是 步骤2 中动态变化且加密的请求参数 d 的 value 值
        - decodeData(data)：将加密数据进行解密。
    - 10.需要通过python调用js的相关代码：
        - PyExecJS：可以让python对js代码进行模拟。
        - 环境的安装：
            - pip install PyExecJS
            - 安装 nodeJS的环境

总结：
    - 动态变化的请求参数
    - js加密
    - js混淆
'''
######################################################