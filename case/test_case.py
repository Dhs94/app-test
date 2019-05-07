# coding = utf-8
import unittest
import os
import time
import HTMLTestRunner
import threading
from business.login_business import LogingBusiness
from util.server import Server
from util.write_device_command import WriteDeviceCommand
import multiprocessing


class Parames(unittest.TestCase):

    def __init__(self, methodName='runTest', parame=None):
        super(Parames, self).__init__(methodName)
        global parames
        parames = parame


class CaseTest(Parames):

    @classmethod
    def setUpClass(cls):
        print("start---------------------->", parames)
        cls.login_businiess = LogingBusiness(parames)

    def test_01(self):
        result = self.login_businiess.login_account_error()
        self.assertTrue(result)

    def test_02(self):
        self.login_businiess.login_success()
        print("loginsuccess")

    @classmethod
    def tearDownClass(cls):
        print('end---------------------------->')


def appiium_init():
    server = Server()
    server.start_server()


def get_suit(i):
    # case_path = os.getcwd()
    # report_path = os.path.join(os.path.abspath('../'), 'report/test_report')
    report_path = "E:/pythonAppium/scripts/boot_configuration/report/report"+str(i)+".html"
    # suit = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
    suit = unittest.TestSuite()
    suit.addTest(CaseTest("test_01", parame=i))
    suit.addTest(CaseTest("test_02", parame=i))
    with open(report_path, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(fp, title=u'Timecube测试报告', description=u'用例执行情况')
        runner.run(suit)
    # unittest.TextTestRunner().run(suit)


def get_devices_count():
    write_command = WriteDeviceCommand()
    data = write_command.get_yaml_lines()
    return data

if __name__ == '__main__':
    appiium_init()
    processes = []
    for i in range(get_devices_count()):
        process = multiprocessing.Process(target=get_suit, args=(i,))
        processes.append(process)
    for j in processes:
        j.start()
        time.sleep(2)


