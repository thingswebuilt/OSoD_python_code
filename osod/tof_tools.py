"""tools for processing data from VL53L5CX sensors"""

import functools
import operator

def average_distance(sensor_reading: list[list[int]]) -> float:
    """returns the average value of all readings"""
    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    flattened_readings: list[int] = functools.reduce(operator.iconcat, sensor_reading, [])
    average_reading = sum(flattened_readings)/len(flattened_readings)
    return average_reading
