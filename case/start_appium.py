# coding=utf-8

from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.get_by_local import GetByLocal



class Base:

    def __init__(self):
        self.driver = self.get_driver()
        self.size = self.get_size()
        self.get_by_local = GetByLocal(self.driver, 'login_element')

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",  # 测试平台，默认为appium，为了get_tost此处为automator2
            "deviceName": "127.0.0.1:21513",
            "app": "E:\\pythonAppium\\autoTest\\apps\\mukewang.apk",
            "appWaitActivity": "cn.com.open.mooc.user.login.MCLoginActivity",
            "noReset": "True",  # 是否重装
            # "chromeOptions": {"androidProcess": "WEBVIEW_cn.com.open.mooc"}

        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        return driver

    def get_size(self):
        # 获取屏幕大小
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    def swipe_right(self):
        """
        从左向右滑
        :return:
        """
        x = self.get_size()[0]/10
        x1 = self.get_size()[0]/10*9
        y = self.get_size()[1]/2
        self.driver.swipe(x, y, x1, y)

    def swipe_left(self):
        """
        从右向左滑
        :return:
        """
        x = self.get_size()[0]/10*9
        x1 = self.get_size()[0]/10
        y = self.get_size()[1]/2
        self.driver.swipe(x, y, x1, y)

    def swipe_up(self):
        """
        从下往上滑
        :return:
        """
        x = self.get_size()[0]/2
        y = self.get_size()[1]/10*9
        y1 = self.get_size()[1]/10
        self.driver.swipe(x, y, x, y1)

    def swipe_down(self):
        """
        从上往下滑
        :return:
        """
        x = self.get_size()[0]/2
        y = self.get_size()[1]/10
        y1 = self.get_size()[1]/10*9
        self.driver.swipe(x, y, x, y1)

    def swipe_on(self, direction):
        if direction == 'left':
            self.swipe_left()
        elif direction == 'right':
            self.swipe_right()
        elif direction == 'up':
            self.swipe_up()
        else:
            self.swipe_down()

    def go_to_login(self):
        """
        跳转到登录界面
        :return:
        """
        self.driver.find_element_by_id('cn.com.open.mooc:id/tv_go_login').click()

    def login_by_id(self):
        self.get_by_local.get_element('username').send_keys('13055211990')
        self.get_by_local.get_element('password').send_keys('dianzi1312')
        self.get_by_local.get_element('login_button').click()

    def login_by_uiautomator(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("13055211990")').clear()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').sendkeys('13055211990')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/password_edit")').sendkeys('dianzi1312')

    def login_by_xpath(self):
        # 在所有层级查找text包含忘记的元素
        # self.drvier.find_element_by_xpath('//*[cotains(@text,"忘记")]').click()
        # 在class为..中查找text为忘记的元素
        # self.drvier.find_element_by_xpath('//android.widget.TextView[@text="忘记"]').click()
        # /../preceding-sibiling::寻找上级节点
        self.driver.find_element_by_xpath('//android.widget.TextView@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibiling::*[@index="1]')

    def get_webview(self):
        time.sleep(20)
        webviews = self.driver.contexts
        print(webviews)
        for view in webviews:
            if 'WEBVIEW_cn.com.open.mooc' in view:
                print("1")
                self.driver.switch_to.context(view)
                print("2")
                break
        self.driver.find_element_by_link_text('JAVA').click()

    def get_tost(self):
        time.sleep(2)
        tost_locator = ("xpath", "//*[contains(@text,'请输入密码')]")
        result = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_locator))
        print(result)


# if __name__ == '__main__':
#     run = Base()
#     time.sleep(5)
#     # run.login_by_uiautomator()
#     # run.go_to_login()
#     time.sleep(2)
#     run.login_by_id()
