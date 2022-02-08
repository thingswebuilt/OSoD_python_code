"""tools for processing data from VL53L5CX sensors"""

import functools
import operator
import numpy as np
from numpy.linalg import svd
import math

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
    """
    p, n = planeFit(points)

    Given an array, points, of shape (d,...)
    representing points in d-dimensional space,
    fit an d-dimensional plane to the points.
    Return a point, p, on the plane (the point-cloud centroid),
    and the normal, n.
    """
    point_cloud = create_point_cloud(sensor_reading)
    # Collapse trialing dimensions
    points = np.reshape(point_cloud, (np.shape(point_cloud)[0], -1))

    assert points.shape[0] <= points.shape[1], "There are only {} points in {} dimensions.".format(points.shape[1], points.shape[0])
    ctr = points.mean(axis=1)
    x = points - ctr[:,np.newaxis]
    M = np.dot(x, x.T) # Could also use np.cov(x) here.
    return ctr, svd(M)[0][:,-1]