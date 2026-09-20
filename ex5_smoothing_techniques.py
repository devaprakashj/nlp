# EXP 5: Smoothing Techniques for Language Models
import nltk
from collections import Counter
from nltk.lm.models import KneserNeyInterpolated, WittenBellInterpolated
from nltk.lm.preprocessing import padded_everygram_pipeline

# Sample text
text = "Natural language processing allows computers to understand human language."
tokens = nltk.word_tokenize(text.lower())
bigrams = list(nltk.bigrams(tokens))

# Count frequencies
unigram_freq = Counter(tokens)
bigram_freq = Counter(bigrams)
V = len(unigram_freq)
example_bigram = ('language', 'processing')

# 1. Laplace Smoothing
def laplace_smoothed_prob(bigram, bigram_freq, unigram_freq, V):
    return (bigram_freq[bigram] + 1) / (unigram_freq[bigram[0]] + V)

prob_laplace = laplace_smoothed_prob(example_bigram, bigram_freq, unigram_freq, V)
print(f"Laplace Smoothed Probability of {example_bigram}: {prob_laplace:.4f}")

# 2. Additive Smoothing (alpha = 0.5)
def additive_smoothed_prob(bigram, bigram_freq, unigram_freq, V, alpha):
    return (bigram_freq[bigram] + alpha) / (unigram_freq[bigram[0]] + alpha * V)

alpha = 0.5
prob_additive = additive_smoothed_prob(example_bigram, bigram_freq, unigram_freq, V, alpha)
print(f"Additive Smoothed Probability of {example_bigram} with alpha={alpha}: {prob_additive:.4f}")

# 3. Good-Turing Smoothing
def good_turing_prob(bigram, bigram_freq, unigram_freq):
    freq_of_freqs = Counter(bigram_freq.values())
    c = bigram_freq[bigram]
    c_star = (c + 1) * (freq_of_freqs[c + 1] / freq_of_freqs[c]) if freq_of_freqs[c] != 0 else 0
    N = sum(bigram_freq.values())
    return c_star / N

prob_gt = good_turing_prob(example_bigram, bigram_freq, unigram_freq)
print(f"Good-Turing Probability of {example_bigram}: {prob_gt:.4f}")

# 4. Kneser-Ney Smoothing
train_data = [['natural', 'language', 'processing', 'allows', 'computers', 'to', 'understand', 'human', 'language']]
n = 2
train_data_kn, padded_sents_kn = padded_everygram_pipeline(n, train_data)
kn_model = KneserNeyInterpolated(n)
kn_model.fit(train_data_kn, padded_sents_kn)
prob_kn = kn_model.score('processing', ['language'])
print(f"Kneser-Ney Smoothed Probability: {prob_kn:.4f}")

# 5. Witten-Bell Interpolation
train_data = [['natural', 'language', 'processing', 'allows', 'computers', 'to', 'understand', 'human', 'language']]
train_data_wb, padded_sents_wb = padded_everygram_pipeline(n, train_data)
wb_model = WittenBellInterpolated(n)
wb_model.fit(train_data_wb, padded_sents_wb)
prob_wb = wb_model.score('processing', ['language'])
print(f"Witten-Bell Interpolated Probability: {prob_wb:.4f}")
