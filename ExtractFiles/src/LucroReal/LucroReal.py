import os
import shutil

from ExtractFiles import helpers
from ExtractFiles.src.Interfaces.Ifactory import Ifactory
from ExtractFiles.src.LucroReal.Notas.Notas import Notas
from ExtractFiles.src.LucroReal.guias.Guia import Guia
from ExtractFiles.src.LucroReal.nfts.Nfts import Ntfs
from ExtractFiles.src.Support.CreatePaths import CreatePaths


class LucroReal(Ifactory):
    def __init__(self, config, pathFile, nameFile):
        self.__Config__ = config
        self.PathFile = pathFile
        self.nameFile = nameFile
        self.__Config__['directoryFile'] = os.path.join(self.__Config__['PathArquivos'], self.nameFile)
        self.__Config__['directoryEntrada'] = os.path.join(self.__Config__['PathArquivos'], self.nameFile, 'ENTRADA')
        self.__Config__['directorySaida'] = os.path.join(self.__Config__['PathArquivos'], self.nameFile, 'SAIDA')
        self.__Config__['directoryNTFS'] = os.path.join(self.__Config__['PathArquivos'], self.nameFile, 'NFTS')
        createPaths = CreatePaths(self.__Config__)
        createPaths.createOutputpaths(self.__Config__['PathArquivos'], self.__Config__['directoryFile'],
                                      self.__Config__['directoryEntrada'],
                                      self.__Config__['directorySaida'],
                                      self.__Config__['directoryNTFS'])

    def init(self):
        helpers.ExtractZip(os.path.join(self.__Config__['PathDownload'], self.nameFile + '.zip'),
                           self.__Config__['PathDownload'])
        directoryCliente = os.path.join(self.__Config__['PathDownload'], self.__Config__['zipDirectorys'])
        for cliente in os.listdir(directoryCliente):
            if not os.path.isdir(os.path.join(self.__Config__['PathDownload'], directoryCliente, cliente)):
                continue
            for path in os.listdir(os.path.join(directoryCliente, cliente)):
                if path == 'nfts':
                    Ntfs(os.path.join(directoryCliente, cliente, path), self.__Config__, cliente).init()
                    continue
                if path == 'guias':
                    Guia(os.path.join(directoryCliente, cliente, path), self.__Config__, cliente).init()
                    continue
                if path == "notas":
                    Notas(os.path.join(directoryCliente, cliente, path), self.__Config__).init()
                    continue
        shutil.rmtree(os.path.join(self.__Config__['PathDownload'], 'NOTAS'))
