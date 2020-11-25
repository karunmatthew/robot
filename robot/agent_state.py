from robot.config import DIRECTION_VECTORS


class AgentState:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction_vector = DIRECTION_VECTORS[direction]

    def get_direction(self):
        for direction, direction_vector in DIRECTION_VECTORS.items():
            if direction_vector == self.direction_vector:
                return direction
