from dataclasses import dataclass
import logging

from controllers import controllers

logging.basicConfig(level=logging.INFO)


@dataclass
class Robot:
    """robot class"""

    input_device: controllers.InputDevice


def main() -> None:
    """main method"""
    logging.debug("starting main method")
    input_device = controllers.PSController()
    robot = Robot(input_device=input_device)
    robot.input_device.start()
    while True:
        logging.debug("still True")


if __name__ == "__main__":
    main()
