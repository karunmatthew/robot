# This file lists all the integration tests that should be performed on the code
import configparser
import unittest

from util.constants import Constants
from robot.robot_agent import Robot


# Integration test for the robot agent
class MainTest(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        # get the default dimensions of the board
        self.max_columns = int(config['DEFAULT']['N'])
        self.max_rows = int(config['DEFAULT']['M'])

    def test_main(self):
        robot = Robot(0, 0, 'NORTH', self.max_columns, self.max_rows)
        robot.run(Constants.INPUT_FILE_PATH)
        assert robot.state.x == 3
        assert robot.state.y == 3
        assert robot.state.direction_vector == [0, 1]


if __name__ == '__main__':
    unittest.main()
