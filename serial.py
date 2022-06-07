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
    def __init__(self, start): # start = 100
        """Sets the starting point for the generator
            start will equal the given starting point.
            count will begin at 0.
        """

        self.start = start
        self.next = start

    def reset(self):
        """Resets the generator back to given start
            sets count back to 0 and returns `None`
        """
        self.next = self.start


    def generate(self):
        """Generates next sequential number
            returns the starting point plus count
            and increments count by 1.
        """
        self.next += 1
        return self.next - 1
    
        
        

        
        


    