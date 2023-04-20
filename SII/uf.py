import calendar
from datetime import datetime
from typing import Union

from .core import get_html_content, extract_uf_table
from .exceptionsii import YearError, MonthError, DayError, InvalidDateError, UFError

ENDPOINT_URL = 'https://www.sii.cl/valores_y_fechas/uf/uf'


def lookup_uf_month_year(month: Union[int, str] = None, year: int = None, day: int = None):
    """
    Retrieves the Unidad de Fomento (UF) value for the specified month and year.

    :param day: The day for which to retrieve the UF value. If not specified, defaults to all days.
    :param year: The year for which to retrieve the UF value. If not specified, defaults to the
    current year.
    :param month: The month in Spanish for which to retrieve the UF value. Can be an integer (1-12) or a string (
    e.g., 'Mayo').

    """

    if day and not month and not year:
        raise UFError("Day specified without month and year")

    # Data dictionary
    data_dict = {}

    # If only year is specified, that means, day and month are not specified
    if year and not month and not day:
        if isinstance(year, int) and year <= 2013:
            raise YearError("Year must be greater than 2013, value received: " + str(year))

        html = get_html_content(ENDPOINT_URL + str(year) + '.htm')
        for _month in calendar.month_name[1:]:
            data_ = extract_uf_table(html, 'mes_' + _month.lower())
            if not data_:
                return data_dict
            else:
                data_dict[_month.lower()] = {k: v for d in data_ for k, v in d.items()}

        return data_dict

    if not year:
        year = str(datetime.now().year)
    else:

        if isinstance(year, int) and year <= 2013:
            raise YearError("Year must be greater than 2013, value received: " + str(year))

        if isinstance(year, str) and int(year) <= 2013:
            raise YearError("Year must be greater than 2013, value received: " + str(year))

        if not isinstance(year, str) and not isinstance(year, int):
            raise YearError("Year must be a valid number or string, value received: " + str(year))

    if not month:
        month = datetime.now()
    else:
        if isinstance(month, int):
            month = datetime.strptime(str(month), '%m')
        elif isinstance(month, str):

            if month.lower() not in calendar.month_name:
                raise MonthError("Month must be a valid month in Spanish, value received " + str(month))

            month = datetime.strptime(month, '%B')

        else:
            raise MonthError("Month must be a valid number or string, value received: " + str(month))

    if day:
        # Check if day is a valid number and is greater than 1 and less than 31
        if isinstance(day, str):
            if not day.isdigit():
                raise DayError("Day must be a valid number, value received: " + str(day))
        elif not isinstance(day, int):
            raise DayError("Day must be a valid number, value received: " + str(day))

        elif day < 1 or day > 31:
            raise DayError("Day must be a valid number between 1 and 31, value received: " + str(day))

    url = ENDPOINT_URL + str(year) + '.htm'
    html = get_html_content(url)

    current_month_name = month.strftime("%B").lower()

    if html:

        data_ = extract_uf_table(html, 'mes_' + current_month_name)

        if day:
            data_ = {k: v for d in data_ for k, v in d.items()}
            return data_[str(day)]

        return {k: v for d in data_ for k, v in d.items()}

    return None


def lookup_uf_date(date: str) -> Union[None, dict, list]:
    """
    Retrieves the Unidad de Fomento (UF) value for a specified date.

    :param date: The date for which to retrieve the UF value in the format 'dd-mm-yyyy'.
    :type date: str
    :return: The UF value for the specified date. If the specified date is invalid or the webpage containing the UF values
    cannot be retrieved, None is returned. If the specified date is valid but the UF value is not available, an empty list
    is returned.
    :rtype: dict or list or None
    """
    # Check if date format is valid

    try:
        date = datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
        raise InvalidDateError("Date format must be 'dd-mm-yyyy', value received: " + str(date))

    return lookup_uf_month_year(month=date.month, year=date.year, day=date.day)
