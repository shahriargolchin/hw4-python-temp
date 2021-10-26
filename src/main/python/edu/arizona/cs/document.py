class Document:
    def __init__(self,doc_id,score):
        self.doc_id=doc_id
        self.docScore = score

    def __eq__(self, other):
        assert self.doc_id == other.doc_id

