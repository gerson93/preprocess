# Preprocess

# Examples

## Preprocessing


## Searching

Search_in(text, pattern):

Parameter         | Comments
------------------|---------
text(string)      | String to analyze
pattern(string)   | Pattern to search in text
Return(object)    | Searched Class
 
Example:
```python
from search.search import search_in

text = 'Pato patito color de café, si tu no me quieres yo ya se porqué, y no me presumas porque yo ya se que tú eres un pato color de café'
search = search_in(text, 'color')
```
This block will return an object from Searched Class, and will show you trough console the number of matches found
```
Matches found: 2
```
The sintax to go over the matches is:

class Searched (self, list_of_match, text)

Parameter         | Comments
------------------|---------
list_of_match(list) | List with the position of each match in the text
text(string)        | String to analyze

method           | Comments
-----------------|---------
first(self, span)| Go over the first match. Span(int) will show a major área of text where match is
next(self, span) | Go over the next match. Span(int) will show a major área of text where match is
last(self, span) | Go over the last match. Span(int) will show a major área of text where match is
prev(self, span) | Go over the previous match. Span(int) will show a major área of text where match is

Now, you can go over the matches by:

```python
search.first(10)
```
And you will see something like this
```
1/2
to patito color de cafe s
Beginning
```
