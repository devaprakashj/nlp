# EXP 1: Word Analysis

def word_analysis(text):
    text = text.lower()
    words = text.split()
    word_freq = {}
    
    for word in words:
        word = word.strip('.,?!-')
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    total_words = sum(word_freq.values())
    word_distribution = {word: freq / total_words for word, freq in word_freq.items()}
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    print("Word\t\tFrequency\tDistribution")
    print("---------------------------------------")
    for word, freq in sorted_word_freq:
        print(f"{word.ljust(15)}{freq}\t\t{word_distribution[word]:.2%}")

text = "This is a sample text for word analysis. Word analysis involves analyzing the frequency of each word in a given text."
word_analysis(text)
