"""
A base Total Station class library
"""
import Lib.file as myFile
import Lib.point as myPoint


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
                                               'tilt_correction': '', 'created_at': ''},
                                  'data': {'point': {}, 'measure': {}}
                                  }

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

    def readPointFile_NameXYZ(self, path, delimiter=','):
        self.setPointFilePath(path)
        self.__str_pointFileData = myFile.read_TXT(path=path)
        for point in self.__str_pointFileData:
            coordinates = point.lstrip().rstrip().split(delimiter)
            # print(coordinates)
            self._dict_rawFileInfo['data']['point'][coordinates[0]] = myPoint.Point()
            self._dict_rawFileInfo['data']['point'][coordinates[0]].set(coordinates[1],
                                                                        coordinates[2],
                                                                        coordinates[3],
                                                                        coordinates[0])

        # for key in self._dict_rawFileInfo['data']['point'].keys():
        #    print(self._dict_rawFileInfo['data']['point'][key].getDict())

    def createAutocadSRCFile(self, path: str, textSize=0.5, transparency=0):
        textExport = ''
        # Example: point 499990.537,499983.388,399.872 -text @ 0.5 0 52
        for key in self._dict_rawFileInfo['data']['point'].keys():
            textExport += 'point '
            textExport += str(self._dict_rawFileInfo['data']['point'][key].get_x()) + ','
            textExport += str(self._dict_rawFileInfo['data']['point'][key].get_y()) + ','
            textExport += str(self._dict_rawFileInfo['data']['point'][key].get_z()) + ' -text @ ' + textSize.__str__()
            textExport += ' ' + transparency.__str__() + ' '
            textExport += str(self._dict_rawFileInfo['data']['point'][key].get_name()) + '\n'

        # print(textExport)
        myFile.write_TXT(path=path,  text=textExport)

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


if __name__ == "__main__":
    # Example of reading coordinates as (Name,X,Y,Z) CSV file and export them as autocad command lines.
    point_NXYZ_path = '../TestData/POINTS_NXYZ.txt'
    ts = TotalStation()
    ts.readPointFile_NameXYZ(path=point_NXYZ_path, delimiter=',')
    ts.createAutocadSRCFile(path='../TestData/AUTOCAD0_SRC.txt', textSize=0.1, transparency=0)

    point_NXYZ_path = '../TestData/POINTS1_NXYZ.txt'
    ts = TotalStation()
    ts.readPointFile_NameXYZ(path=point_NXYZ_path, delimiter=',')
    ts.createAutocadSRCFile(path='../TestData/AUTOCAD1_SRC.txt', textSize=0.1, transparency=0)

    point_NXYZ_path = '../TestData/POINTS2_NXYZ.txt'
    ts = TotalStation()
    ts.readPointFile_NameXYZ(path=point_NXYZ_path, delimiter=',')
    ts.createAutocadSRCFile(path='../TestData/AUTOCAD2_SRC.txt', textSize=0.1, transparency=0)

    point_NXYZ_path = '../TestData/POINTS3_NXYZ.txt'
    ts = TotalStation()
    ts.readPointFile_NameXYZ(path=point_NXYZ_path, delimiter=',')
    ts.createAutocadSRCFile(path='../TestData/AUTOCAD3_SRC.txt', textSize=0.1, transparency=0)

    point_NXYZ_path = '../otherData/syntetagmenesEgsa87_Dimitra.csv'
    ts = TotalStation()
    ts.readPointFile_NameXYZ(path=point_NXYZ_path, delimiter=',')
    ts.createAutocadSRCFile(path='../otherData/syntetagmenesEgsa87_Dimitra.csv', textSize=0.1, transparency=0)
