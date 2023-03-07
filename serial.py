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
        self.current_num = start
        self.initial_val = start

    def generate(self):
        """Prints initial value of start on first call, adds one for subsequent calls"""
        generated_num = self.current_num
        self.current_num += 1
        return generated_num

    def reset(self):
        """Resets start number to initial value"""
        self.current_num = self.initial_val



    
    


