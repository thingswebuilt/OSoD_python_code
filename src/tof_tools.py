"""tools for processing data from VL53L5CX sensors"""

import functools
import operator
import numpy as np
from numpy.linalg import svd
import math
from sklearn import linear_model

def average_distance(sensor_reading: list[list[int]]) -> float:
    """returns the average value of all readings"""
    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    flattened_readings: list[int] = functools.reduce(operator.iconcat, sensor_reading, [])
    average_reading = sum(flattened_readings)/len(flattened_readings)
    return average_reading

def create_point_cloud(sensor_reading: list[list[int]]) -> list[tuple[float, float, float]]:
    """converts a 2D array of range measurements into a
     3d point cloud using standard VL53L5CX FOV,
     assuming the sensor is pointing vertically upwards"""
    point_cloud=[[] for i in range(3)]
    if len(sensor_reading) == 4:
        #sensor in 4x4 zone mapping
        #FOV is 45degree both vertically and horizontally
        angle_between_zones = math.radians(45) / 4
        #2 zones per side. so centre of first zone is 3 half angles from centre
        angle_to_first_zone = angle_between_zones /2  * 3
    elif len(sensor_reading) == 8:
        #sensor in 8x8 zone mapping
        #FOV is 45degree both vertically and horizontally
        angle_between_zones = 45 / 8
        #4 zones per side. so centre of first zone is 7 half angles from centre
        angle_to_first_zone = angle_between_zones /2 * 7
    else:
        raise TypeError("non-standard zone mapping provided")
    for v_index, vertical_angle in enumerate(np.arange(-angle_to_first_zone,
                                                   angle_to_first_zone+angle_between_zones,
                                                   angle_between_zones)):
        for h_index, horizontal_angle in enumerate(np.arange(-angle_to_first_zone,
                                                         angle_to_first_zone+angle_between_zones,
                                                         angle_between_zones)):
            distance_value = sensor_reading[v_index][h_index]
            x = distance_value * math.sin(horizontal_angle)
            y = distance_value * math.sin(vertical_angle)
            z = distance_value * math.cos(horizontal_angle) * math.cos(vertical_angle)
            point_cloud[0].append(x)
            point_cloud[1].append(y)
            point_cloud[2].append(z)
    return point_cloud


def plane_fit(sensor_reading: list[list[int]]) -> tuple[list[float],list[float]]:
    """ use a lienar model to get a best fit plane of the sensor reading"""
    # your data is stored as X, Y, Z
    X, Y, Z = np.array(create_point_cloud(sensor_reading))

    print(X.shape, Y.shape, Z.shape)

    x1, y1, z1 = X.flatten(), Y.flatten(), Z.flatten()

    X_data = np.array([x1, y1]).reshape((-1, 2))
    Y_data = z1

    reg = linear_model.LinearRegression().fit(X_data, Y_data)

    print("coefficients of equation of plane, (a1, a2): ", reg.coef_)

    print("value of intercept, c:", reg.intercept_)