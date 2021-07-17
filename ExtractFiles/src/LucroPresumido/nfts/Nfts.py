import os

from src.DataFrame.Create import Create
from src.DataFrame.Save import Save
from src.LucroPresumido.nfts.Intermediadas import Intermediadas
from src.LucroPresumido.nfts.Tomados import Tomados


class Ntfs:
    def __init__(self, directory, config, cliente):
        self.Directory = directory
        self.cliente = cliente
        self.__Config__ = config

    def init(self):
        for file in os.listdir(self.Directory):
            if file == 'nfsintermediadas.csv':
                pathDfInput = os.path.join(self.Directory,
                                           'nfsintermediadas.csv')
                pathDfOutput = os.path.join(self.__Config__['directoryNTFS'],
                                            'nfsintermediadas.csv')
                df = Create.create(pathDfInput)
                df = Intermediadas(df, self.__Config__).init()
                Save.save(df, pathDfOutput)
                continue
            if file == 'nfstomados.csv':
                pathDfInput = os.path.join(self.Directory,
                                           'nfstomados.csv')
                pathDfOutput = os.path.join(self.__Config__['directoryNTFS'],
                                            'nfstomados.csv')
                df = Create.create(pathDfInput)
                df = Tomados(df, self.__Config__).init()
                Save.save(df, pathDfOutput)
                continue
