# coding = utf-8
from util.dos_cmd import DosCmd
from util.port import Port
import threading
from util.write_device_command import WriteDeviceCommand
import time
from handle.login_handle import LoginHandle
from page.login_page import LoginPage
from business.login_business import LogingBusiness

class Server:

    def __init__(self):
        self.dos = DosCmd()
        self.port = Port()
        self.write_data = WriteDeviceCommand()
        self.device_list = self.get_device()

    def get_device(self):
        """
        获取设备地址
        """
        device_result = self.dos.excute_dos_cmd_result('adb devices')
        device_list = []
        if len(device_result) >= 2:
            for i in device_result:
                if 'List' in i:
                    continue
                else:
                    device_info = i.split('\t')
                    if device_info[1] == 'device':
                        device_list.append(device_info[0])
            return device_list
        else:
            return None

    def creat_command_list(self, i):
        # appium -p 4700 -bp 4710 -u 127.0.0.1:21503
        device_list = self.get_device()
        port_list = self.port.creat_avalible_port(4800, device_list)
        bootstrap_list = self.port.creat_avalible_port(4900, device_list)
        cmd = 'appium -p ' + str(port_list[i]) + ' -bp ' + str(bootstrap_list[i]) + ' -U ' + device_list[i]
        self.write_data.write_data(i, device_list[i], port_list[i], bootstrap_list[i])
        return cmd

    def excute_command(self, i):
        cmd = self.creat_command_list(i)
        print(cmd)
        result = self.dos.excute_dos_cmd(cmd)
        return result

    def kill_server(self):
        process_list = self.dos.excute_dos_cmd_result('tasklist | find "node.exe"')
        if len(process_list) > 0:
            self.dos.excute_dos_cmd_result('taskkill -F -PID node.exe')

    def clear_data(self):
        with open("../config/device_config.yaml", 'w') as fr:
            fr.truncate()
            fr.close()

    def start_server(self):
        self.kill_server()
        self.clear_data()
        for i in range(len(self.device_list)):
            thread = threading.Thread(target=self.excute_command, args=(i,))
            thread.start()
        time.sleep(20)


# S = Server()
# print(S.start_server())
# L = LogingBusiness(0)
# L = L.login_success()


