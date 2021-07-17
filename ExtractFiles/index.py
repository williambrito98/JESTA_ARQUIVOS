import os
import shutil
import helpers
from src.FactoryFile import FactoryFile

#os.chdir('../')
ConfigJson = helpers.readJson(os.path.join(os.getcwd(), 'config.json'))
PathDownload = os.path.join(os.getcwd(), 'downloads')
PathArquivos = os.path.join(os.getcwd(), 'arquivos')
ConfigJson['PathDownload'] = PathDownload
ConfigJson['PathArquivos'] = PathArquivos
try:
    for file in os.listdir(PathDownload):
        file = file[0:-4]
        FactoryFile.setClass(file, ConfigJson, os.path.join(PathDownload, file))
        print('REMOVENDO ZIP')
        os.remove(os.path.join(PathDownload, file + '.zip'))
except Exception as e:
    raise str(e)
finally:
    print('FIM')
