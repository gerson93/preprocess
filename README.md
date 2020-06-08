# UNDER CONSTRUCTION
# Preprocess

# Examples

## Preprocessing
class preprocessing(self, text)

Parameter         | Comments
------------------|---------
text(string)      | String to analyze

```python
from preprocess.preprocess_basic import preprocessing

text = 'Pato patito color de café, si tu no me quieres yo ya se porqué, y no me presumas porque yo ya se que tú eres un pato color de café'

prep = preprocessing(text)
```

method                            | Comments
----------------------------------|---------
text_(self, alphanumeric = True, punctuation = True, lower = True) | It will delete punctuation, alphanumeric words and it will put lower case, if the parameters is true. By default, every one is true. 
common_words(self)                 | return a list with the number of each words in the text
count_words(self)                  | return a int with the number of total words

**note of authors: i need to change the name of "text_"

so, then you can preprocess the your text
```
print(prep.text_())
```
and you'll get

```
pato patito color de café  si tu no me quieres yo ya se porqué  y no me presumas porque yo ya se que tú eres un pato color de café
```

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
