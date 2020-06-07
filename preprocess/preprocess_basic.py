import re
import string

from nltk.tokenize import word_tokenize
from collections import Counter


class preprocessing:
    def __init__(self, text):
        assert type(text) == type(''), 'Text must be a string'
        self.text = text
        pass
    def text_ (self, alphanumeric = True, punctuation = True, lower = True):
        remove_alphanumeric = lambda x: re.sub(r"""\w*\d\w*""", ' ', x)
        remove_punctuation = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x)
        lower_case = lambda x: x.lower()
        text = self.text
        if (alphanumeric):
            text = remove_alphanumeric(text)
        if (punctuation):
            text = remove_punctuation(text)
        if (lower):
            text = lower_case(text)
        return text

    def common_words (self):
        text = self.text
        word_list = word_tokenize(text)
        word_counts = Counter(word_list)
        word_counts = list(zip(word_counts.values(), word_counts.keys()))
        word_counts = sorted(word_counts, reverse=True)
        return word_counts

    def count_words (self):
        text = self.text
        word_list = word_tokenize(text)
        return len(word_list)


def text_ (text, alphanumeric = True, punctuation = True, lower = True):
    assert type(text) == type(''), 'Text must be a string'
    remove_alphanumeric = lambda x: re.sub(r"""\w*\d\w*""", ' ', x)
    remove_punctuation = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x)
    lower_case = lambda x: x.lower()

    if (alphanumeric):
        text = remove_alphanumeric(text)
    if (punctuation):
        text = remove_punctuation(text)
    if (lower):
        text = lower_case(text)
    return text

def common_words (text):
    assert type(text) == type(''), 'Text must be a string'
    word_list = word_tokenize(text)
    word_counts = Counter(word_list)
    word_counts = list(zip(word_counts.values(), word_counts.keys()))
    word_counts = sorted(word_counts, reverse=True)
    return word_counts

def count_words (text):
    assert type(text) == type(''), 'Text must be a string'
    word_list = word_tokenize(text)
    return len(word_list)

def search(text, textToFind):
    assert type(text) == type(''), 'Text must be a string'
    
#ok