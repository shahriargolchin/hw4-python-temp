from src.main.python.edu.arizona.cs.document import Document

class QueryEngineQ4:

    def __init__(self,input_file):
        # add your code here
        pass


    #This method computes the parameters of the language model".
    def buildmodel(self):
        pass

    '''List of documents that you return for runQ4_3_with_smoothing 
    must be sorted in the descending order of scores. '''

    def runQ4_3_with_smoothing(self,query):
        # dummy code. add your code here
        ans=[]
        ans1 = Document("Doc1",0.4)
        ans2 = Document("Doc2",0.3)
        ans3 = Document("Doc4",0.2)
        ans4 = Document("Doc3",0.5)
        ans.append(ans1)
        ans.append(ans2)
        ans.append(ans3)
        ans.append(ans4)
        return ans

    '''    
    List of documents that you return for runQ4_3_without_smoothing must be sorted in descending order of scores. Even documents with score=0 must be returned.
     '''
    def runQ4_3_without_smoothing(self,query):
        # dummy code. add your code here
        ans=[]
        ans1 = Document("Doc1",0.4)
        ans2 = Document("Doc2",0.3)
        ans3 = Document("Doc3",1)
        ans4 = Document("Doc4",1)
        ans.append(ans1)
        ans.append(ans2)
        ans.append(ans3)
        ans.append(ans4)
        return ans
