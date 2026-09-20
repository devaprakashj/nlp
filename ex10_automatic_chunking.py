# EXP 10: Automatic Chunking
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.chunk import RegexpParser

# Download necessary datasets
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog"

# Tokenize and POS Tag
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)
print("POS Tagged Tokens:", tagged_tokens)

# Chunk grammar for noun phrases
chunk_grammar = r"""
    NP: {<DT>?<JJ>*<NN>}
"""

chunk_parser = RegexpParser(chunk_grammar)
chunked_sentence = chunk_parser.parse(tagged_tokens)
print("Chunked Sentence:", chunked_sentence)
