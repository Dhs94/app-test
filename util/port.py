# coding = utf-8

from util.dos_cmd import DosCmd


class Port:

    def is_port_used(self, portNumber):
        cmd = 'netstat -ano | findstr '+str(portNumber)
        result = DosCmd().excute_dos_cmd_result(cmd)
        if len(result) > 0:
            flag = True
        else:
            flag =False
        return flag

    def creat_avalible_port(self, startPort, deviceList):
        """
        生成可用端口
        :param startPort:int
        :param deviceList:list
        :return:
        """
        portList = []
        if deviceList:
            while len(portList) != len(deviceList):
                if not self.is_port_used(startPort):
                    portList.append(startPort)
                startPort += 1
        return portList


# P = Port()
# start = 4700
# device =[0,1,2,3]
# print(P.creat_avalible_port(start,device))