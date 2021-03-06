from robot.robot_agent import Robot
import configparser


def main():
    # read the default values from the configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # get the default dimensions of the board
    max_columns = int(config['DEFAULT']['N'])
    max_rows = int(config['DEFAULT']['M'])

    # get path to the command file
    command_file_path = config['DEFAULT']['INPUT_FILE_PATH']

    # get the default starting position and facing direction of the robot
    default_start_x = int(config['DEFAULT']['START_X'])
    default_start_y = int(config['DEFAULT']['START_Y'])
    default_direction = config['DEFAULT']['FACING_DIRECTION']

    # initialize the robot with these default starting values
    robot = Robot(default_start_x, default_start_y, default_direction,
                  max_columns, max_rows)

    # perform the actions present in the command file
    robot.run(command_file_path)


if __name__ == "__main__":
    main()
