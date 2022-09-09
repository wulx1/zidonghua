from time import sleep
from selenium.webdriver import ActionChains
from appium import webdriver

# 设备信息
from appium.webdriver.common.touch_action import TouchAction


android_INFO = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "xiaomi",
    "appPackage": "com.leiting.aobi",
    "appActivity": "com.leiting.sdk.activity.PrivacyActivity",
    "noReset": False
}

# 发送指令给appium server
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", android_INFO)
driver.implicitly_wait(10)
driver.find_element("id", "com.leiting.aobi:id/btn_positive").click()
sleep(3)
driver.find_element("id", "com.leiting.aobi:id/btn_positive").click()
driver.find_element("id", "com.android.packageinstaller:id/permission_allow_button").click()
sleep(10)
# 坐标点击,同意用户协议
driver.tap([(403,792)])
sleep(2)
# 开始游戏
driver.tap([(788,573)])
sleep(2)
# 点击使用雷霆账号登录
driver.tap([(998,643)])
# driver.find_element("id", "	com.leiting.aobi:id/agreement_btn").click()
sleep(2)
# 输入账号
driver.find_element("xpath", "//*[@text='请输入雷霆账号']").send_keys("gltcszttest1597")
sleep(2)
# 输入密码
driver.find_element("xpath", "//*[@text='请输入登录密码']").send_keys("gltcszt2022")
sleep(2)
# 勾选我同意
driver.find_element("id", "com.leiting.aobi:id/agreement_btn").click()
sleep(2)
# 点击登录
driver.find_element("id", "com.leiting.aobi:id/lt_common_submit").click()
sleep(2)
# 点击弹窗同意按钮
driver.find_element("id", "com.leiting.aobi:id/btn_positive").click()
sleep(2)
# 点击确定
driver.find_element("id", "com.leiting.aobi:id/lt_common_submit").click()
sleep(2)
# 坐标点击关闭公告弹窗
driver.tap([(1417, 89)])
sleep(1)
#点击开始游戏
driver.tap([(800, 573)])
sleep(2)
#任意点击屏幕空白处
driver.tap([(803,903)])
#点击跳过动画
driver.tap([(1507,35)])
sleep(10)

print("程序运行结束！")
driver.close()
# def taptest(driver):
#     # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
#     a1 = 188.8/1069
#     b1 = 941.5/1916
#     # 获取当前手机屏幕大小X,Y
#     X = driver.get_window_size()['width']
#     Y = driver.get_window_size()['height']
#     # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
#     driver.tap([(a1*X, b1*Y)])

