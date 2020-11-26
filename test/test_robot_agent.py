import configparser
import unittest

from robot.constants import Constants, Direction, CommandType
from robot.robot_agent import Robot


class RobotAgentTest(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        # get the default dimensions of the board
        self.max_columns = int(config['DEFAULT']['N'])
        self.max_rows = int(config['DEFAULT']['M'])

    def test_robot_move_action(self):
        # the agent should move in the direction it is facing
        robot = Robot(0, 0, 'NORTH', self.max_columns, self.max_rows)
        robot.perform_action('MOVE')
        self.assert_robot_state(robot, 0, 1, [0, 1])

    def test_robot_left_action(self):
        # the agent should move in the direction it is facing
        robot = Robot(0, 0, 'NORTH', self.max_columns, self.max_rows)
        robot.perform_action('LEFT')
        self.assert_robot_state(robot, 0, 0, [-1, 0])

    def test_robot_right_action(self):
        # the agent should move in the direction it is facing
        robot = Robot(0, 0, 'NORTH', self.max_columns, self.max_rows)
        robot.perform_action('RIGHT')
        self.assert_robot_state(robot, 0, 0, [1, 0])

    def test_robot_move_outside_board(self):
        # robot should ignore commands to move outside the board
        robot = Robot(0, 0, 'NORTH', self.max_columns, self.max_rows)
        robot.rotate(Constants.ANTI_CLOCKWISE)
        robot.perform_action(CommandType.MOVE.name)
        robot.perform_action(CommandType.MOVE.name)
        self.assert_robot_state(robot, 0, 0, [-1, 0])

    def test_robot_action_with_extra_arguments(self):
        # should not perform action if extra arguments are passed in
        robot = Robot(0, 0, 'NORTH', self.max_columns, self.max_rows)
        robot.perform_action('MOVE 222')
        self.assert_robot_state(robot, 0, 0, [0, 1])
        robot.perform_action('LEFT JUNK VALUE')
        self.assert_robot_state(robot, 0, 0, [0, 1])
        robot.perform_action('RIGHT -$$$-')
        self.assert_robot_state(robot, 0, 0, [0, 1])

    def test_robot_move_outside_board_from_top(self):
        # the agent should not move beyond the limits of the board
        # even when asked to
        robot = Robot(0, 0, 'NORTH', self.max_columns, self.max_rows)
        robot.perform_action('PLACE ' +
                             str(self.max_columns - 1) + ' ' +
                             str(self.max_rows - 1) + ' ' +
                             Direction.NORTH.name)
        self.assert_robot_state(robot,
                                self.max_columns - 1, self.max_rows - 1, [0, 1])
        robot.perform_action(CommandType.MOVE.name)
        robot.perform_action(CommandType.MOVE.name)
        self.assert_robot_state(robot,
                                self.max_columns - 1, self.max_rows - 1, [0, 1])

    # checks that the robot is at the specified state
    def assert_robot_state(self, robot, x, y, direction):
        assert robot.state.x == x
        assert robot.state.y == y
        assert robot.state.direction_vector == direction


if __name__ == '__main__':
    unittest.main()
