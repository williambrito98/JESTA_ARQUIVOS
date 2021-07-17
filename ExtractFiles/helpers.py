import json
import zipfile


def readJson(file):
    with open(file) as f:
        config = f.read()
    return json.loads(config)


def ExtractZip(file, path):
    print('EXTRAINDO ZIP DO' + file)
    with zipfile.ZipFile(file=file, mode='r') as zip:
        zip.extractall(path=path)
