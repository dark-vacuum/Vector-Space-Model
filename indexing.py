from Dictionaries import WordsDictionary, QueryDictionary
from functools import reduce

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


"""
Funcion que lee un archivo, y regresa todas las
palabras que hay en el documento.
"""
def read_CranfieldDocs(file: str, words_Dict: WordsDictionary) -> WordsDictionary:
    """
    Receives a word which could be a number or a word or a word
    with symbols and if the string has any af the specified
    symbols they will be removed.

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
    words_Dict : WordsDictionary
        The dictionary where the words will be stored.

    Returns
    -------

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
                    words_Dict.total_documents += 1
                avoid_line = True if arr_line[0] in indicators_toAvoid else False
                continue
            if avoid_line:
                continue
            arr_line = list(filter(lambda x : x != "", map(lambda x : replace(x), arr_line)))
            for word in arr_line:
                words_Dict.createIfNotExists(word, current_doc)
    return words_Dict

def read_CranfieldQuerys(file: str, querys_Dict: QueryDictionary) -> QueryDictionary:
    indicators = {".I", ".W"}

    # Lectura del archivo linea por linea.
    with open(file) as document:
        current_query = 0
        for line in document:
            arr_line = line.split()
            if arr_line[0] in indicators:
                if arr_line[0] == ".I":
                    current_query = int(arr_line[1])
                    querys_Dict.total_querys += 1
                    querys_Dict.insertQuery(current_query)
                continue
            arr_line = list(filter(lambda x : x != "", map(lambda x : replace(x), arr_line)))
            for word in arr_line:
                querys_Dict.insertWord(current_query, word)
    return querys_Dict



def main():
    # Colocar aqui los documentos que se quieran leer para crear el indice
    cranfield_docs = "cran.all.1400"
    cranfield_querys = "cran.qry"
    words_Dict = WordsDictionary()
    querys_Dict = QueryDictionary()
    words_Dict = read_CranfieldDocs(cranfield_docs, words_Dict)
    words_Dict.printDictionary()
    querys_Dict = read_CranfieldQuerys(cranfield_querys, querys_Dict)
    querys_Dict.printDictionary()



if __name__ == '__main__':
    main()
