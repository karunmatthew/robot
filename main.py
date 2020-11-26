from robot.robot_agent import Robot
from robot.config import Config

robot = Robot()
# the path to the input file is given as input
robot.run(Config.INPUT_FILE_PATH)