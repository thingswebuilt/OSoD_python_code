"""Fixtures for vl53lcx tof tests"""
from typing import Iterable, cast
import pytest

from osod.tof.enums import Vl53l5cxStatus
from osod.tof.models import (
    Vl53l5cxFrame8x8Data,
    Vl53l5cxZoneReading,
)


@pytest.fixture
def perfect_flat_reading_data() -> Vl53l5cxFrame8x8Data:
    """pytest fixture to return data for flat tof reading"""
    raw_sensor_data = (1000,) * 64

    return cast(
        Vl53l5cxFrame8x8Data,
        tuple(
            Vl53l5cxZoneReading(
                value=value, status=Vl53l5cxStatus.RANGE_VALID, zone=index
            )
            for index, value in enumerate(cast(Iterable[int], raw_sensor_data), start=1)
        ),
    )


@pytest.fixture
def oblique_reading_data() -> Vl53l5cxFrame8x8Data:
    """pytest fixture to return data for oblique tof reading"""
    raw_sensor_data = (
        1398,
        1560,
        1488,
        1464,
        1523,
        1697,
        1656,
        1853,
        1635,
        1671,
        1831,
        1646,
        1566,
        1550,
        1760,
        1771,
        1347,
        1409,
        1981,
        1969,
        2244,
        2077,
        2218,
        2188,
        1341,
        1373,
        2170,
        2182,
        2396,
        2234,
        2262,
        2158,
        1946,
        1673,
        2204,
        2257,
        2256,
        2279,
        2273,
        2360,
        1833,
        2055,
        2069,
        2110,
        2146,
        2157,
        2170,
        2212,
        1832,
        1932,
        1905,
        1947,
        1943,
        1966,
        1985,
        1987,
        1766,
        1769,
        1802,
        1804,
        1840,
        1811,
        1826,
        1851,
    )
    return cast(
        Vl53l5cxFrame8x8Data,
        tuple(
            Vl53l5cxZoneReading(value, Vl53l5cxStatus.RANGE_VALID, zone=index)
            for index, value in enumerate(cast(Iterable[int], raw_sensor_data), start=1)
        ),
    )
