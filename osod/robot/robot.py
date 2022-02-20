from dataclasses import dataclass, field
import logging
from typing import Generator
from controllers import controllers


@dataclass
class Robot:
    """robot class"""

    input_device: controllers.InputDevice
    input_stream: Generator[controllers.InputStreamItem, None, None] = field(init=False)
    is_running: bool = field(default=False, init=False)

    def start(self) -> None:
        """Set robot into 'running' mode"""
        # pylint: disable=assignment-from-no-return
        self.input_stream = self.input_device.get_input_stream()
        self.is_running = True

    def stop(self) -> None:
        """Set robot into 'stopped' mode"""
        self.is_running = False

    def loop(self) -> None:
        """Perform event loop for robot"""
        if self.is_running:
            try:
                result = next(self.input_stream)
                logging.info(result)
            except (controllers.InputStreamError, StopIteration):
                # pylint: disable=assignment-from-no-return
                logging.info("input stream error")
                self.input_stream = self.input_device.get_input_stream()
