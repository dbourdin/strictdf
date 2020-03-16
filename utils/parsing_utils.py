def is_float(value):
    """
    Will return True if the object can be converted to float.
    :param value: object
        An object like a String or a number that needs to be tested if it can
        be parsed to a float.
    :return: bool
        Whether the value can or can't be parsed as a float.
    """
    try:
        float(value)
    except ValueError:
        return False
    return True


def is_integer(value):
    """
    Will return True if the object can be converted to int.
    :param value: object
        An object like a String or a number that needs to be tested if it can
        be parsed to an int.
    :return: bool
        Whether the value can or can't be parsed as an int.
    """
    return is_float(value) and float(value).is_integer()


def str_to_bool(value):
    if value in ('True', 'true'):
        return True
    elif value in ('False', 'false'):
        return False
    else:
        raise ValueError


def is_bool(value):
    """
    Will return True if the object can be converted to int.
    :param value: object
        An object like a String or a number that needs to be tested if it can
        be parsed to an int.
    :return: bool
        Whether the value can or can't be parsed as a boolean.
    """
    return value in ('True', 'true', 'False', 'false')


def is_int_boolean_column(column):
    """
    :param column: pd.Series
        The column to be analyzed if it should be converted to bool
    :return: bool
        Whether all the int values on the column are 1/0 and can be defined as
        booleans.
    """
    if column.dtype != 'int64':
        return False
    return column.isin((0, 1)).all()
