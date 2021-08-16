"""
A base Total Station class library
"""
import Lib.file as myFile


class TotalStation:
    def __init__(self):
        self.__str_rawFilePath = ''
        self.__str_pointFilePath = ''
        self.__str_rawFileData = ''
        self.__str_pointFileData = ''
        self._dict_rawFileInfo = {'metadata': {'file_type': '', 'job': '', 'description': '',
                                               'client': '', 'comments': '', 'downloaded': '',
                                               'software': '', 'instrument': '', 'dist_unit': '',
                                               'angle_unit': '', 'zero_azimuth': '', 'vertical_angle': '',
                                               'coord_system': '', 'horizontal_angle_raw_data': '',
                                               'projection_correction': '', 'c_r_correction': '',
                                               'tilt_correction': '', 'created_at': ''}}

    def setRawFilePath(self, path):
        self.__str_rawFilePath = path

    def getRawFilePath(self):
        return self.__str_rawFilePath

    def setPointFilePath(self, path):
        self.__str_pointFilePath = path

    def getPointFilePath(self):
        return self.__str_pointFilePath

    def readRawFile(self, path):
        self.setRawFilePath(path)
        self.__str_rawFileData = myFile.read_TXT(path=path)

    def readPointFile(self, path):
        self.setPointFilePath(path)
        self.__str_pointFileData = myFile.read_TXT(path=path)

    def viewRawData(self):
        print('\n\n\n*** RAW DATA FILE ***')
        print(self.__str_rawFileData)

    def viewPointData(self):
        print('\n\n\n*** POINT DATA FILE ***')
        print(self.__str_pointFileData)

    def getRawData(self):
        return self.__str_rawFileData

    def getPointData(self):
        return self.__str_pointFileData

    def viewRawFileMetadata(self):
        for key in self._dict_rawFileInfo['metadata'].keys():
            print(key + ':', self._dict_rawFileInfo['metadata'][key])