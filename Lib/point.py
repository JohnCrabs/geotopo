"""
This file contains a class named point
"""


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.name = '0'

    def set(self, x, y, z, name='0'):
        self.x = x
        self.y = y
        self.z = z
        self.name = name

    def get(self):
        return {self.name: {'x': self.x, 'y': self.y, 'z': self.z}}

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_name(self):
        return self.name
