import math

class Test_Circle:
    radius = 2
    def test_radius(self, radius):
        radius = 2
        if radius < 0:
            raise ValueError("positive radius expected")
        self.radius = radius

    def test_area(self):
        assert self.radius >= 0, "positive radius expected"
        # assert math.pi * self.radius ** 2

