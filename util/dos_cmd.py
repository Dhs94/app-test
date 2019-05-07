# coding = uts-8
import os


class DosCmd:

    def excute_dos_cmd_result(self, cmd):
        result_list = []
        results = os.popen(cmd).readlines()
        for i in results:
            if i == '\n':
                continue
            else:
                result_list.append(i.strip('\n'))
        return result_list

    def excute_dos_cmd(self, cmd):
        os.system(cmd)

# D = DosCmd()
# print(D.excute_dos_cmd_result('appium -p 4700 -bp 4900 -U 127.0.0.1:21503'))
