import unittest

from error.app_error import CommandArgumentError
from robot.config import Direction
from robot.validate import validate_command_parameters


class ValidateTest(unittest.TestCase):
    def test_validate_command_parameters(self):
        self.assertRaises(CommandArgumentError, validate_command_parameters,
                          'NORTHWEST', '2', '3')
        self.assertRaises(CommandArgumentError, validate_command_parameters,
                          Direction.NORTH.name, '-2', '3')
        self.assertRaises(CommandArgumentError, validate_command_parameters,
                          Direction.SOUTH.name, '2', '-3')
        self.assertRaises(CommandArgumentError, validate_command_parameters,
                          Direction.EAST.name, '0.2', '3')


if __name__ == '__main__':
    unittest.main()
