import pytest
import io
import sys
from src.task2 import retry


def failing_func(error_type, msg="Error"):
    raise error_type(msg)

def test_success(): # успешное выполнение с первого раза
    counter = 0

    @retry(3, 0.1)
    def success_func():
        nonlocal counter
        counter += 1
        return "success"

    result = success_func()
    assert result == "success"
    assert counter == 1


def test_failure_output_messages(): # вывод при неудачных попытках
    captured_output = io.StringIO()
    original_stdout = sys.stdout

    try:
        sys.stdout = captured_output

        @retry(2, 0.1, [ZeroDivisionError])
        def test_func():
            failing_func(ZeroDivisionError, "Test error")

        with pytest.raises(ZeroDivisionError):
            test_func()

        output = captured_output.getvalue()
        assert "Попытка 1: Test error" in output
        assert "Попытка 2: Test error" in output
        assert "Попытка 3" not in output

    finally:
        sys.stdout = original_stdout


def test_skips_other_exceptions(): # на исключения вне списка

    @retry(3, 0.1,[ZeroDivisionError])
    def test_func():
        failing_func(ValueError, "Wrong type")

    with pytest.raises(ValueError):
        test_func()


def test_retry_until_success(capsys): # успешное выполнение после повторов
    counter = 0

    @retry(3,0.1, [ValueError])
    def eventually_successful():
        nonlocal counter
        counter += 1
        if counter < 2:
            raise ValueError("Not yet")
        return "success"

    result = eventually_successful()
    output = capsys.readouterr().out

    assert result == "success"
    assert counter == 2
    assert "Попытка 1: Not yet" in output