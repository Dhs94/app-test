# coding = utf-8
from util.read_init import ReadIni

class GetByLocal:
    def __init__(self, driver, section):
        self.driver = driver
        self.section = section

    def get_element(self, key):
        read_ini = ReadIni()
        local = read_ini.get_value(self.section, key)
        by = local.split('>')[0]
        local_by = local.split('>')[1]
        try:
            if by == 'id':
                element = self.driver.find_element_by_id(local_by)
            elif by == 'calssName':
                element = self.driver.find_element_by_calss_name(local_by)
            elif by == 'linkText':
                element = self.driver.find_element_by_link_text(local_by)
            else:
                element = self.driver.find_element_by_xpath(local_by)
            return element
        except:
            return None


