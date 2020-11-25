from robot.agent_state import AgentState
from robot.app_error import CommandArgumentError, CommandError
from robot.config import Config, DIRECTION_VECTORS, CommandType, Direction
from robot.util import validate_command_parameters


class Robot:

    def __init__(self):
        self.state = AgentState(Config.DEFAULT_START_X,
                                Config.DEFAULT_START_Y,
                                Direction.NORTH.name)

    def perform_safe_move(self):
        self.state.x = max(0, min(Config.N - 1, self.state.x + self.state.direction_vector[0]))
        self.state.y = max(0, min(Config.M - 1, self.state.y + self.state.direction_vector[1]))

    # rotate the agent clockwise or anti-clockwise by updating the facing direction
    def rotate(self, is_clockwise):
        self.state.direction_vector = self.state.direction_vector[-1:] + self.state.direction_vector[:-1]
        self.state.direction_vector[is_clockwise] = -self.state.direction_vector[is_clockwise]

    # for a 'PLACE' command update the positional info
    def update_state(self, x, y, direction):
        validate_command_parameters(direction, x, y)
        self.state.x = int(x)
        self.state.y = int(y)
        self.state.direction_vector = DIRECTION_VECTORS[direction.strip()]

    # perform the appropriate action
    def perform_action(self, command):

        command_tokens = command.split(Config.DELIMITER)
        command_action = command_tokens[0].strip()

        try:
            if command_action == CommandType.MOVE.name:
                self.perform_safe_move()
            elif command_action == CommandType.REPORT.name:
                print('X: ', self.state.x, ' Y: ', self.state.y, ' Direction: ', self.state.get_direction())
            elif command_action == CommandType.LEFT.name:
                self.rotate(Config.ANTI_CLOCKWISE)
            elif command_action == CommandType.RIGHT.name:
                self.rotate(Config.CLOCKWISE)
            elif command_action == CommandType.PLACE.name and len(command_tokens) == 4:
                self.update_state(command_tokens[1], command_tokens[2], command_tokens[3])
            else:
                raise CommandError(command_action, 'Unknown command')

        except CommandError as e:
            e.print_error_message(command.strip())

    def run(self, input_file_path):

        with open(input_file_path, 'r') as file_data:
            for command in file_data:
                self.perform_action(command)

