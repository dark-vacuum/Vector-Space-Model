from Dictionaries import WordsDictionary, QueryDictionary, RelevancesDictionary, PresitionRecallDictionary
from vectorSpaceModel import VectorSpaceModel
from presitionRecall import PresitionRecall
from functools import reduce
from graphing import Graphing

"""
    Equipo:
        Luis Alberto Flores Sanchez
        Luis Antonio Vazquez Garcia
"""



def replace(token: str) -> str:
    """
    Receives a word which could be a number or a word or a word
    with symbols and if the string has any af the specified
    symbols they will be removed.

    Attributes
    ----------
    symbols_toRemove : [str]
        The symbols we want to remove in the string

    Parameters
    ----------
    token : str
        The word which is going to be cleanned.

    Returns
    -------
    token : str
        A string without symbols like ".", ",", "'", "(", ")", "/".
    """

    symbols_toRemove = [".", ",", "'", "(", ")", "/"]

    try:
        float(token)
    except ValueError:
        # Use of the function reduce to apply the replace to each symbol
        token = reduce(lambda x, y : x.replace(y, ""), symbols_toRemove, token)

    return token


def read_CranfieldCollection(file: str, dictionary):
    """
    Receives a file of the Cranfield Collection, it could be the
    documents or the queries, reads the file and stores the information
    in 'dictionary'.

    Attributes
    ----------
    indicators : set(str)
        The indicators in the documents of the Cranfild Collection.
    indicators_toAvoid : set(str)
        Which of the content of the indicators we want to avoid.

    Parameters
    ----------
    file : str
        The path or the name of the documents of the Cranfield
        Collection.
    dictionary : WordsDictionary or QueryDictionary
        The dictionary where the words will be stored.

    Returns
    -------
    Returns a class WordsDictionary or QueryDictionary, depending on
    the input.
    """

    indicators = {".I", ".T", ".A", ".B", ".W"}
    indicators_toAvoid = {".T", ".A", ".B"}

    # Lectura del archivo linea por linea.
    with open(file) as document:
        avoid_line = False
        current_doc = 0
        for line in document:
            arr_line = line.split()
            if arr_line[0] in indicators:
                if arr_line[0] == ".I":
                    current_doc = int(arr_line[1])
                    if type(dictionary) == WordsDictionary:
                        dictionary.total_documents += 1
                avoid_line = True if arr_line[0] in indicators_toAvoid else False
                continue
            if avoid_line:
                continue
            arr_line = list(filter(lambda x : x != "", map(lambda x : replace(x), arr_line)))
            for word in arr_line:
                dictionary.createIfNotExists(word, current_doc)
    return dictionary


def read_CranfieldRelevances(file: str, relevances_Dict: RelevancesDictionary) -> RelevancesDictionary:
    """
    Reads the cranfield relevances of the docuement.

    Parameters
    ----------
    file : str
        Filename of the document with relevance relations.
    relevances_Dict : PresitionRecall
        .

    Returns
    -------
    Returns
    """

    # Lectura del archivo linea por linea.
    with open(file) as document:
        for line in document:
            arr_line = line.split()
            query = int(arr_line[0])
            number = int(arr_line[1])
            relevances_Dict.insertDoc(query, number)

    return relevances_Dict




def main():
    # Name of files to read
    cranfield_docs = "cran.all.1400"
    cranfield_queries = "cran.qry"
    cranfield_qrels = "cranqrel"

    words_Dict = WordsDictionary()
    queries_Dict = QueryDictionary()
    relevances_Dict = RelevancesDictionary()

    words_Dict = read_CranfieldCollection(cranfield_docs, words_Dict)
    queries_Dict = read_CranfieldCollection(cranfield_queries, queries_Dict)
    relevances_Dict = read_CranfieldRelevances(cranfield_qrels, relevances_Dict)
    
    # Vector Space Model
    vsm = VectorSpaceModel(words_Dict, queries_Dict)
    # Calculates the similarity coeficients, sorts them and print them
    # VSM with a limit of coeficients
    vsm.calculate_Coeficients()
    vsm.sort_Coeficients()
    
    #for id_query, ranking in vsm.get_Ranking(10, 10):
    #   print(f"{id_query} --> {ranking}")


    presition_recall = PresitionRecall(relevances_Dict.qrels, vsm.get_Ranking(10, 10))
    presition_recall.calculate_presition()
    presition_recall.calculate_Average()
    for i in presition_recall.get_PresitionRecallData():
        print(i)
    

    
    
    
    #relevances_Dict.printDictionary()
    #graph = Graphing(vsm)
    #graph.printGraph()



if __name__ == '__main__':
    main()
