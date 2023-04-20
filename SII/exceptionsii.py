# Create exception classes
class YearError(Exception):
    """
    Exception raised for errors in the year.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MonthError(Exception):
    """
    Exception raised for errors in the month.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class DayError(Exception):
    """
    Exception raised for errors in the day.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidDateError(Exception):
    """
    Exception raised for errors in the date.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class UFError(Exception):
    """
    Exception raised for errors when retrieving the UF value(s).
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
