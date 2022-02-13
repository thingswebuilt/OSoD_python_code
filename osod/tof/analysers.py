"""Analysers for ToF data"""
from typing import Optional
from statistics import mean, StatisticsError


class RangeDataAnalyserException(Exception):
    """Base exception for range analysis operations"""


class RangeDataAnalyser:
    """Class for performing various analysis function on range data"""

    data: list[float]

    def __init__(self, data: Optional[list[float]] = None) -> None:
        default_data: list[float] = []
        self.set_data(data if data is not None else default_data)

    def set_data(self, data: Optional[list[float]] = None) -> None:
        """set dataset to supplied data, or empty list if data is None"""
        self.data = data if data is not None else []

    @property
    def average(self) -> float:
        """Return the mean value of the data set"""
        try:
            return mean(self.data)
        except StatisticsError as exc:
            raise RangeDataAnalyserException(
                "Cannot calculate mean of empty list"
            ) from exc
