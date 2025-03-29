import pytest
import asyncio
import time
import io
import sys
from task5 import function1, function2

pytestmark = pytest.mark.asyncio


async def test_async_functions():
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        start_time = time.time()
        await asyncio.gather(function1(), function2())
        end_time = time.time()

        output = captured_output.getvalue()

        assert "Function 1 - Start" in output
        assert "Function 2 - Start" in output
        assert "Function 1 - Middle" in output
        assert "Function 2 - Middle 1" in output
        assert "Function 2 - Middle 2" in output
        assert "Function 1 - End" in output
        assert "Function 2 - End" in output

        execution_time = end_time - start_time
        assert 4.5 <= execution_time <= 5.5

    finally:
        sys.stdout = sys.__stdout__