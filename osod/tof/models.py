"""models related to time of Flight sensors"""
from dataclasses import dataclass

from osod.tof.enums import Vl53l5cxStatus


@dataclass
class Vl53l5cxZoneReading:
    """A distance reading for a single zone of a vl53l5cx"""

    value: int
    status: Vl53l5cxStatus
    zone: int

    def __post_init__(self):
        if self.zone < 0 or self.zone > 64:
            raise ValueError("Zone must be between 1 and '64'")


class Vl53lcxDataFrameBase:
    """A single data frame of readings froma vl53l5cx sensor."""

    data: list[Vl53l5cxZoneReading]
    max_readings: int

    def __init__(self) -> None:
        self.data = []
        self.max_readings = 0

    def add_reading(self, reading: Vl53l5cxZoneReading) -> None:
        """add a single Vl53l5cx zone reading to the data frame"""
        if len(self.data) == self.max_readings:
            raise ValueError(
                (
                    f"Cannot add reading. Max number of readings for "
                    f"{self.__class__.__name__} is {self.max_readings}"
                )
            )

        self.data.append(reading)

    def as_list(self) -> list[float]:
        """return all values as a list"""
        return [item.value for item in self.data]


class Vl53l5cxDataFrame1x1(Vl53lcxDataFrameBase):
    """A single data frame of readings from vl53l5cx sensor in 1x1 mode"""

    def __init__(self) -> None:
        super().__init__()
        self.max_readings = 1


class Vl53l5cxDataFrame4x4(Vl53lcxDataFrameBase):
    """A single data frame of readings from vl53l5cx sensor in 4x4 mode"""

    def __init__(self) -> None:
        super().__init__()
        self.max_readings = 16


class Vl53l5cxDataFrame8x8(Vl53lcxDataFrameBase):
    """A single data frame of readings from vl53l5cx sensor in 8x8 mode"""

    def __init__(self) -> None:
        super().__init__()
        self.max_readings = 64
