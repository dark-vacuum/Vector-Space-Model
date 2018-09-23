class VectorSpaceModel:
    """
    A class used to represent.

    ...

    Attributes
    ----------
    relation_coeficient : {int : [(int, float)]}
        A dictionary of relation coeficient between a query and the
        documents, the key is the number of query and the value is an
        array of tuples with the document number in the first position
        and the coeficient in the second.
    queries : QueryDictionary
        Contains all the queries

    Methods
    -------
    
    """

    def __init__(self, words_Dict, query_Dict):
        self.relation_coeficient = {}
        self.queries = query_Dict
        self.words = words_Dict
        

