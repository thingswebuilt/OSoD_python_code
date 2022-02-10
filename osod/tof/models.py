from enum import Enum, auto
from statistics import mean


class Vl53l5cxMode(Enum):
    """Vl53l5cx modes"""

    SINGLE = auto()
    FOURBYFOUR = auto()
    EIGHTBYEIGHT = auto()


class Vl53l5cxReading:
    """A single reading from a vl53l5cx sensor"""

    data: list[int]
    mode: Vl53l5cxMode

    expected_list_length = {
        Vl53l5cxMode.EIGHTBYEIGHT: 64,
        Vl53l5cxMode.FOURBYFOUR: 16,
        Vl53l5cxMode.SINGLE: 1,
    }

    def __init__(
        self, values: list[int], mode: Vl53l5cxMode = Vl53l5cxMode.EIGHTBYEIGHT
    ) -> None:
        # do we have the correct number of items?
        num_values = len(values)
        expected_num_values = self.expected_list_length[mode]

        if num_values != self.expected_list_length[mode]:
            raise ValueError(
                (
                    f"Unexpected number of data elements for TofValue."
                    f"Expected {expected_num_values}, received {num_values}"
                )
            )

        # are they all ints?
        if not all(isinstance(value, int) for value in values):  # type: ignore
            raise ValueError("Only ints are accepted in sensor data")

        self.mode = mode
        self.data = values

    @property
    def average(self) -> float:
        """Return averge ranging value"""
        return mean(self.data)
