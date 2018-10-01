from collections import defaultdict
class PresitionRecall:
    '''
        A class used to represent the Presition and Recall of queries.

        Presition is defined like:
            |{Relevant documents} ∩ {Retrieved documents}| / |{Retrieved Documents}|

        Recall is defined like:
            |{Relevant documents} ∩ {Retrieved documents}| / |{Relevant Documents}|
    '''
    '''
    {int: [int]}
    '''
    def __init__(self):
        self.qrels = {}
        #self.total_queries = 0

    def insertQuery(self, query_num:  int):
        already_exists = query_num in self.qrels
        if not already_exists:
            self.qrels[query_num] = []

    def insertWord(self, query_num: int, relDoc: int):
        already_exists = relDoc in self.qrels[query_num]
        if not already_exists:
            self.qrels[query_num].append(relDoc)


    def printDictionary(self):
        for id_query, docs in self.qrels.items():
            print(f"{id_query} --> {docs}")
        #print(len(self.qrels.items()))
