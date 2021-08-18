"""
This library contains functions which solves the basic geodesic problems
"""
import numpy
import numpy as np

ANG_RAD = 'RAD'
ANG_DEG = 'DEG'
ANG_GON = 'GON'


def angleConvert(ang, conv_from=ANG_RAD, conv_to=ANG_GON):
    """
    Convert the angle from a format to another
    :param ang: angle to convert
    :param conv_from: a flag to check the current angle format (rad, degrees, gradients)
    :param conv_to: a flag to check the output angle format (rad, degrees, gradients)
    :return: an angle in the specified format (if wrong formats given then the original angle will be returned)
    """

    if conv_from == ANG_RAD:  # from RAD
        if conv_to == ANG_DEG:  # to DEG
            return (ang * (180.0 / np.pi)) % 360.0  # 1 rad = 180.0 / pi deg
        elif conv_to == ANG_GON:  # to GON
            return (ang * (200.0 / np.pi)) % 400.0  # 1 rad = 200.0 / pi gon
        else:  # Wrong Format
            return ang
    elif conv_from == ANG_DEG:  # from DEG
        if conv_to == ANG_RAD:  # to RAD
            return (ang * (np.pi / 180.0)) % 2*np.pi  # 1 deg = pi / 180.0 rad
        elif conv_to == ANG_GON:  # to GON
            return (ang * (200.0 / 180.0)) % 400.0  # 1 deg = 200.0 / 180.0 gon
        else:  # Wrong Format
            return ang
    elif conv_from == ANG_GON:  # from GON
        if conv_to == ANG_RAD:  # to RAD
            return (ang * (np.pi / 200.0)) % 2*np.pi  # 1 gon = 180.0 / 200.0 deg
        elif conv_to == ANG_DEG:  # to DEG
            return (ang * (180.0 / 200.0)) % 180.0  # 1 rad = pi / 200.0 deg
        else:  # Wrong Format
            return ang
    else:  # Wrong Format
        return ang


def calcAzimuthAngle(xb, yb, xt, yt):
    """
    This function calculates the Azimuth Angle G_12 between two points (base and target)
    :param xb: the x coordinate of base point
    :param yb: the y coordinate of base point
    :param xt: the x coordinate of target point
    :param yt: the y coordinate of target point
    :return: the azimuth angle in RAD, DEG, GON
    """

    dx = xt - xb  # calculate the x difference
    dy = yt - yb  # calculate the y difference

    if dx > 0:  # if dx > 0 situation
        if dy > 0:  # if dy > 0 situation
            ang = np.arctan(dx/dy)  # rad
            return ang, angleConvert(ang, conv_from=ANG_RAD, conv_to=ANG_DEG), angleConvert(ang, conv_from=ANG_RAD,
                                                                                            conv_to=ANG_GON)
        elif dy < 0:  # if dy < 0 situation
            ang = np.pi - np.arctan(dx/dy)  # rad
            return ang, angleConvert(ang, conv_from=ANG_RAD, conv_to=ANG_DEG), angleConvert(ang, conv_from=ANG_RAD,
                                                                                            conv_to=ANG_GON)
        else:  # if dy = 0 situation
            ang = 100.0000  # gon
            return angleConvert(ang, conv_from=ANG_GON, conv_to=ANG_RAD), angleConvert(ang, conv_from=ANG_GON,
                                                                                       conv_to=ANG_DEG), ang

    elif dx < 0:  # if dx < 0 situation
        if dy > 0:  # if dy > 0 situation
            ang = 2*np.pi - np.arctan(dx/dy)  # rad
            return ang, angleConvert(ang, conv_from=ANG_RAD, conv_to=ANG_DEG), angleConvert(ang, conv_from=ANG_RAD,
                                                                                            conv_to=ANG_GON)

        elif dy < 0:  # if dy < 0 situation
            ang = np.pi + np.arctan(dx / dy)  # rad
            return ang, angleConvert(ang, conv_from=ANG_RAD, conv_to=ANG_DEG), angleConvert(ang, conv_from=ANG_RAD,
                                                                                            conv_to=ANG_GON)

        else:  # if dy = 0 situation
            ang = 300.0000  # gon
            return angleConvert(ang, conv_from=ANG_GON, conv_to=ANG_RAD), angleConvert(ang, conv_from=ANG_GON,
                                                                                       conv_to=ANG_DEG), ang

    else:  # if dx = 0 situation
        if dy > 0:  # if dy > 0 situation
            ang = 0.0000  # gon
            return angleConvert(ang, conv_from=ANG_GON, conv_to=ANG_RAD), angleConvert(ang, conv_from=ANG_GON,
                                                                                       conv_to=ANG_DEG), ang
        elif dy < 0:  # if dy < 0 situation
            ang = 200.0000  # gon
            return angleConvert(ang, conv_from=ANG_GON, conv_to=ANG_RAD), angleConvert(ang, conv_from=ANG_GON,
                                                                                       conv_to=ANG_DEG), ang
        else:  # if dy = 0 situation
            # dx = 0 and dy = 0 it's the same point, infinite lines can be created
            return numpy.inf, numpy.inf, numpy.inf


