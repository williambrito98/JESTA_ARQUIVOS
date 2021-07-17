import json
import zipfile
from datetime import date
import lxml.html

def readJson(file):
    with open(file) as f:
        config = f.read()
    return json.loads(config)


def ExtractZip(file, path):
    with zipfile.ZipFile(file=file, mode='r') as zip:
        zip.extractall(path=path)


def appendFile(file, content):
    with open(file=file, mode='a', encoding='ANSI') as file:
        file.writelines(content)


def readFile(file):
    with open(file=file, mode='r', encoding='ANSI') as file:
        file = file.readlines()
    return file


def clearFile(file):
    content = readFile(file)
    with open(file=file, mode='w') as file:
        file.write(content[0])


def processFiles(directoryFile, fileAppend, configJson):
    newContent = []
    try:
        contentFile = readFile(directoryFile)
        if len(contentFile) != 2:
            if 'SIMPLES_NACIONAL' in fileAppend:
                for linha in contentFile[1:-1]:
                    if linha == '\n':
                        continue
                    if 'html' in linha:
                        break
                    if len(linha.split(';')[23].strip(' ')) > 1:
                        continue
                    if configJson['CODIGO_SERVICO'].get(linha.split(';')[28], None):
                        newContent.append(linha.replace('\n', '') + ';' + configJson['CODIGO_SERVICO'].get(
                            linha.split(';')[28].strip(' ')) + str(date.today().month - 1) +
                                          str(date.today().year) + '\n')
                appendFile(fileAppend, newContent)
            else:
                appendFile(fileAppend, contentFile)
        else:
            print('sem conteudo no arquivo do cliente ' + directoryFile)
    except FileNotFoundError:
        print('Arquivo nao encontrado')
