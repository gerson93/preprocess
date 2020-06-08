import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class search_by_words:
    def __init__(self, text, words):
        self.text = text
        self.words = words
        self.search()
        print ('Matches found: %d' %self.matches_found)

    def search(self):
        search = re.compile(self.words).finditer(self.text)
        list_of_match = []
        for match in search:
            list_of_match.append(match)
        self.list_of_match = list_of_match
        self.position = 0
        self.matches_found = len(self.list_of_match)

    def next(self, span = 0):
        list_of_match = self.list_of_match
        text = self.text
        self.position += 1
        position = self.position    
        if (position < len(list_of_match)):
            print('%d' %(position + 1) + '/' + '%d' %(self.matches_found))  
            span_left = span
            span_right = span
            if (list_of_match[position].span()[0] - span < 0):
                span_left = list_of_match[position].span()[0]
            if (list_of_match[position].span()[1] + span > len(text)):
                span_right = len(text) - list_of_match[position].span()[1]
            print(text[list_of_match[position].span()[0] - span_left :list_of_match[position].span()[1] + span_right])  
        else:
            print ('End')
    def prev(self, span = 0):
        list_of_match = self.list_of_match
        text = self.text
        self.position -= 1
        position = self.position 
        if (position >= 0):
            print('%d' %(position + 1) + '/' + '%d' %(self.matches_found))
            span_left = span
            span_right = span
            if (list_of_match[position].span()[0] - span < 0):
                span_left = list_of_match[position].span()[0]
            if (list_of_match[position].span()[1] + span > len(text)):
                span_right = len(text) - list_of_match[position].span()[1]
            print(text[list_of_match[position].span()[0] - span_left:list_of_match[position].span()[1] + span_right])
        else:
            print ('Beginning')
            self.position = -1
    def first (self, span = 0):
        list_of_match = self.list_of_match
        text = self.text
        self.position = 0
        position = self.position
        span_left = span
        span_right = span
        print('%d' %(position + 1) + '/' + '%d' %(self.matches_found))
        if (list_of_match[position].span()[0] - span < 0):
            span_left = list_of_match[position].span()[0]
        if (list_of_match[position].span()[1] + span > len(text)):
            span_right = len(text) - list_of_match[position].span()[1]
        print(text[list_of_match[position].span()[0] - span_left :list_of_match[position].span()[1] + span_right])  
        print ('Beginning')
    def last (self, span = 0):
        list_of_match = self.list_of_match
        text = self.text
        self.position = self.matches_found - 1
        position = self.position
        span_left = span
        span_right = span
        print('%d' %(position + 1) + '/' + '%d' %(self.matches_found))
        if (list_of_match[position].span()[0] - span < 0):
            span_left = list_of_match[position].span()[0]
        if (list_of_match[position].span()[1] + span > len(text)):
            span_right = len(text) - list_of_match[position].span()[1]
        print(text[list_of_match[position].span()[0] - span_left :list_of_match[position].span()[1] + span_right])  
        print ('Beginning')
    def replace(self, words_to_replace):
        position = self.position
        list_of_match = self.list_of_match
        print('%d' %(position + 1) + '/' + '%d' %(self.matches_found))
        text = self.text
        self.text = text[0:list_of_match[position].span()[0]] + words_to_replace + text[list_of_match[position].span()[1]:]
        self.search()
        return self.text

class search_related:
    def __init__ (self, text, content, language, limit = 0.7):
        self.text = text
        self.content = content
        self.stopwords = stopwords.words(language)
        self.stemmer = SnowballStemmer(language)
        self.sent = nltk.sent_tokenize(self.text)
        self.limit = limit
        print(self.content)
        self.GenerateAnswer()
        
    def stemTokens (self, tokens):
        return [self.stemmer.stem(token) for token in tokens]

    def stemmm (self, text):
        return self.stemTokens(nltk.word_tokenize(text))

    def GenerateAnswer (self):
        self.sent.append(self.content.lower())
        TfidfVector = TfidfVectorizer(tokenizer = self.stemmm)
        tfidf_vectorizer_vectors = TfidfVector.fit_transform(self.sent)
        cos_simil = cosine_similarity(tfidf_vectorizer_vectors[-1], tfidf_vectorizer_vectors)
        id_sent=cos_simil.argsort()[0][-2]
        flat = cos_simil.flatten()
        flat.sort()
        request_tfidf = flat[-2]
        if (request_tfidf < self.limit):
            return print ('ups! sorry, can you be more clear?')
        return print(self.sent[id_sent])