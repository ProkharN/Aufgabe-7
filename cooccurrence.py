"""
Code-Gerüst zur Implementierung einer Kookkurrenzmatrix
CLT-22
"""

# import-Statements hier


class Cooccurrence:
    def __init__(self, skip_stops=False):
        """Kookkurrenzobjekt zur Repräsentation der Matrix

        :param skip_stops: ob Stopwörtern entfernt werden
            sollen (True) oder nicht (False)
        """
        self.w2i = dict()  # Mapping zwischen Wörtern (str) und Indices (int)
        self.cooccurrence_matrix = None  # Matrix, vorzugsweise als numpy array
        self.skip_stopwords = skip_stops

    def word_similarity(self, word_1, word_2):
        """ Gibt die Ähnlichkeit zwischen zwei Wörtern zurück

        :param word_1: str
        :param word_2: str
        :return: float, Ähnlichkeit
        """

    def build_matrix(self, corpus, window_size=10):
        """ Baut die Kookkurrenzmatrix (self.cooccurrence_matrix) auf

        :param corpus: list, Korpus als Wortliste
        :param window_size: int, Größe des Fensters, das als Kontext dient
        """

    def find_most_common_words(self, n):
        """ Gibt die n häufigsten Wörter des Korpus zurück

        :param n: int, wieviele Wörter gesucht sind
        :return: nach Häufigkeiten sortierte Liste mit Wörtern
        """


def cosine_similarity(vector_a, vector_b):
    """ Berechnung der Kosinusähnlichkeit zwischen zwei Vektoren

    :param vector_a: Kontext-Vektor des einen Wortes
    :param vector_b: Kontext-Vektor des anderen Wortes
    :return: float, Ähnlichkeit
    """


if __name__ == '__main__':
    # Mit allen Tokens:
    brown_cooccurrences = Cooccurrence()
    brown_cooccurrences.build_matrix(brown.words())

    print('10 most common words:')
    print(brown_cooccurrences.find_most_common_words(10))

    # Ohne Stopwörter:
    brown_cooccurrences_without_stops = Cooccurrence(skip_stops=True)
    brown_cooccurrences_without_stops.build_matrix(brown.words(),
                                                   window_size=10)

    print('10 most common words:')
    print(brown_cooccurrences_without_stops.find_most_common_words(10))

    # Similarity between 'good' and 'evil':
    similarity = brown_cooccurrences.word_similarity('good', 'evil')
    print(f'The similarity between "good" and "evil" is {similarity}.')
