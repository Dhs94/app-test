# coding = utf-8
from util.get_by_local import GetByLocal
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class LoginPage:

    def __init__(self, i):
        self.driver = BaseDriver().android_driver(i)
        self.get_by_local = GetByLocal(self.driver, 'login_element')

    def get_username_element(self):
        """
        获取用户名元素信息
        """
        return self.get_by_local.get_element('username')

    def get_password_element(self):
        """
        获取密码元素信息
        """
        return self.get_by_local.get_element('password')

    def get_login_button_element(self):
        """
        获取登录按钮元素信息
        """
        return self.get_by_local.get_element('login_button')

    def get_forget_password_element(self):
        """
        获取忘记密码元素信息
        """
        return self.get_by_local.get_element('forget_password')

    def get_register_element(self):
        """
        获取注册元素信息
        """
        return self.get_by_local.get_element('register')

    def get_sns_login_element(self):
        """
        获取注册元素信息
        """
        return self.get_by_local.get_element('sns_login')

    def get_tost_element(self, message):
        """
        获取tost元素信息
        """
        time.sleep(2)
        tost_locator = ("xpath", "//*[contains(@text,"+message+")]")
        result = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_locator))
        return result

    # def clear_account(self):
    #     """
    #     清楚账号
    #     """
    #     return self.get_by_local.get_element('account_delete')