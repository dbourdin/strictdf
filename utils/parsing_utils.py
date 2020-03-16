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
