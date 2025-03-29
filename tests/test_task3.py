import pytest
import io
import sys
from src.task3 import logger

class Test:
    @logger
    def normal_method(self, x):
        return x + 4

    def __magic_method(self):
        return "magic off"
    __magic_method = logger(__magic_method, show_magic_methods=False)

    def __magic_method__(self):
        return "magic on"
    __magic_method__ = logger(__magic_method__, show_magic_methods=True)