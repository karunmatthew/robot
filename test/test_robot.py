from robot.config import Config, Direction
from robot.robot_agent import Robot


def test_robot_move_action():
    robot = Robot()
    robot.perform_action('MOVE')
    assert robot.state.x == 0
    assert robot.state.y == 1
    assert robot.state.direction_vector == [0, 1]


def test_robot_move_outside_board():
    robot = Robot()
    robot.rotate(Config.ANTI_CLOCKWISE)
    robot.perform_action('MOVE')
    robot.perform_action('MOVE')
    assert robot.state.x == 0
    assert robot.state.y == 0


def test_robot_move_outside_board_from_top():
    robot = Robot()
    robot.perform_action('PLACE ' + str(Config.N - 1) + ' ' + str(Config.M - 1) + ' ' + Direction.NORTH.name)
    assert robot.state.x == (Config.N - 1)
    assert robot.state.y == (Config.M - 1)
    robot.perform_action('MOVE')
    robot.perform_action('MOVE')
    assert robot.state.x == (Config.N - 1)
    assert robot.state.y == (Config.M - 1)