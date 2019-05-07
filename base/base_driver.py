# coding= utf-8
from appium import webdriver
from util.write_device_command import WriteDeviceCommand
import time


class BaseDriver:

    def android_driver(self, i):
        write_device_cmd = WriteDeviceCommand()
        device_name = write_device_cmd.get_data('device_info_'+str(i), 'deviceName')
        device_port = write_device_cmd.get_data('device_info_'+str(i), 'port')
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",  # 测试平台，默认为appium，为了get_tost此处为automator2
            "deviceName": device_name,
            "app": "E:\\pythonAppium\\autoTest\\apps\\mukewang.apk",
            "appWaitActivity": "cn.com.open.mooc.user.login.MCLoginActivity",
            "noReset": "True",  # 是否重装
            # "chromeOptions": {"androidProcess": "WEBVIEW_cn.com.open.mooc"}
        }
        driver = webdriver.Remote("http://127.0.0.1:"+str(device_port)+"/wd/hub", capabilities)
        time.sleep(5)
        return driver