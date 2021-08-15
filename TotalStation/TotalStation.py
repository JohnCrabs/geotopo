"""
A base Total Station class library
"""
import Lib.file


class TotalStation:
    def __init__(self):
        self._str_rawFilePath = ''
        self._str_pointFilePath = ''
        self._str_rawFileData = ''
        self._str_pointFileData = ''

    def setRawFilePath(self, path):
        self._str_rawFilePath = path

    def getRawFilePath(self):
        return self._str_rawFilePath

    def setPointFilePath(self, path):
        self._str_pointFilePath = path

    def getPointFilePath(self):
        return self._str_pointFilePath

    def readRawFile(self, path):
        self.setRawFilePath(path)