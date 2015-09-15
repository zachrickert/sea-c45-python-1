# This program highlights three type of errors: name, attribute and type.


def exhibit_name_error():
    zach


def exhibit_attribute_error():
    import math
    math.zach


def exhibit_type_error():
    True + "super cute cat!"
