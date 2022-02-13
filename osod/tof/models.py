"""models related to time of Flight sensors"""
from dataclasses import dataclass
from typing import TypeAlias

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


Vl53l5cxFrame1x1Data: TypeAlias = Vl53l5cxZoneReading

Vl53l5cxFrame4x4Data: TypeAlias = tuple[
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
]

Vl53l5cxFrame8x8Data: TypeAlias = tuple[
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
    Vl53l5cxZoneReading,
]


@dataclass
class Vl53l5cxFrame1x1:
    """All readings for a single 'frame' from a VL53L5CX"""

    data: Vl53l5cxFrame1x1Data


@dataclass
class Vl53l5cxFrame4x4:
    """All readings for a single 'frame' from a VL53L5CX"""

    data: Vl53l5cxFrame4x4Data


@dataclass
class Vl53l5cxFrame8x8:
    """All readings for a single 'frame' from a VL53L5CX"""

    data: Vl53l5cxFrame8x8Data
