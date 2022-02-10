from typing import TypeAlias

TofReading: TypeAlias = tuple[
    int,
    int,
    int,
    int,
    int,
    int,
    int,
    int,
]

TofReadingSet: TypeAlias = tuple[
    TofReading,
    TofReading,
    TofReading,
    TofReading,
    TofReading,
    TofReading,
    TofReading,
    TofReading,
]