if __name__ == "__main__":
    print("#################")
    print("# ANGLE CONVERT #")
    print("#################")
    ang_deg = 63.4
    ang_rad = 1.1065387458
    ang_gon = 70.4444

    print()
    print("DEG example")
    print("ang_from_DEG = %.2f" % ang_deg)
    print("ang_to_RAD = %.10f" % angleConvert(ang_deg, conv_from=ANG_DEG, conv_to=ANG_RAD))
    print("ang_to_GON = %.4f" % angleConvert(ang_deg, conv_from=ANG_DEG, conv_to=ANG_GON))

    print()
    print("RAD example")
    print("ang_from_RAD = %.10f" % ang_rad)
    print("ang_to_DEG = %.2f" % angleConvert(ang_rad, conv_from=ANG_RAD, conv_to=ANG_DEG))
    print("ang_to_GON = %.4f" % angleConvert(ang_rad, conv_from=ANG_RAD, conv_to=ANG_GON))

    print()
    print("GON example")
    print("ang_from_GON = %.4f" % ang_gon)
    print("ang_to_RAD = %.10f" % angleConvert(ang_gon, conv_from=ANG_GON, conv_to=ANG_RAD))
    print("ang_to_DEG = %.2f" % angleConvert(ang_gon, conv_from=ANG_GON, conv_to=ANG_DEG))

    print()
    print()
    print("#######################")
    print("# AZIMUTH CALCULATION #")
    print("#######################")

    x1 = 486235.992
    y1 = 4211781.955
    x2 = 486230.853
    y2 = 4211780.757
    x3 = 486232.551
    y3 = 4211790.555
    x4 = x1
    y4 = y2

    print("p1(%.3f, %.3f)" % (x1, y1))
    print("p2(%.3f, %.3f)" % (x2, y2))
    print("p3(%.3f, %.3f)" % (x3, y3))
    print("p4(%.3f, %.3f)" % (x4, y4))
    print()
    print("dp12(%.3f, %.3f)" % (x2 - x1, y2 - y1))
    print("dp13(%.3f, %.3f)" % (x3 - x1, y3 - y1))
    print("dp14(%.3f, %.3f)" % (x4 - x1, y4 - y1))
    print('-----')
    print("dp23(%.3f, %.3f)" % (x3 - x2, y3 - y2))
    print("dp24(%.3f, %.3f)" % (x4 - x2, y4 - y2))
    print('-----')
    print("dp34(%.3f, %.3f)" % (x4 - x3, y4 - y3))
    print()
    print("AZ = (.10f rad, .3f deg, .4f gon)")
    print("AZ_12 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x1, y1, x2, y2))
    print("AZ_21 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x2, y2, x1, y1))
    print("AZ_13 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x1, y1, x3, y3))
    print("AZ_31 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x3, y3, x1, y1))
    print("AZ_14 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x1, y1, x4, y4))
    print("AZ_41 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x4, y4, x1, y1))
    print('-----')
    print("AZ_23 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x2, y2, x3, y3))
    print("AZ_32 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x3, y3, x2, y2))
    print("AZ_24 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x2, y2, x4, y4))
    print("AZ_42 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x4, y4, x2, y2))
    print('-----')
    print("AZ_34 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x3, y3, x4, y4))
    print("AZ_43 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x4, y4, x3, y3))
    print('-----')
    print("AZ_44 = (%.10f, %.3f, %.4f)" % calcAzimuthAngle(x4, y4, x4, y4))
