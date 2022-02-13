"""tests to check tof_tools functions work as expected"""

import pytest
from osod.tof.enums import Vl53l5cxStatus
from osod.tof.models import (
    Vl53l5cxDataFrame1x1,
    Vl53l5cxDataFrame4x4,
    Vl53l5cxDataFrame8x8,
    Vl53l5cxZoneReading,
)


def test_1x1_dataframe_accepts_only_single_zone_reading():
    """test the single zone data model accepts only one zone reading"""
    df_1x1 = Vl53l5cxDataFrame1x1()
    zone_reading = Vl53l5cxZoneReading(
        value=1, status=Vl53l5cxStatus.RANGE_VALID, zone=1
    )
    df_1x1.add_reading(zone_reading)

    with pytest.raises(ValueError):
        zone_reading_2 = Vl53l5cxZoneReading(
            value=1, status=Vl53l5cxStatus.RANGE_VALID, zone=2
        )
        df_1x1.add_reading(zone_reading_2)


def test_4x4_dataframe_accepts_max_16_zone_readings():
    """test the 4x4 zone data model accepts a maximum of 16 zone readings"""
    df_4x4 = Vl53l5cxDataFrame4x4()
    for zone_index in range(1, 17):
        zone_reading = Vl53l5cxZoneReading(
            value=1, status=Vl53l5cxStatus.RANGE_VALID, zone=zone_index
        )
        df_4x4.add_reading(zone_reading)

    with pytest.raises(ValueError):
        zone_reading_2 = Vl53l5cxZoneReading(
            value=1, status=Vl53l5cxStatus.RANGE_VALID, zone=2
        )
        df_4x4.add_reading(zone_reading_2)


def test_8x8_dataframe_accepts_max_64_zone_readings():
    """test the 8x8 zone data model accepts a maximum of 64 zone readings"""
    df_8x8 = Vl53l5cxDataFrame8x8()
    for zone_index in range(1, 65):
        zone_reading = Vl53l5cxZoneReading(
            value=1, status=Vl53l5cxStatus.RANGE_VALID, zone=zone_index
        )
        df_8x8.add_reading(zone_reading)

    with pytest.raises(ValueError):
        zone_reading_2 = Vl53l5cxZoneReading(
            value=1, status=Vl53l5cxStatus.RANGE_VALID, zone=2
        )
        df_8x8.add_reading(zone_reading_2)


def test_dataframe_as_list():
    """test that dataframe returns a list of floats/ints"""
    df_8x8 = Vl53l5cxDataFrame8x8()
    value_list = list(range(1, 65))
    for value in value_list:
        zone_reading = Vl53l5cxZoneReading(
            value=value, status=Vl53l5cxStatus.RANGE_VALID, zone=value
        )
        df_8x8.add_reading(zone_reading)

    assert df_8x8.as_list() == value_list


# def test_8x8_instantiates_correctly(perfect_flat_reading_data: list[int]):
#     """test the single zone data model instantiates correctly"""
#     frame = Vl53l5cxFrame8x8(perfect_flat_reading_data)
#     assert frame.data == perfect_flat_reading_data


# def test_average_for_perfect_flat_reading(perfect_flat_reading: Vl53l5cxFrame):
#     """ "average_distance should always average all provided readings"""
#     assert perfect_flat_reading.average == 1000


# def test_average_for_oblique_reading(oblique_reading: Vl53l5cxFrame):
#     """ "average_distance should always average all provided readings"""
#     assert oblique_reading.average == 1899.75
