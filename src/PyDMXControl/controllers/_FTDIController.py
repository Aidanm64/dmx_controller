"""
 *  PyDMXControl: A Python 3 module to control DMX using OpenDMX or uDMX.
 *                Featuring fixture profiles, built-in effects and a web control panel.
 *  <https://github.com/MattIPv4/PyDMXControl/>
 *  Copyright (C) 2022 Matt Cowley (MattIPv4) (me@mattcowley.co.uk)
"""

from time import sleep
from typing import List

from pylibftdi import Device
from ._TransmittingController import TransmittingController


class FTDIController(TransmittingController):

    def __init__(self, port, *args, **kwargs):
        """
        Serial port interface requires port string to establish connection, e.g. 'COM1' for
        windows operating systems.

        Parameters
        ----------
        port: Serial port string.
        """

        # Store the port and device
        self.__port = port
        self.__device = None
        super().__init__(*args, **kwargs)

    def _connect(self):
        # Try to close if exists
        if self.__device is not None:
            try:
                self.__device.close()
            except Exception:
                pass

        # Get new device
        self.__device = Device(port=self.__port)
        self.__device.baudrate = 250000
        self.__device.ftdi_fn.ftdi_set_line_property(8, 2, 0) # 8 bit word, 2 stop bit, no parity

    def _close(self):
        self.__device.close()
        print("CLOSE: Serial port closed")

    def _transmit(self, frame: List[int], first: int):
        # Convert to a bytearray and pad the start of the frame
        # We're transmitting direct DMX data here, so a frame must start at channel 1, but can end early
        data = bytearray(([0] * (first - 1)) + frame)

        # The first byte in the type, and is `0` for normal DMX data
        data.insert(0, 0)

        # Write
        self.__device.setBaudRate(300)
        sleep(10e-6)
        self.__device.setBaudRate(250000)
        self.__device.write(bytes(data))
