import math

class Position:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x_pos(self):
        return self.__x

    @property
    def y_pos(self):
        return self.__y

    def update_pos(self, x=None, y=None):
        self.__x = x if x is not None else self.__x
        self.__y = y if y is not None else self.__y

    def __add__(self, p2):
        return Position(self.x_pos + p2.x_pos, self.y_pos + p2.y_pos)

    def __sub__(self, p2):
        return Position(self.x_pos - p2.x_pos, self.y_pos - p2.y_pos)

    def distance(self, p2):
        x_2 = (p2.x_pos - self.x_pos) ** 2
        y_2 = (p2.y_pos - self.y_pos) ** 2
        return math.sqrt(x_2 + y_2)

class Vector:
    def __init__(self, magnitude=0, angle=0):
        self.__mag = magnitude
        self.__angle = angle

    @property
    def magnitude(self):
        return self.__mag

    @magnitude.setter
    def magnitude(self, mag):
        self.__mag = mag

    @property
    def angle(self):
        return self.__angle

    def __add__(self, v2):
        length2 = v2.magnitude
        angle2 = v2.angle
        x = math.sin(self.angle) * self.magnitude + math.sin(angle2) * length2
        y = math.cos(self.angle) * self.magnitude + math.cos(angle2) * length2

        magnitude = math.hypot(x, y)
        angle = 0.5 * math.pi - math.atan2(y, x)
        return Vector(magnitude, angle)

    def __neg__(self):
        return Vector(self.magnitude, math.pi - self.angle)

def collide(p1, p2):
    dx = p1.position.x_pos - p2.position.x_pos
    dy = p1.position.y_pos - p2.position.y_pos

    dist = math.hypot(dx, dy)
    if dist < p1.radius + p2.radius:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        # The following block of commented out code is for inelastic collisions.
        # I opted to go for elastic collisions. Keeping this here for posterities sake
        # momentum1 = Vector(p1.velocity.magnitude*p1.mass, p1.velocity.angle)
        # momentum2 = Vector(p2.velocity.magnitude*p2.mass, p2.velocity.angle)
        # total_momentum = momentum1 + momentum2
        # final_velocity = Vector(total_momentum.magnitude/total_mass, total_momentum.angle)
        # p1.velocity = final_velocity
        # p2.velocity = final_velocity

        # Following Vectors represent the change in velocity for each object in an
        # elastic collision
        v1 = Vector(p1.velocity.magnitude*(p1.mass-p2.mass)/total_mass, p1.velocity.angle)
        v2 = Vector((2*p2.velocity.magnitude*p2.mass/total_mass), p2.velocity.angle)
        v3 = Vector(p2.velocity.magnitude*(p2.mass-p1.mass)/total_mass, p2.velocity.angle)
        v4 = Vector((2*p1.velocity.magnitude*p1.mass/total_mass), p1.velocity.angle)

        p1.velocity = v1 + v2
        p2.velocity = v3 + v4
        elasticity =.5 
        p1.velocity.magnitude *= elasticity
        p2.velocity.magnitude *= elasticity
        
        overlap = 0.5*(p1.radius + p2.radius - dist+1)
        p1.position = Position(p1.position.x_pos + math.sin(angle)*overlap, p1.position.y_pos - math.cos(angle)*overlap)
        p2.position = Position(p2.position.x_pos - math.sin(angle)*overlap, p2.position.y_pos + math.cos(angle)*overlap)
