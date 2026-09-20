import os
import subprocess
import sys

EXPERIMENTS = [
    ("1", "Word Analysis", "ex1_word_analysis.py"),
    ("2", "Word Generation", "ex2_word_generation.py"),
    ("3", "Morphology (Prefixes & Suffixes)", "ex3_morphology.py"),
    ("4", "N-Grams and POS Tagging", "ex4_ngrams_pos.py"),
    ("5", "Smoothing Techniques (Laplace, Additive, Good-Turing, etc.)", "ex5_smoothing_techniques.py"),
    ("6", "HMM POS Tagging (Treebank)", "ex6_hmm_pos_tagging.py"),
    ("7", "Viterbi POS Tagging", "ex7_viterbi_pos_tagging.py"),
    ("8", "Perceptron POS Tagging", "ex8_pos_tagger.py"),
    ("9", "Chunking (Noun Phrase Extraction)", "ex9_chunking.py"),
    ("10", "Automatic Chunking", "ex10_automatic_chunking.py"),
]

def run_experiment(script_name, title):
    print("\n" + "=" * 60)
    print(f" RUNNING: {title} ({script_name})")
    print("=" * 60)
    subprocess.run([sys.executable, script_name])
    print("=" * 60)
    input("\nPress Enter to continue...")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("               NLP LAB EXPERIMENTS RUNNER               ")
        print("=" * 60)
        for num, title, script in EXPERIMENTS:
            print(f" [{num.rjust(2)}] {title}")
        print(" [ A] Run All Experiments sequentially")
        print(" [ Q] Exit")
        print("=" * 60)
        
        choice = input("Enter experiment number (1-10 / A / Q): ").strip().upper()
        
        if choice == 'Q':
            print("Exiting NLP Runner. All the best for your lab!")
            break
        elif choice == 'A':
            for _, title, script in EXPERIMENTS:
                run_experiment(script, title)
        else:
            match = next((item for item in EXPERIMENTS if item[0] == choice), None)
            if match:
                run_experiment(match[2], match[1])
            else:
                input("Invalid option! Press Enter to try again...")

if __name__ == "__main__":
    main()
