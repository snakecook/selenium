
# 滑动模块讲解
from selenium import webdriver
from time import sleep
from lxml import etree
from selenium.webdriver import ActionChains

bro = webdriver.Chrome('chromedriver.exe')

bro.get('https://www.runob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult')
div_tag = bro.find_element_by_id('draggable')

# 拖动 = 点击 + 滑动
action = ActionChains(bro)
action.click_and_hold(div_tag)

for i in range(5):
    # perform让动作链立即执行
    action.move_by_offset(17,5).perform()
    sleep(0.5)

action.release()
sleep(3)

bro.quit()




# 12306截图爬取
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains   # 点击动作链
from PIL import Image           # 截图
from Cjy import Chaojiying_Client       # 导入超级鹰
# from selenium.webdriver.chrome.options import Options      # 无头

# 无头（存在浏览器最大化问题）
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

bro = webdriver.Chrome('chromedriver.exe')
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
bro.maximize_window()           # 最大或浏览器窗口
sleep(2)
login_button = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
login_button.click()
sleep(2)

# 用户名密码输入
bro.find_element_by_id('J-userName').send_keys('761446814@qq.com')
sleep(0.5)
bro.find_element_by_id('J-password').send_keys('Zx18788585995')
sleep(0.5)

# 截图（这里格式有要求，只能是 .png）
bro.save_screenshot('main.png')
# 找出验证码位置定位区域范围
code_img_tag = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location = code_img_tag.location
size = code_img_tag.size
rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))

# 截图裁剪并保存
i = Image.open('./main.png')
frame = i.crop(rangle)
frame.save('code.png')

# 超级鹰解析坐标
def get_text(imgPath,imgType):
    chaojiying = Chaojiying_Client('cicihaha', 'z761446814', '904920')
    im = open(imgPath, 'rb').read()
    return chaojiying.PostPic(im,imgType)['pic_str']
img_location = get_text('./code.png',9004)
# img_location 得到 x1,y1|x2,y2|x3,y3|...
# 转换成[['x1','y1'],['x2','y2'],['x3','y3']..]
all_list = []
f_list = img_location.split('|')
for index in f_list:
    a = index.split(',')
    b = [int(a[0]),int(a[1])]
    all_list.append(b)
print(all_list)

# 点击坐标
# action = ActionChains(bro)
for i in all_list:
    x,y = i
    ActionChains(bro).move_to_element_with_offset(code_img_tag,x,y).click().perform()
    sleep(0.5)

# 点击登录
bro.find_element_by_xpath('//div[@class="login-btn"]/a[@id="J-login"]').click()
