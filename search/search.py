import re

class searched:
    def __init__(self, list_of_match, text):
        self.list_of_match = list_of_match
        self.text = text
        self.position = 0
        self.matches_found = len(list_of_match)
        print ('Matches found: %d' %self.matches_found)
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
    def prev(self, span):
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

def search_in(text, pattern):
   
    search = re.compile(pattern).finditer(text)
    list_of_match = []
    for match in search:
        list_of_match.append(match)
    return searched(list_of_match, text)