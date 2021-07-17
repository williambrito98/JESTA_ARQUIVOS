from src.LucroPresumido.LucroPresumido import LucroPresumido
from src.LucroReal.LucroReal import LucroReal
from src.SimplesNacional.SimplesNacional import SimplesNacional


class FactoryFile:
    @staticmethod
    def setClass(nameClass, config, path):
        try:

            functions = {
                'LUCRO_REAL': LucroReal,
                'SIMPLES_NACIONAL': SimplesNacional,
                'LUCRO_PRESUMIDO': LucroPresumido
            }
            print('ARQUIVO DO ' + nameClass)
            return functions[nameClass](config, path, nameClass).init()
        except KeyError as e:
            print('CLASSE NAO ENCONTRADA PARA O ARQUIVO: ' + str(e))
