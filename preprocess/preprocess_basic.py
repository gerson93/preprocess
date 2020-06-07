import re
import string

class preprocess:
    def __init__(self, text):
        self.text = text
    def preprocess_text (self):
        alphanumeric = lambda x: re.sub(r"""\w*\d\w*""", ' ', x)
        punc_lower = lambda x: re.sub('[%s]' % re.escape(string.punctuation), ' ', x.lower())

        self.text = alphanumeric(self.text)
        self.text = punc_lower(self.text)
        return self.text


def hi():
    print('hi')