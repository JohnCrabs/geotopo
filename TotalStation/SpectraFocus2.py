"""
My python library for reading Spectra Focus 2 total station data
"""
import TotalStation


class SpectraFocus2(TotalStation.TotalStation):
    def __init__(self):
        super().__init__()

    def __decodeRawFile(self):
        tmp_rawData = self.getRawData()
        # Read Metadata Lines
        self._dict_rawFileInfo['metadata']['file_type'] = tmp_rawData[0].split(',')[1].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['job'] = tmp_rawData[1].split(',')[1].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['description'] = tmp_rawData[2].split(',')[1].partition('Description:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['client'] = tmp_rawData[3].split(',')[1].partition('Client:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['comments'] = tmp_rawData[4].split(',')[1].partition('Comments:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['downloaded'] = tmp_rawData[5].split(',')[1].partition('Downloaded')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['software'] = tmp_rawData[6].split(',')[1].partition('Software:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['instrument'] = tmp_rawData[7].split(',')[1].partition('Instrument:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['dist_unit'] = tmp_rawData[8].split(',')[1].partition('Dist Units:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['angle_unit'] = tmp_rawData[9].split(',')[1].partition('Angle Units:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['zero_azimuth'] = tmp_rawData[10].split(',')[1].partition('Zero azimuth:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['vertical_angle'] = tmp_rawData[11].split(',')[1].partition('VA:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['coord_system'] = tmp_rawData[12].split(',')[1].partition('Coord Order:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['horizontal_angle_raw_data'] = tmp_rawData[13].split(',')[1].partition('HA Raw data:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['projection_correction'] = tmp_rawData[14].split(',')[1].partition('Projection correction:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['c_r_correction'] = tmp_rawData[15].split(',')[1].partition('C&R correction:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['tilt_correction'] = tmp_rawData[16].split(',')[1].partition('Tilt Correction:')[2].lstrip().rstrip()
        self._dict_rawFileInfo['metadata']['created_at'] = tmp_rawData[17].split(',')[1].partition('<JOB> Created')[2].lstrip().rstrip()

        self.viewRawFileMetadata()

        print()

        # Read Data Lines
        for index in range(18, tmp_rawData.__len__()):
            dec_line = tmp_rawData[index].rstrip()
            print(dec_line)

    def openFileRaw(self, path):
        self.readRawFile(path)
        # self.viewRawData()
        self.__decodeRawFile()

    def openFilePoint(self, path):
        self.readPointFile(path)
        # self.viewPointData()


if __name__ == "__main__":
    rawFile_path = '../TestData/ADARAW.TXT'
    pointFile_path = '../TestData/ADAXYZ.TXT'

    ts = SpectraFocus2()
    ts.openFileRaw(rawFile_path)
    ts.openFilePoint(pointFile_path)
