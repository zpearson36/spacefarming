from object import GRAVITATIONAL_CONSTANT, Object

class Orbit(Object):
    """Class to implement orbital influences on multiple bodies"""
    def __init__(self, central_body = None, orbiting_bodies = []):
        if central_body is None:
            raise Exception("No Central Body designated")

        self.central_body = central_body
        self.orbiting_bodies = orbiting_bodies

    def display(self):
        self.central_body.display()
        for obj in self.orbiting_bodies:
            obj.display()

    def orbit(self):
        for obj in self.orbiting_bodies:
            gravitational_acceleration = Object.gravitational_force(self.central_body, obj)
            gravitational_acceleration.magnitude /= obj.mass
            obj.update_velocity(gravitational_acceleration)
