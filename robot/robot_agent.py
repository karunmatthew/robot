from error.app_error import CommandError
from robot.agent_state import AgentState
from robot.constants import Constants, CommandType


# The robot class encapsulates all the robot's attributes and actions
class Robot:

    def __init__(self, default_start_x, default_start_y, default_direction,
                 max_columns, max_rows):
        self.state = AgentState(default_start_x,
                                default_start_y,
                                default_direction)
        self.max_columns = max_columns
        self.max_rows = max_rows

    # ensure that the agent never steps outside the board
    # when performing the 'MOVE' action
    def perform_safe_move(self):
        self.state.x = max(0, min(self.max_columns - 1,
                                  self.state.x +
                                  self.state.direction_vector[0]))
        self.state.y = max(0, min(self.max_rows - 1,
                                  self.state.y +
                                  self.state.direction_vector[1]))

    # rotate the agent clockwise or anti-clockwise by updating
    # the facing direction vector
    def rotate(self, is_clockwise):
        self.state.direction_vector = self.state.direction_vector[
                                      -1:] + self.state.direction_vector[:-1]
        self.state.direction_vector[is_clockwise] = - \
            self.state.direction_vector[is_clockwise]

    # perform the appropriate action
    def perform_action(self, command):

        command_tokens = command.strip().split(Constants.DELIMITER)
        command_action = command_tokens[0].strip()

        try:
            if command_action == CommandType.PLACE.name and len(
                    command_tokens) == Constants.PLACE_ACTION_ARGUMENTS:
                self.state.update_agent_state(command_tokens[1],
                                              command_tokens[2],
                                              command_tokens[3])
            elif len(command_tokens) > 1:
                raise CommandError(command_action, 'Extra arguments in action')
            elif command_action == CommandType.MOVE.name:
                self.perform_safe_move()
            elif command_action == CommandType.REPORT.name:
                print('X: ', self.state.x, ' Y: ', self.state.y, ' Direction: ',
                      self.state.get_direction())
            elif command_action == CommandType.LEFT.name:
                self.rotate(Constants.ANTI_CLOCKWISE)
            elif command_action == CommandType.RIGHT.name:
                self.rotate(Constants.CLOCKWISE)

            else:
                raise CommandError(command_action, 'Unknown command')

        except CommandError as e:
            e.print_error_message(command.strip())

    def run(self, input_file_path):
        # read the commands in the input file and execute them one by one
        with open(input_file_path, 'r') as file_data:
            for command in file_data:
                self.perform_action(command)
