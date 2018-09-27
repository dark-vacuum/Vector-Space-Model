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
        self.query_Dict = query_Dict
        self.words_Dict = words_Dict
        self.N = words_Dict.total_documents

    def calculate_Coeficients(self):
        n_queries = 10
        n_documents = 1400
        for id_query, query in list(self.query_Dict.queries.items())[:n_queries]:
            for document in list(self.words_Dict.id_documents)[:n_documents]:
                coeficient = 0
                for query_word, query_incidence in query.items():
                    if query_word in self.words_Dict.words:
                        idf = self.words_Dict.words[query_word].idf(self.N)
                        term_weight_document = self.words_Dict.words[query_word].docs.get(document, 0) * idf
                    else:
                        idf = 0
                        term_weight_document = 0
                    term_weight_query = query_incidence * idf
                    #if id_query == 4 and document == 5:
                    #    print(f"log10({self.N}/{self.words_Dict.words[query_word].length_docs})")
                    #    print(f"(idf, {idf}), (doc, {term_weight_document}), (qry, {term_weight_query})")
                    #    print(f"coef -> {int(coeficient * 1000)/1000}")
                    coeficient += term_weight_document * term_weight_query
                coeficient = int(coeficient * 1000)/1000
                if id_query in self.relation_coeficient:
                    self.relation_coeficient[id_query].append((document, coeficient))
                else:
                    self.relation_coeficient[id_query] = [(document, coeficient)]
            self.relation_coeficient[id_query].sort(key = lambda tup : tup[1], reverse = True)

    def print_VSM(self):
        #print(list(filter(lambda x : x[0] == 184, self.relation_coeficient[1])))
        for id_query, coeficients in self.relation_coeficient.items():
            print(f"{id_query} -> {coeficients}\n")
