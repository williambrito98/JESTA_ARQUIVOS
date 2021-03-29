import json
import zipfile


def readJson(file):
    with open(file) as f:
        config = f.read()
    return json.loads(config)


def ExtractZip(file, path):
    with zipfile.ZipFile(file=file, mode='r') as zip:
        zip.extractall(path=path)


def appendFile(file, content):
    with open(file=file, mode='a', encoding='Latin1') as file:
        file.writelines(content)


def readFile(file):
    with open(file=file, mode='r', encoding='Latin1') as file:
        file = file.readlines()
    return file


def clearFile(file):
    content = readFile(file)
    with open(file=file, mode='w') as file:
        file.write(content[0])

# def deleteFiles(file):
#     if os.

def processFiles(directoryFile, fileAppend):
    try:
        contentFileEnviadas = readFile(directoryFile)
        if len(contentFileEnviadas) != 2:
            appendFile(fileAppend, contentFileEnviadas[1:-1])
        else:
            print('sem conteudo no arquivo do cliente ' + directoryFile)
    except FileNotFoundError:
        print('Arquivo de enviadas nao encontrado')
