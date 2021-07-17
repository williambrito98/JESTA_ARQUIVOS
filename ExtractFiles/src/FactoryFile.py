from ExtractFiles.src.LucroPresumido.LucroPresumido import LucroPresumido
from ExtractFiles.src.LucroReal.LucroReal import LucroReal
from ExtractFiles.src.SimplesNacional.SimplesNacional import SimplesNacional


class FactoryFile:
    @staticmethod
    def setClass(nameClass, config, path):
        try:

            functions = {
                'LUCRO_REAL': LucroReal,
                'SIMPLES_NACIONAL': SimplesNacional,
                'LUCRO_PRESUMIDO': LucroPresumido
            }

            return functions[nameClass](config, path, nameClass).init()
        except KeyError as e:
            print('CLASSE NAO ENCONTRADA PARA O ARQUIVO: ' + str(e))
