"""Test cases for the core module."""
from perf_py_pkg import core as c


def test_add_one() -> None:
    """Test the add_one function."""
    assert c.add_one(0) == 1
    assert c.add_one(1) == 2
    assert c.add_one(-1) == 0
    assert c.add_one(99) == 100

def test_about_me() -> None:
    """Test the function with a sample name."""
    assert c.about_me("Alice") == "The wise Alice loves Python."
    assert c.about_me("Bob") == "The wise Bob loves Python."

def test_ExampleClass_init() -> None:
    """Test the constructor and the `name` attribute assignment"""
    example = c.ExampleClass("TestInstance")
    assert example.name == "TestInstance"

def test_ExampleClass_about_self() -> None:
    """Test the about_self method."""
    example = c.ExampleClass("TestInstance")
    assert example.about_self() == "I am a very smart TestInstance object."