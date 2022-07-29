class SaveConf:

    def __init__(self):
        super(SaveConf, self).__init__()

        self.configNames = ["proxy_host", "proxy_port", "proxy_user", "proxy_pass", "ssl", "ssh_port", "socket_port"]

    def writeconf(self, content):
        file = "ptunnel.conf"
        mode = "w"
        archive = open(file, mode)
        j = 0
        for est in content:
            if self.configNames[j] == "ssl":
                archive.write(f"{self.configNames[j]} {est.capitalize()}\n")
            else:
                archive.write(f"{self.configNames[j]}: {est}\n")
            j += 1

        archive.close()
