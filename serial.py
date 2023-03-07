class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create a new Serial Generator using num argument"""
        self.start = start
        self.initial_value = start

    def generate(self):
        """Prints initial value of start on first call, adds one for subsequent calls"""
        print(self.start)
        self.start += 1

    def reset(self):
        """Resets start number to initial value"""
        self.start = self.initial_value



    
    


