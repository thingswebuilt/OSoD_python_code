"""tools for processing data from VL53L5CX sensors"""

import functools
import operator
from typing import TypeAlias
import numpy as np
import math
from skspatial.objects import Plane, Vector

from . import TofReadingSet


def average_distance(sensor_reading: TofReadingSet) -> float:
    """returns the average value of all readings"""
    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    flattened_readings: list[int] = functools.reduce(
        operator.iconcat, sensor_reading, []
    )
    average_reading = sum(flattened_readings) / len(flattened_readings)
    return average_reading


XYZPoint: TypeAlias = tuple[float, float, float]


def create_point_cloud(
    sensor_reading: list[list[int]],
) -> list[XYZPoint]:
    """converts a 2D array of range measurements into a
    3d point cloud using standard VL53L5CX FOV,
    assuming the sensor is pointing vertically upwards"""
    point_cloud: list[XYZPoint] = []
    if len(sensor_reading) == 4:
        # sensor in 4x4 zone mapping
        # FOV is 45degree both vertically and horizontally
        angle_between_zones = math.radians(45) / 4
        # 2 zones per side. so centre of first zone is 3 half angles from centre
        angle_to_first_zone = angle_between_zones / 2 * 3
    elif len(sensor_reading) == 8:
        # sensor in 8x8 zone mapping
        # FOV is 45degree both vertically and horizontally
        angle_between_zones = 45 / 8
        # 4 zones per side. so centre of first zone is 7 half angles from centre
        angle_to_first_zone = angle_between_zones / 2 * 7
    else:
        raise TypeError("non-standard zone mapping provided")

    vertical_angle_array: list[float] = np.arange(  # type: ignore
        angle_to_first_zone * -1,
        angle_to_first_zone + angle_between_zones,
        angle_between_zones,
        dtype=float,
    ).tolist()
    horizontal_angle_array: list[float] = np.arange(  # type: ignore
        angle_to_first_zone * -1,
        angle_to_first_zone + angle_between_zones,
        angle_between_zones,
    ).tolist()
    for v_index, vertical_angle in enumerate(vertical_angle_array):

        for h_index, horizontal_angle in enumerate(horizontal_angle_array):
            distance_value = sensor_reading[v_index][h_index]
            x_pos = distance_value * math.sin(horizontal_angle)
            y_pos = distance_value * math.sin(vertical_angle)
            z_pos = (
                distance_value * math.cos(horizontal_angle) * math.cos(vertical_angle)
            )
            point_cloud.append((x_pos, y_pos, z_pos))
    return point_cloud


def plane_fit(sensor_reading: list[list[int]]) -> Vector:
    """use a linear model to get a best fit plane of the sensor reading
    returns normal vector"""
    points = create_point_cloud(sensor_reading)
    plane: Plane = Plane.best_fit(points)  # type: ignore
    normal: Vector = plane.normal  # type: ignore
    return normal
