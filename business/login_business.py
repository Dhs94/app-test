# coding utf-8
from handle.login_handle import LoginHandle


class LogingBusiness:

    def __init__(self, i):
        self.login_handle = LoginHandle(i)

    def login_success(self):
        # self.login_handle.click_clear_account()
        self.login_handle.send_username('13055211990')
        self.login_handle.send_password('dianzi1312')
        self.login_handle.click_login_button()

    def login_account_error(self):
        self.login_handle.send_username('13055211991')
        self.login_handle.send_password('dianzi1312')
        self.login_handle.click_login_button()
        flag = self.login_handle.get_fail_tost('账号未注册')
        if flag:
            return True
        else:
            return False

    def login_password_error(self):
        self.login_handle.send_username('13055211990')
        self.login_handle.send_password('dianzi1312')
        self.login_handle.click_login_button()
        flag = self.login_handle.get_fail_tost('登录密码错误')
        if flag:
            return True
        else:
            return False
