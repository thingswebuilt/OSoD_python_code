import logging
import multiprocessing as mp
from typing import Protocol
from approxeng.input.selectbinder import ControllerResource


class InputDevice(Protocol):
    """Protocol class for Input Devices"""

    def start(self) -> None:
        """start reeceicing events from the input device"""
        ...


class PSController:
    """Class for PS Controllers"""

    process: mp.Process

    def connect_joystick(self) -> None:
        """Connect to the joystick resource"""
        with ControllerResource() as joystick:
            logging.debug("connecting joystick..")
            # Loop until we're disconnected
            while joystick.connected:
                # logging.debug("joystick connected")
                # Call check_presses at the top of the loop to check for presses and releases, this returns the buttons
                # pressed, but not the ones released. It does, however, have the side effect of updating the
                # joystick.presses and joystick.releases properties, so you use it even if you're not storing the return
                # value anywhere.
                joystick.check_presses()
                # Check for a button press
                if joystick.presses.circle:
                    logging.info("CIRCLE pressed since last check")
                # Check for a button release
                if joystick.releases.circle:
                    logging.info("CIRCLE released since last check")

                # If we had any releases, print the list of released buttons by standard name
                if joystick.has_releases:
                    logging.info(joystick.releases)
            logging.info("joystick disconnected")

    def start(self) -> None:
        """start getting joystick events"""
        self.process = mp.Process(target=self.connect_joystick)
        self.process.start()
