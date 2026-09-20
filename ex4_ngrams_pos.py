# EXP 4: N-Grams and POS Tagging
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.util import ngrams
from collections import Counter

# Download required resources silently
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('treebank', quiet=True)

# 1. N-Grams and Perplexity
text = "Natural language processing allows computers to understand human language."
tokens = nltk.word_tokenize(text.lower())
bigrams = list(ngrams(tokens, 2))

unigram_freq = Counter(tokens)
bigram_freq = Counter(bigrams)

bigram_prob = {bg: bigram_freq[bg] / unigram_freq[bg[0]] for bg in bigram_freq}

print("Bigram Probabilities:")
for bg, prob in bigram_prob.items():
    print(f"{bg}: {prob:.4f}")

def perplexity(sentence, bigram_prob, unigram_freq):
    tokens = nltk.word_tokenize(sentence.lower())
    bigrams = list(ngrams(tokens, 2))
    N = len(tokens)
    perp = 1.0
    for bg in bigrams:
        if bg in bigram_prob:
            perp *= 1 / bigram_prob[bg]
        else:
            perp *= 1 / (unigram_freq[bg[0]] + len(unigram_freq))
    return pow(perp, 1 / N)

test_sentence = "Language processing allows understanding."
perplexity_score = perplexity(test_sentence, bigram_prob, unigram_freq)
print(f"\nPerplexity of the sentence '{test_sentence}': {perplexity_score:.4f}")

# 2. Part-of-Speech (POS) Tagging using HMM
from nltk.corpus import treebank
from nltk.tag import hmm

training_data = treebank.tagged_sents()[:3000]
testing_data = treebank.tagged_sents()[3000:]

trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(training_data)

try:
    accuracy = hmm_tagger.accuracy(testing_data)
except Exception:
    accuracy = hmm_tagger.evaluate(testing_data)

print(f"\nHMM Tagger Accuracy: {accuracy:.4f}")

sentence = "Natural language processing allows computers to understand human language.".split()
tagged_sentence = hmm_tagger.tag(sentence)
print("Tagged Sentence:")
print(tagged_sentence)
