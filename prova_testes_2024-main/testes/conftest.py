import pytest
from stat_funcs import StatsN2

@pytest.fixture
def example_data():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def example_weights():
    return [0.1, 0.2, 0.3, 0.4, 0.5]

@pytest.fixture(autouse=True)
def set_precision():
    yield
    pytest.approx._DEFAULT_RELATIVE = 1e-6
    pytest.approx._DEFAULT_ABSOLUTE = 0.0