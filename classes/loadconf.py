import os
import re


class LoadConf:

    def __init__(self):
        super(LoadConf, self).__init__()

        self.configNames = ["proxy_host", "proxy_port", "proxy_user", "proxy_pass", "ssl", "ssh_port", "socket_port"]
        self.configValues = ["", "", "", "", "", "", ""]

    # Gives config names
    def getconfignames(self):
        return self.configNames

    # Gives all config items from .conf files one by one in working directory
    @staticmethod
    def openconf(file, mode):
        archive = open(file, mode)

        listlines = []
        for est in archive:
            listlines.append(est)

        archive.close()

        return listlines

    # Gives a list of all .conf files in working dir
    @staticmethod
    def listfilesindir(typefile):
        listlines = []
        for _configs in os.listdir(os.getcwd()):
            if _configs.endswith(typefile):
                listlines.append(str(_configs))

        return listlines

    # Load config from first file
    def loadconf(self):
        confExtension = ".conf"
        fileMode = "r"
        conffiles = self.listfilesindir(confExtension)
        for n in range(len(conffiles)):
            contents = self.openconf(conffiles[n], fileMode)
            for i in range(len(self.configNames)):
                for content in contents:
                    if re.findall(self.configNames[i], content):
                        self.configValues[i] = content.split()[1]

        return self.configValues
