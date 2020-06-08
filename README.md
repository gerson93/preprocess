# UNDER CONSTRUCTION
# Preprocess

# Examples

## Preprocessing


## Searching

class search_by_words(self, text, words)

Parameter         | Comments
------------------|---------
text(string)      | String to analyze
pattern(string)   | Pattern to search in text

 
Example:
```python
from preprocess.search import search_by_words

text = 'Pato patito color de café, si tu no me quieres yo ya se porqué, y no me presumas porque yo ya se que tú eres un pato color de café'
s = search_by_words(text, 'color')
```

```
Matches found: 2
```

method                         | Comments
-------------------------------|---------
first(self, span)              | Go over the first match. Span(int) will show a major área of text where match is
next(self, span)               | Go over the next match. Span(int) will show a major área of text where match is
last(self, span)               | Go over the last match. Span(int) will show a major área of text where match is
prev(self, span)               | Go over the previous match. Span(int) will show a major área of text where match is
replace(self, words_to_replace)| Replace words in the text with words_to_replace(string)

Now, you can go over the matches by:

```python
s.first(10)
```
And you will see something like this
```
1/2
to patito color de cafe s
Beginning
```
And then you can replace the content with another:
```python
s.replace('none')
```
And you will get something like this:
```
'pato patito color de cafe si tu no me quieres yo ya se porqué, y no me presumas porque yo ya se que tú eres un none color de café'
```
