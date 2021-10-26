from unittest import TestCase
from src.main.python.edu.arizona.cs.queryengineq4 import QueryEngineQ4


class test_q4(TestCase):
    input_path= "src/main/resources/input.txt"

    def test_Q4_3_with_smoothing(self):
        query = ["information", "retrieval"]
        ans=QueryEngineQ4(self.input_path).runQ4_3_with_smoothing(query)
        assert type(ans) is not None
        assert type(ans) is list
        assert len(ans) > 0
        assert len(ans) == 4

        doc_names_q1 = ["Doc1", "Doc2","Doc4","Doc3"]
        assert doc_names_q1[0] == ans[0].doc_id
        assert doc_names_q1[1] == ans[1].doc_id
        assert ans[0].docScore > ans[1].docScore
        assert ans[1].docScore > ans[2].docScore
        assert ans[1].docScore > ans[3].docScore

    def test_Q4_3_without_smoothing(self):
        query = ["information", "retrieval"]
        ans = QueryEngineQ4(self.input_path).runQ4_3_without_smoothing(query)
        assert type(ans) is not None
        assert type(ans) is list
        assert len(ans) > 0
        assert len(ans) == 4

        doc_names_q1 = ["Doc1", "Doc2", "Doc3", "Doc4"]
        assert doc_names_q1[0] == ans[0].doc_id
        assert doc_names_q1[1] == ans[1].doc_id
        assert doc_names_q1[2] == ans[2].doc_id
        assert doc_names_q1[3] == ans[3].doc_id
        assert ans[0].docScore > ans[1].docScore
        assert ans[1].docScore > ans[2].docScore
        assert ans[2].docScore == 0
        assert ans[3].docScore == 0



