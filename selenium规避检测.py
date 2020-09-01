# # 方法一:： https://blog.csdn.net/qq_35866846/article/details/104422505(包含版本退回操作)
# # Chrome 79及以上版本无法使用该方法
# from selenium import webdriver
#
# 规避检测
# from selenium.webdriver import ChromeOptions
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
#
# driver = webdriver.Chrome(r'chromedriver.exe',options=option)
# driver.get('https://www.taobao.com/')


# 方法二：  https://zhuanlan.zhihu.com/p/117506307
# Chrome 79及以上版本使用
# 使用 Google 的Chrome Devtools-Protocol（Chrome 开发工具协议）简称CDP

from selenium.webdriver import Chrome

driver = Chrome('chromedriver.exe')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
# driver.get('http://exercise.kingname.info')
driver.get('https://www.taobao.com/')
