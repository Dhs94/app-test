# coding = utf-8
import configparser


class ReadIni:

    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = 'E:/pythonAppium/scripts/boot_configuration/config/localElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_value(self, section, key):
        try:
            data = self.data.get(section, key)
            return data
        except:
            return None

# R = ReadIni()
# print(R.get_value('login_element', 'username'))