from serial import Serial


class ArduinoController:
    def __init__(self, port="/dev/ttyACM0", baudrate=9600, timeout=0.1):
        self.arduino = Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout
        )

    def write(self, text):
        self.arduino.write(bytes(text, 'utf-8'))

