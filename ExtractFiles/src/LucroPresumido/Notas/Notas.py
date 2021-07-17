import os

from src.DataFrame.Create import Create
from src.DataFrame.Save import Save
from src.LucroPresumido.Notas.Enviadas import Enviadas
from src.LucroPresumido.Notas.Recebidas import Recebidas


class Notas:
    def __init__(self, directory, config):
        self.Directory = directory
        self.__Config__ = config

    def init(self):
        for file in os.listdir(self.Directory):
            if file == 'enviadas.csv':
                pathDfInput = os.path.join(self.Directory,
                                           'enviadas.csv')
                pathDfOutput = os.path.join(self.__Config__['directorySaida'],
                                            'enviadas.csv')
                df = Create.create(pathDfInput)
                df = Recebidas(df, self.__Config__).init()
                Save.save(df, pathDfOutput)
                continue
            if file == "recebidas.csv":
                pathDfInput = os.path.join(self.Directory, 'recebidas.csv')
                pathDfOutput = os.path.join(self.__Config__['directorySaida'],
                                            'recebidas.csv')
                df = Create.create(pathDfInput)
                df = Enviadas(df, self.__Config__).init()
                Save.save(df, pathDfOutput)
                continue
        return True
