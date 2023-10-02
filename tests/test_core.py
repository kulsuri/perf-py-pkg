"""Test cases for the core module."""
from perf_py_pkg import core as c


def test_add_one() -> None:
    """Test the add_one function."""
    assert c.add_one(0) == 1
    assert c.add_one(1) == 2
    assert c.add_one(-1) == 0
    assert c.add_one(99) == 100
