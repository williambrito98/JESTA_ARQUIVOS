import os
import shutil


class Guia():
    def __init__(self, directory, config, cliente):
        self.Directory = directory
        self.__Config__ = config
        self.cliente = cliente

    def init(self):
        for file in os.listdir(self.Directory):
            shutil.copy(os.path.join(self.Directory, file),
                        os.path.join(self.__Config__['directoryEntrada'], self.cliente + "_GUIA." + file.split('.')[1]))
