import logging

from controllers import controllers
from robot.robot import Robot

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """main method"""
    logging.debug("starting main method")
    input_device = controllers.PSController()
    robot = Robot(input_device=input_device)
    robot.start()
    while True:
        robot.loop()


if __name__ == "__main__":
    main()
