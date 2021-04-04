import math
import pygame.sprite


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector2(self.x + other.x, self.y + other.y)
        return Vector2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector2(self.x - other.x, self.y - other.y)
        return Vector2(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vector2(self.x * other.x, self.y * other.y)
        return Vector2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Vector2(self.x / other.x, self.y / other.y)
        return Vector2(self.x / other, self.y / other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other

    def unit_vector(self):
        self.x = self.x / math.sqrt(self.x ** 2 + self.y ** 2)
        self.y = self.y / math.sqrt(self.x ** 2 + self.y ** 2)

        return Vector2(self.x, self.y)
#
# def dot(vec1, vec2):
#     return print(vec1.x * vec2.x + vec1.y * vec2.y)
#
#
#
#
# a = Vector2(-1,-1)
# b = Vector2(-50,5)

#
# print(a.unit_vector())
#
# #
# #
# # dot(a,b)
