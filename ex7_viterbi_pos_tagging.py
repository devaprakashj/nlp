# EXP 7: POS Tagging using Viterbi Algorithm (HMM)
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.tag import hmm
from nltk.corpus import treebank

# Download necessary datasets
nltk.download('treebank', quiet=True)
nltk.download('universal_tagset', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Load the Penn Treebank corpus with universal tagset
train_data = treebank.tagged_sents(tagset='universal')

# Train an HMM POS tagger
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(train_data)

def pos_tag_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = hmm_tagger.tag(tokens)
    return pos_tags

sentence = "The quick brown fox jumps over the lazy dog."
pos_tags = pos_tag_sentence(sentence)
print(pos_tags)
