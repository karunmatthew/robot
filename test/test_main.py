import unittest

from robot.config import Config
from robot.robot_agent import Robot

# Integration test for the robot agent
class MainTest(unittest.TestCase):
    def test_main(self):
        robot = Robot()
        robot.run(Config.INPUT_FILE_PATH)
        assert robot.state.x == 3
        assert robot.state.y == 3
        assert robot.state.direction_vector == [0, 1]


if __name__ == '__main__':
    unittest.main()
