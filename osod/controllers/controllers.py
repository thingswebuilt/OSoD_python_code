from dataclasses import dataclass
import logging
from typing import Protocol, Generator
from approxeng.input.selectbinder import ControllerResource
from approxeng.input.controllers import ControllerNotFoundError


@dataclass
class InputStreamItem:
    """Class representing a single item in the input device stream"""

    lx: float
    ly: float


class InputStreamError(Exception):
    """An Input Stream Exception"""

    ...


class InputDevice(Protocol):
    """Protocol class for Input Devices"""

    def get_input_stream(self) -> Generator[InputStreamItem, None, None]:
        """Returns an iterator of InputStreamitems"""
        ...


class PSController:
    """Class for PS Controllers"""

    def get_input_stream(self) -> Generator[InputStreamItem, None, None]:
        """Returns an iterator of InputStreamitems"""
        try:
            with ControllerResource() as joystick:
                logging.debug("connecting joystick..")
                # Loop until we're disconnected
                while joystick.connected:
                    logging.debug("joystick connected..")
                    state: tuple[float, float] = joystick["lx", "ly"]  # type: ignore
                    yield InputStreamItem(*state)
                # logging.debug("joystick disconnected")
        except ControllerNotFoundError as exc:
            logging.info("No controller found")
            raise InputStreamError("No controller found") from exc
        except StopIteration as exc:
            logging.info("could not communicate with controller")
            raise InputStreamError("could not communicate with controller") from exc
