import unittest

from basicrepo.defaultmodule import DefaultClass


class Test(unittest.TestCase):

    def test_defaultFunction(self):
        DefaultClass.defaultFunction()
        assert(True)