from unittest import TestCase
from src.main.python.edu.arizona.cs.queryengineq5 import QueryEngineQ5


class test_q4(TestCase):
    def testQ5_2_f1score(self):
        ans=QueryEngineQ5().runQ5_2_f1score()
        assert type(ans) is not None
        assert ans > 0.8



