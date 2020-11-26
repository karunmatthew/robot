import unittest
from robot.agent_state import AgentState
from robot.config import Direction


class AgentStateTest(unittest.TestCase):

    def test_agent_state(self):
        agent_state = AgentState(0, 0, Direction.NORTH.name)
        assert agent_state.x == 0
        assert agent_state.y == 0
        assert agent_state.direction_vector == [0, 1]

    def test_agent_state_direction_vector(self):
        agent_state = AgentState(0, 0, Direction.SOUTH.name)
        assert agent_state.get_direction() == Direction.SOUTH.name


if __name__ == '__main__':
    unittest.main()
