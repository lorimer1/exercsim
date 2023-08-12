"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created: int = 0

    def __init__(self, x: int, y: int):
        self.x_coordinate: int = x
        self.y_coordinate: int = y
        self.health: int = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, x: int, y: int):
        self.x_coordinate: int = x
        self.y_coordinate: int = y

    def collision_detection(self, other_object):
        return None


def new_aliens_collection(alien_start_positions: list[tuple]) -> list[Alien]:
    new_aliens_collection = []
    for start_position in alien_start_positions:
        new_aliens_collection.append(Alien(start_position[0], start_position[1]))
    return new_aliens_collection
