# This file contains the unit test cases for testing methods in agent_state.py

import unittest
from robot.agent_state import AgentState

from robot.constants import Direction


class AgentStateTest(unittest.TestCase):

    def test_agent_state(self):
        agent_state = AgentState(0, 0, Direction.NORTH.name)
        assert agent_state.x == 0
        assert agent_state.y == 0
        assert agent_state.direction_vector == [0, 1]

    def test_agent_state_get_direction(self):
        agent_state = AgentState(0, 0, Direction.SOUTH.name)
        assert agent_state.get_direction() == Direction.SOUTH.name

    def test_update_agent_state(self):
        agent_state = AgentState(0, 0, Direction.SOUTH.name)
        agent_state.update_agent_state('3', '5', Direction.EAST.name)
        assert agent_state.x == 3
        assert agent_state.y == 5
        assert agent_state.direction_vector == [1, 0]


if __name__ == '__main__':
    unittest.main()
