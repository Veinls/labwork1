import pytest
import io
import sys
import time
from src.task1 import logger


@logger
def sample_func(a, b):
    time.sleep(0.01)
    return a + b


def test():
    captured_output = io.StringIO()
    original_stdout = sys.stdout
    try:
        sys.stdout = captured_output

        result = sample_func(3, 4)

        output = captured_output.getvalue()

        assert result == 7
        assert "name function:sample_func" in output
        assert "(3, 4)" in output
        assert "7" in output

    finally:
        sys.stdout = original_stdout