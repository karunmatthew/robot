from robot.config import DIRECTION_VECTORS
from robot.validate import validate_command_parameters

# AgentState class captures the state of an agent at any given point of time
#
# The state of a robotic agent is represented by three attributes
# 1. x co-ordinate value
# 2. y co-ordinate value
# 3. a 2D unit vector representing the direction the agent is facing
class AgentState:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        # instead of maintaining the direction string,
        # maintain the direction unit vector for faster updation
        self.direction_vector = DIRECTION_VECTORS[direction]

    # return the direction string corresponding to the direction vector
    def get_direction(self):
        for direction, direction_vector in DIRECTION_VECTORS.items():
            if direction_vector == self.direction_vector:
                return direction

    # update the state of the agent after validating the parameters
    def update_agent_state(self, x, y, direction):
        validate_command_parameters(direction, x, y)
        self.x = int(x)
        self.y = int(y)
        self.direction_vector = DIRECTION_VECTORS[direction.strip()]
