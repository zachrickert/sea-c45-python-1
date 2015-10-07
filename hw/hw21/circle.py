#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        '''Initialize circle with a given radius'''

        self.radius = float(radius)

    def __str__(self):
        line = 'Circle with radius: {:0.6f}'
        line = line.format(self.radius)
        return line

    def __repr__(self):
        return 'Circle({:0.0f})'.format(self.radius)

    def __eq__(self, other):
        return float(self.radius) == float(other.radius)

    def __lt__(self, other):
        return float(self.radius) < float(other.radius)

    def __gt__(self, other):
        return float(self.radius) > float(other.radius)

    def __le__(self, other):
        return float(self.radius) <= float(other.radius)

    def __ge__(self, other):
        return float(self.radius) >= float(other.radius)

    def __add__(self, other):
        return Circle(float(self.radius) + float(other.radius))

    def __mul__(self, multiplier):
        return Circle(float(self.radius) * multiplier)

    def get_diameter(self):
        return self.radius * 2

    def set_diameter(self, diameter):
        if (diameter < 0):
            raise ValueError("Circle cannot have negative diameter.")
        self.radius = diameter / 2.0

    diameter = property(get_diameter, set_diameter)

    def get_area(self):
        return math.pi * self.radius ** 2

    # def set_area(self, area):
    #     if (area < 0):
    #         raise ValueError("Circle cannot have negative area.")
    #     if (area == 44):
    #         raise AttributeError("Your circle can't have an area of 44  :(")
    #     self.radius = math.sqrt(area / math.pi)

    area = property(get_area)
