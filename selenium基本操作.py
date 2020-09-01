'''

- 下载安装selenium: pip install selenium
- 下载浏览器驱动程序
    - http://chromedriver.storage.googleapis.com/index.html
- 查看驱动和浏览器版本的映射关系：
    - http://blog.csdn.net/huilan_same/article/details/51896672
- 实例化某一浏览器对象

- 动作链：
    - 一系列连续的动作
    - 在实现标签定位时，如果发现定位的标签是存在于iframe标签之中的
    ，则在定位时必须执行一个固定的操作：bro.switch_to.frame('iframe的id')
- 无头浏览器的操作：无可视化界面的浏览器
    - PhantomJs：停止更新
    - 谷歌无头浏览器
- 让selenium规避检测

'''
from time import sleep
from selenium import webdriver
bro = webdriver.Chrome(executable_path=r'F:\cc\chaojiying\chaojiying_Python\chromedriver.exe')

# 目标网页
bro.get('https://www.jd.com/')

# 进行标签定位
search_input = bro.find_element_by_xpath('//*[@id="key"]')
search_input.send_keys('我叼你妈的！')

btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click()
sleep(2)

# 执行js
# bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')   # 滚动到底
bro.execute_script('window.scrollTo(0,400)')
sleep(0.5)
bro.execute_script('window.scrollTo(0,800)')
sleep(0.5)
bro.execute_script('window.scrollTo(0,1200)')
sleep(2)

# 获取页面代码
page_text = bro.page_source
print(page_text)

sleep(1)
bro.quit()