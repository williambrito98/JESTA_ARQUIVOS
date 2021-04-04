import os
import shutil

import helpers

ConfigJson = helpers.readJson(os.path.join(os.getcwd(), 'config.json'))
PathDownload = os.path.join(os.getcwd(), 'downloads')
PathArquivos = os.path.join(os.getcwd(), 'arquivos')

for arq in os.listdir(os.getcwd()):
    if os.path.isfile(os.path.join(os.getcwd(), arq)) and arq[-3::] == 'csv':
        print('APAGANDO ARQUIVOS CSV ANTIGOS')
        os.remove(os.path.join(os.getcwd(), arq))

for zip in os.listdir(PathDownload):
    zipName = zip.split('.')[0]
    if zip[-3::] != 'zip':
        continue
    print('EXTRAINDO ZIP')
    helpers.ExtractZip(os.path.join(PathDownload, zip), PathDownload)
    clintes = os.path.join(PathDownload, ConfigJson['zipDirectorys'])
    helpers.appendFile(os.path.join(os.getcwd(), 'ExtractFiles', zipName + '_recebidas.csv'),
                       ConfigJson['header_recebidas'])
    helpers.appendFile(os.path.join(os.getcwd(), 'ExtractFiles', zipName + '_enviadas.csv'),
                       ConfigJson['header_enviadas'])
    FileEnviadas = os.path.join(os.getcwd(), 'ExtractFiles', zipName + '_enviadas.csv')
    FileRecebidas = os.path.join(os.getcwd(), 'ExtractFiles', zipName + '_recebidas.csv')
    print('LENDO CLIENTES')
    for cli in os.listdir(clintes):
        if not os.path.isdir(os.path.join(PathDownload, clintes, cli)):
            continue
        for file in os.listdir(os.path.join(clintes, cli, 'notas')):
            extensionFile = file.split('.')[1]
            if file in ConfigJson['nameOfFilesToJoin']:
                helpers.processFiles(os.path.join(clintes, cli, 'notas', ConfigJson['nameOfFilesToJoin'][0]),
                                     FileEnviadas)
                helpers.processFiles(os.path.join(clintes, cli, 'notas', ConfigJson['nameOfFilesToJoin'][1]),
                                     FileRecebidas)
            shutil.copy(os.path.join(clintes, cli, 'notas', file),
                        os.path.join(PathArquivos, cli) + '.' + extensionFile)

    os.remove(os.path.join(PathDownload, zip))
    shutil.rmtree(os.path.join(PathDownload, 'NOTAS'))

    shutil.copy(FileRecebidas, os.getcwd())
    shutil.copy(FileEnviadas, os.getcwd())
    os.remove(FileEnviadas)
    os.remove(FileRecebidas)
