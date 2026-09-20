# EXP 3: Morphology

def extract_prefix_suffix(word):
    prefixes = []
    suffixes = []

    for i in range(1, len(word)):
        prefixes.append(word[:i])

    for i in range(len(word) - 1, 0, -1):
        suffixes.append(word[i:])

    return prefixes, suffixes

word = "prefixsuffix"
prefixes, suffixes = extract_prefix_suffix(word)

print("Prefixes:", prefixes)
print("Suffixes:", suffixes)
