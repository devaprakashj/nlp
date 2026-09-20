# EXP 8: POS Tagging using NLTK Perceptron Tagger
import nltk

# Download required resources
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

text = nltk.word_tokenize("and now for everything completely same")
result = nltk.pos_tag(text)
print(result)
