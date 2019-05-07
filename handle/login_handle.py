# coding = utf-8
from page.login_page import LoginPage


class LoginHandle():

    def __init__(self,  i):
        self.login_page = LoginPage(i)

    # 操作登录页面的元素
    def send_username(self, username):
        """
        输入登录账号
        """
        self.login_page.get_username_element().send_keys(username)

    def send_password(self, pwd):
        """
        输入登录密码
        """
        self.login_page.get_password_element().send_keys(pwd)

    def click_login_button(self):
        """
        点击登录按键
        """
        self.login_page.get_login_button_element().click()

    def click_forget_password(self):
        """
        点击忘记密码
        """
        self.login_page.get_forget_password_element().click()

    def click_register(self):
        """
        点击注册
        """
        self.login_page.get_register_element().click()

    def click_sns_login(self):
        """
        点击社交账号登录
        """
        self.login_page.get_sns_login_element().click()

    def get_fail_tost(self, message):
        """
        获取tost，根据获取的信息返数据
        """
        tost_elememt = self.login_page.get_tost_element(message)
        if tost_elememt:
            return True
        else:
            return False

    # def click_clear_account(self):
    #     """
    #     点击清空账号按钮
    #     """
    #     if self.login_page.get_username_element().text != '手机号/邮箱':
    #         self.login_page.clear_account().click()




