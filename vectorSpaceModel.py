class VectorSpaceModel:
    """
    A class used to represent a vector space model and its functioning.

    ...

    Attributes
    ----------
    similarity_coeficient : {int : [(int, float)]}
        A dictionary of similarity coeficient between a query and the
        documents, the key is the number of query and the value is an
        array of tuples with the document number in the first position
        and the coeficient in the second.
    query_Dict : QueryDictionary
        Contains all the queries.
    words_Dict : WordsDictionary
        Contains all the words and the documents where they appear.
    N : int
        Total number of documents.

    Methods
    -------
    calculate_Coeficients()
        Calculate the similarity coeficients between all the querys and
        all the documents.
    sort_Coeficients()
        Sorts the coeficients for every query from higher to lower.
    print_VSM()
        Prints the similarity coeficients.
    """

    def __init__(self, words_Dict, query_Dict):
        self.similarity_coeficient = {}
        self.query_Dict = query_Dict
        self.words_Dict = words_Dict
        self.N = words_Dict.total_documents

    def calculate_Coeficients(self):
        """
        Goes through every word of each query and every document
        getting the idf and saving the similarity coeficient.
        """

        # Goes for every query
        for id_query, query in self.query_Dict.queries.items():
            # Goes for ever document
            for document in self.words_Dict.id_documents:
                coeficient = 0
                # Goes for every word in the query
                for query_word, query_incidence in query.items():
                    # Checking for the a query term in the document
                    if query_word in self.words_Dict.words:
                        # Getting the idf of the term
                        idf = self.words_Dict.words[query_word].idf(self.N)
                        # Term weight of the document
                        term_weight_document = self.words_Dict.words[query_word].docs.get(document, 0) * idf
                    else:
                        idf = 0
                        term_weight_document = 0
                    # Term weight of the query
                    term_weight_query = query_incidence * idf
                    # Similarity coeficient between the query and the document
                    coeficient += term_weight_document * term_weight_query
                # Making the coeficient up to 3 decimal points
                coeficient = int(coeficient * 1000)/1000
                # Creating or appending the coeficient with a document
                if id_query in self.similarity_coeficient:
                    self.similarity_coeficient[id_query].append((document, coeficient))
                else:
                    self.similarity_coeficient[id_query] = [(document, coeficient)]
    
    def sort_Coeficients(self):
        """
        Sorts the coeficients from higher to lower.
        """

        for coeficients in self.similarity_coeficient.values():
            coeficients.sort(key = lambda tup : tup[1], reverse = True)

    def print_VSM(self, limit:  int):
        """
        Prints the Vector Space Model with the a limit of coeficients.

        Parameters
        ----------
        limit : int
            Number of coeficients to show for each document.
        """

        #print(list(filter(lambda x : x[0] == 184, self.relation_coeficient[1])))
        for id_query, coeficients in self.similarity_coeficient.items():
            print(f"{id_query} -> {coeficients[:limit]}\n")

