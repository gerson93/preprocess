""" from preprocess.search import search_by_words

text = 'Pato patito color de café, si tu no me quieres yo ya se porqué, y no me presumas porque yo ya se que tú eres un pato color de café'

s = search_by_words(text, 'color') """

from preprocess.preprocess_basic import preprocessing

text = 'Pato patito color de café, si tu no me quieres yo ya se porqué, y no me presumas porque yo ya se que tú eres un pato color de café'

prep = preprocessing(text)

print(prep.text_())