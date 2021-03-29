import os
import shutil
import helpers

ConfigJson = helpers.readJson(os.path.join(os.getcwd(), 'config.json'))
FileEnviadas = os.path.join(os.getcwd(), 'ExtractFiles', 'enviadas.csv')
FileRecebidas = os.path.join(os.getcwd(), 'ExtractFiles', 'recebidas.csv')
PathDownload = os.path.join(os.getcwd(), 'downloads')

if os.path.exists(os.path.join(os.getcwd(), 'enviadas.csv')):
    print('APAGANDO ARQUIVO DE ENVIADAS ANTIGO')
    os.remove(os.path.join(os.getcwd(), 'enviadas.csv'))

if os.path.exists(os.path.join(os.getcwd(), 'recebidas.csv')):
    print('APAGANDO ARQUIVO DE RECEBIDAS ANTIGO')
    os.remove(os.path.join(os.getcwd(), 'recebidas.csv'))

for zip in os.listdir(PathDownload):
    if zip[-3::] != 'zip':
        continue
    print('EXTRAINDO ZIP')
    helpers.ExtractZip(os.path.join(PathDownload, zip), PathDownload)
    clintes = os.path.join(PathDownload, ConfigJson['zipDirectorys'])
    print('LENDO CLIENTES')
    for cli in os.listdir(clintes):
        if not os.path.isdir(os.path.join(PathDownload, clintes, cli)):
            continue
        helpers.processFiles(os.path.join(clintes, cli, ConfigJson['nameOfFilesToJoin'][0]), FileEnviadas)
        helpers.processFiles(os.path.join(clintes, cli, ConfigJson['nameOfFilesToJoin'][1]), FileRecebidas)

    os.remove(os.path.join(PathDownload, zip))
    shutil.rmtree(os.path.join(PathDownload, 'NOTAS'))

shutil.copy(FileRecebidas, os.getcwd())
shutil.copy(FileEnviadas, os.getcwd())

helpers.clearFile(FileEnviadas)
helpers.clearFile(FileRecebidas)
