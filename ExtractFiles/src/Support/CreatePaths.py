import os


class CreatePaths:
    def __init__(self, config):
        self.__Config__ = config

    def createOutputpaths(self, *args):
        args = list(args)
        if len(args) == 0:
            return True
        path = args.pop(0)
        if not os.path.exists(path):
            print('CRIANDO PASTA ' + path)
            os.mkdir(path)
        return self.createOutputpaths(*args)
