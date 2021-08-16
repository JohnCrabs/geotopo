"""
This file contains a class named line
"""

import point
from scipy.spatial import distance


class Line:
    def __init__(self):
        self.p_start = point.Point()
        self.p_end = point.Point()
        self.size = 0

    def _calc_size(self):
        self.size = distance.euclidean(self.p_start.getArr(), self.p_end.getArr())

    def set(self, p_start: point.Point(), p_end: point.Point()):
        self.p_start.set(p_start.get_x(), p_start.get_y(), p_start.get_z())
        self.p_end.set(p_end.get_x(), p_end.get_y(), p_end.get_z())
        self._calc_size()

    def getSize(self):
        return self.size

    def getStartPoint(self):
        return self.p_start

    def getStartEnd(self):
        return self.p_end

