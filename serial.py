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
        """Returns current number and iterates current number by one for next call"""
        generated_num = self.current_num
        self.current_num += 1
        return generated_num

    def reset(self):
        """Resets current number to initial value"""
        self.current_num = self.initial_val



    
    


