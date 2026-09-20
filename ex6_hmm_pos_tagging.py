# EXP 6: POS Tagging using Hidden Markov Model (HMM)
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.corpus import treebank
from nltk.tag.hmm import HiddenMarkovModelTrainer

# Download necessary datasets
nltk.download('treebank', quiet=True)
nltk.download('universal_tagset', quiet=True)

# Load Treebank corpus with universal tagset
train_data = treebank.tagged_sents(tagset='universal')[:3000]
test_data = treebank.tagged_sents(tagset='universal')[3000:]

# Train HMM Tagger
trainer = HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(train_data)

# Evaluate on test data
try:
    accuracy = hmm_tagger.accuracy(test_data)
except Exception:
    accuracy = hmm_tagger.evaluate(test_data)

print(f"HMM Tagger Accuracy: {accuracy:.4f}")

# Tagging a sample sentence
sentence = "Natural language processing allows computers to understand human language.".split()
tagged_sentence = hmm_tagger.tag(sentence)

print("Tagged Sentence:")
print(tagged_sentence)
