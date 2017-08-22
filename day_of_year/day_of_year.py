
def day_of_year(year, month, day):
    """
    :param year: type int and year > 0
    :param month: type int and 0 < month < 12
    :param day: type int and 0 < day < length(month)

    :return: -1 represent an error input
             and a logic number represent the day of the year for that date
    """
    month_day_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    error_day = -1
    which_day = 0

    if not isinstance(year, int) or year < 0:
        return error_day

    if not isinstance(month, int) or month < 1 or month > 12:
        return error_day

    if _is_leap_year(year):
        month_day_list[2] = 29

    if not isinstance(day, int) or day < 0 or day > month_day_list[month]:
        return error_day

    for i in range(1, month):
        which_day += month_day_list[i]

    which_day = which_day + day

    return which_day


def _is_leap_year(year):
    """
    :param year: the year to determine

    :return: True is leap year and False not
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
