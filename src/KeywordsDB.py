"""
This class builds KeyWordsDB and provides function to query it
"""


class KeywordsDB:
    def __init__(self):
        self.db = {}

    def build(self, products):
        for product in products:
            keywords = product.get_title().split(" ")

            for word in keywords:
                if word in self.db:
                    self.db[word] += 1
                else:
                    self.db[word] = 0

    def find_keyword_frequency(self, word):
        if word in self.db:
            return self.db[word]
        else:
            return 0

    def find_all_frequencies(self, request_dict):
        all_frequencies = []
        all_words = request_dict["keywords"]
        final_output = dict()

        for word in all_words:
            word_frequency = dict()
            word_frequency[word] = self.find_keyword_frequency(word)
            all_frequencies.append(word_frequency)

        final_output["keywordFrequencies"] = all_frequencies
        return final_output
