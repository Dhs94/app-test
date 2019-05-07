# coding = utf-8

import yaml



class WriteDeviceCommand:

    def read_data(self):
        """
        加载yaml文件数据
        :return:
        """
        with open("../config/device_config.yaml") as fr:
            data = yaml.load(fr)
        return data

    def get_data(self, row, key):
        """
        :param row: 'device_info_0'
        :param key: 'port'
        :return:
        """
        data = self.read_data()
        return data[row][key]

    def write_data(self, i, device, port, bp):
        """
        写入yaml文件
        """
        with open("../config/device_config.yaml", 'a') as fr:
            data = self.data_formate(i, device, port, bp)
            yaml.dump(data, fr)
        return data

    def data_formate(self, i, device, port, bp):
        """
        格式化写入yaml的数据

        """
        data = {
            'device_info_'+str(i): {
                'deviceName': device,
                'port': port,
                'bp': bp
            }
        }
        return data

    def get_yaml_lines(self):
        """
        获取devices个数
        """
        data = self.read_data()
        lines = len(data)
        return lines

# D = WriteDeviceCommand()
# D.write_data(2, 'name', '666', '777')
# print(D.get_data('device_info_2', 'deviceName'))
