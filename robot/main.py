from enum import Enum, auto
from robot.config import Config


class State:
    def __init__(self, x, y, step_direction_vector):
        self.x = x
        self.y = y
        self.step_direction_vector = step_direction_vector

    def get_direction_from_vector(self):
        for direction, direction_vector in DIRECTION_VECTORS.items():
            if direction_vector == self.step_direction_vector:
                return direction


DIRECTION_VECTORS = {
    'NORTH': [0, 1],
    'SOUTH': [0, -1],
    'EAST': [1, 0],
    'WEST': [-1, 0]
}


class CommandType(Enum):
    MOVE = auto()
    REPORT = auto()
    LEFT = auto()
    RIGHT = auto()
    PLACE = auto()


# ensure that the agent never steps outside the board
def perform_safe_move(state, step_direction):
    state.x = max(0, min(Config.M, state.x + step_direction[0]))
    state.y = max(0, min(Config.M, state.y + step_direction[1]))


# rotate the agent clockwise or anti-clockwise by updating the facing direction
def rotate(state, is_clockwise):
    state.step_direction_vector = state.step_direction_vector[-1:] + state.step_direction_vector[:-1]
    state.step_direction_vector[is_clockwise] = -state.step_direction_vector[is_clockwise]


# for a 'PLACE' command update the positional info
def update_state(state, x, y, direction):
    if x.isnumeric() and y.isnumeric() and direction.strip() in DIRECTION_VECTORS:
        state.x = int(x)
        state.y = int(y)
        state.step_direction_vector = DIRECTION_VECTORS[direction.strip()]


# perform the appropriate action
def perform_action(state, command):

    command_tokens = command.split(' ')
    command_action = command_tokens[0].strip()

    if command_action == CommandType.MOVE.name:
        step_direction = state.step_direction_vector
        perform_safe_move(state, step_direction)
    elif command_action == CommandType.REPORT.name:
        print('X: ', state.x, ' Y: ', state.y, ' Direction: ', state.get_direction_from_vector())
    elif command_action == CommandType.LEFT.name:
        rotate(state, 0)
    elif command_action == CommandType.RIGHT.name:
        rotate(state, 1)
    elif command_action == CommandType.PLACE.name and len(command_tokens) == 4:
        update_state(state, command_tokens[1], command_tokens[2], command_tokens[3])
    else:
        print('Wrong input ', command_action)


def run(input_file_path):

    state = State(0, 0, DIRECTION_VECTORS['NORTH'])
    with open(input_file_path, 'r') as file_data:
        for command in file_data:
            perform_action(state, command)


run(Config.INPUT_FILE_PATH)