class SomeExampleApp:
    """This is example of documented class. Just powers two numbers
    and increments call count.

    >>> from package.app import SomeExampleApp
    >>> app = SomeExampleApp()
    >>> app.power(2, 3)
    8
    >>> app.ncalls
    1
    """
    def __init__(self, name: str = 'app'):
        self.name = name
        self.ncalls = 0

    def power(self, num: int, times: int) -> int:
        """Power number by given times."""
        self.ncalls += 1
        return num ** times
