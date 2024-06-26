from colorpoint import ColorPoint
#the idea is to make x an y protected from being written after initialization.
#there is still a way to hack it through ._color
class AdvancedColorPoint(ColorPoint):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

new_point = AdvancedColorPoint(10, 10, "blue")
print(new_point)
new_point.color = "red"
print(new_point)