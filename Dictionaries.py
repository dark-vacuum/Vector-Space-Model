from math import log10
class QueryDictionary:
    """
    A class used to represent a dictionary of querys.

    ...

    Attributes
    ----------
    querys : {int : {str : int}}
        A dictionary of querys, where the key is the number of the
        query and the values are dictionaries containing the words
        of the query and its incidences.
    total_querys : int
        The total numbers of querys.

    Methods
    -------
    insertQuery(query_num: int)
        Inserts the query in the dicctionary if the query doesn't
        exists.
    insertWord(query_num: int, word: str)
        Inserts a word or adds an incidence.
    """

    def __init__(self):
        self.querys = {}
        self.total_querys = 0

    def insertQuery(self, query_num:  int):
        """
        Checks if the query exist in the dictionary, if not exists is
        created.

        Parameters
        ----------
        query_num : int
            The number of the query to check.
        """

        already_exists = query_num in self.querys
        if not already_exists:
            self.querys[query_num] = {}
            self.total_querys += 1

    def insertWord(self, query_num: int, word: str):
        """
        Checks if the word exist in the query, if not exists is
        created, else the incidence increments in 1.

        Parameters
        ----------
        query_num : int
            The number of the query to check.
        """

        already_exists = word in self.querys[query_num]
        if already_exists:
            self.querys[query_num][word] += 1
        else:
            self.querys[query_num][word] = 1


    def printDictionary(self):
        for i in self.querys:
            print(f"{i}--{self.querys[i]}")


class Word:
    """
    A class used to represent a word.

    ...

    Attributes
    ----------
    docs : {int : int}
        A dictionary of documents, where the key is the number of the
        document and the value is the incidences of the word in that
        document.
    idf : float
        lambda value of the word correspondig to log(N/n), where N is
        the total of documents and n is the documents where the word
        appear, it has one argument N.
    length_docs : int
        The total number of documents where the term appears.

    Methods
    -------
    insertDoc(doc_num: int)
        Inserts the document in the dicctionary if the document doesn't
        exists.
    """

    def __init__(self):
        self.docs = {}
        self.idf = lambda N : log10(N/self.length_docs)
        self.length_docs = 0


    def insertDoc(self, doc_num: int):
        """
        Checks if the document exist in the dictionary, if not exists
        is created, else the incidence increments in 1.

        Parameters
        ----------
        doc_num : int
            The number of the document to check.
        """

        already_exists = doc_num in self.docs

        if already_exists:
            self.docs[doc_num] += 1
        else:
            self.docs[doc_num] = 1
            self.length_docs += 1



class WordsDictionary:
    """
    A class used to represent a dictionary of words.

    ...

    Attributes
    ----------
    words : {str : Word}
        A dictionary of words, where the key is a term and the values
        are objects of the class Word.
    total_documents : int
        The total numbers of querys.
    total_words : int
        The total numbers of words.

    Methods
    -------
    createIfNotExists(word: str, doc_num: int)
        Inserts the word in the dicctionary if the word doesn't
        exists and inserts the document where it appears.
    """

    def __init__(self):
        self.words = {}
        self.total_documents = 0
        self.total_words = 0


    def createIfNotExists(self, word: str, doc_num: int):
        """
        Checks if the word exist in the dictionary, if not exists
        is created and the document is inserted.

        Parameters
        ----------
        doc_num : int
            The number of the document to check.
        """

        already_exists = word in self.words

        if not already_exists:
            self.words[word] = Word()
            self.total_words += 1
        self.words[word].insertDoc(doc_num)

    def printDictionary(self):
            for i in self.words:
                print(f"{i}--{self.words[i].docs}")
