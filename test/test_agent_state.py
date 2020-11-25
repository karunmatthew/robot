from robot.agent_state import AgentState


def test_agent_state():
    agent_state = AgentState(0, 0, 'NORTH')
    assert agent_state.x == 0
    assert agent_state.y == 0
    assert agent_state.direction_vector == [0, 1]


def test_agent_state_direction_vector():
    agent_state = AgentState(0, 0, 'SOUTH')
    assert agent_state.get_direction() == 'SOUTH'


test_agent_state()
test_agent_state_direction_vector()