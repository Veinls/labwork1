import pytest
import io
import sys
import time
import task3

class Test:
    @task3.logger
    def normal_method(self, x):
        return x

    def __magic_method__(self, x):
        return x


# def test():
    # captured_output = io.StringIO()
    # sys.stdout = captured_output
    #
    # start_time = time.time()
    # result = Test()
    # result.normal_method(1)
    # result.__magic_method__(1)
    # end_time = time.time()
    #
    # output = captured_output.getvalue()
