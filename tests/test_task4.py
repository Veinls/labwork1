import pytest
from unittest.mock import MagicMock


def test_method_calls_within_limit():

    @call_limiter(limit=2)
    class TestClass:
        def method1(self):
            return "method1 called"

        def method2(self):
            return "method2 called"

    obj = TestClass()

    # Первые два вызова должны работать
    assert obj.method1() == "method1 called"
    assert obj.method1() == "method1 called"

    # Другой метод тоже должен работать
    assert obj.method2() == "method2 called"