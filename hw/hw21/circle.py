#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        '''Initialize circle with a given radius'''

        self.radius = radius
        self.diameter = 2 * radius
        self.area = math.pi * (radius ** 2)

    def __str__(self):
        line = 'Circle with radius:{}'
        line.format(self.radius)
