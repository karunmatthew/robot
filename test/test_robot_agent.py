import unittest
from robot.config import Config, Direction, CommandType
from robot.robot_agent import Robot


class RobotAgentTest(unittest.TestCase):

    def test_robot_move_action(self):
        robot = Robot()
        robot.perform_action('MOVE')
        assert robot.state.x == 0
        assert robot.state.y == 1
        assert robot.state.direction_vector == [0, 1]

    def test_robot_move_outside_board(self):
        robot = Robot()
        robot.rotate(Config.ANTI_CLOCKWISE)
        robot.perform_action(CommandType.MOVE.name)
        robot.perform_action(CommandType.MOVE.name)
        assert robot.state.x == 0
        assert robot.state.y == 0

    def test_robot_move_outside_board_from_top(self):
        robot = Robot()
        robot.perform_action('PLACE ' + str(Config.N - 1) + ' ' + str(
            Config.M - 1) + ' ' + Direction.NORTH.name)
        assert robot.state.x == (Config.N - 1)
        assert robot.state.y == (Config.M - 1)
        robot.perform_action(CommandType.MOVE.name)
        robot.perform_action(CommandType.MOVE.name)
        assert robot.state.x == (Config.N - 1)
        assert robot.state.y == (Config.M - 1)


if __name__ == '__main__':
    unittest.main()