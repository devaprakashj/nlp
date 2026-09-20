# EXP 2: Word Generation
import random

def generate_sentence(word_count, transition_probs):
    sentence = ""
    for _ in range(word_count):
        word_length = random.randint(1, 10)
        word = generate_word(word_length, transition_probs)
        sentence += word + " "
    return sentence.strip()

def generate_word(word_length, transition_probs):
    word = ""
    current_state = "@"
    for _ in range(word_length):
        if current_state not in transition_probs:
            break
        next_state = random.choices(
            list(transition_probs[current_state].keys()),
            weights=list(transition_probs[current_state].values())
        )[0]
        if next_state == "$":
            break
        word += next_state
        current_state = next_state
    return word

word_transition_probs = {
    "@": {"The": 0.3, "A": 0.5, "$": 0.2},
    "The": {"cat": 0.7, "dog": 0.3, "$": 0},
    "A": {"quick": 0.6, "lazy": 0.4, "$": 0},
    "quick": {"brown": 0.8, "black": 0.2, "$": 0},
    "lazy": {"brown": 1.0, "$": 0},
    "cat": {"jumped": 1.0, "$": 0},
    "dog": {"ran": 1.0, "$": 0},
    "brown": {"fox": 1.0, "$": 0},
    "black": {"dog": 1.0, "$": 0},
    "fox": {"$": 1.0},
    "jumped": {"over": 1.0, "$": 0},
    "ran": {"through": 1.0, "$": 0},
    "over": {"the": 1.0, "$": 0},
    "through": {"the": 1.0, "$": 0},
    "the": {"fence": 1.0, "$": 0},
    "fence": {"$": 1.0}
}

new_sentence = generate_sentence(8, word_transition_probs)
print("Generated Sentence:", new_sentence)
