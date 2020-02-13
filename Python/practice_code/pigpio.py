import RPi.GPIO as gpio


class Pigpio:
    def __init__(self):
        gpio.setmode(gpio.BOARD)

        self.left = [
            3,
            5,
            7,
            11,
            13,
            15,
            19,
            21,
            23,
            # 27,
            29,
            31,
            33,
            35,
            37
        ]

        self.right = [
            8,
            10,
            12,
            16,
            18,
            22,
            24,
            26,
            # 28,
            32,
            36,
            38,
            40
        ]

    def run(self):
        for pin in self.right:
            print("pin {}".format(pin))
            gpio.setup(pin, gpio.IN)

        for pin in self.left:
            print("pin {}".format(pin))
            gpio.setup(pin, gpio.OUT)
            gpio.output(pin, False)

        while(True):
            print("looping")

    def shutdown(self):
        gpio.cleanup()


if __name__=="__main__":
    app = Pigpio()

    try:
        app.run()

    except KeyboardInterrupt:
        app.shutdown()
