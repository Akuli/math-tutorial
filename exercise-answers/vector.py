import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    @property
    def length(self):
        return math.hypot(self.x, self.y)

    @length.setter
    def length(self, new_length):
        old_length = math.hypot(self.x, self.y)
        scale = new_length / old_length
        self.x = self.x * scale
        self.y = self.y * scale

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    @angle.setter
    def angle(self, new_angle):
        length = math.hypot(self.x, self.y)
        self.x = math.cos(new_angle) * length
        self.y = math.sin(new_angle) * length


v = Vector(1, 2)
v.x
v.y
v.length
v.angle
v.angle = math.radians(45)     # 45° in radians
v
v.length = 0        # lol
v
