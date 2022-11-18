from serial import Serial


class ArduinoController:
    def __init__(self, port, baudrate, timeout):
        self.arduino = Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout
        )

    def write(self, text):
        self.arduino.write(bytes(text, 'utf-8'))

