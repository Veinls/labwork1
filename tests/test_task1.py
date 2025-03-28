import pytest
import io
import sys
import task1

@task1.logger
def test_function():
    return

def test():
    captured_output = io.StringID()
    sys.stdout = captured_output

    test_function()

    output = sys.__stdout__.getvalue()

    assert output == ""


