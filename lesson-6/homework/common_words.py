import os
import string
from collections import Counter

def create_sample_file():
    text = input("Enter a paragraph to create sample.txt: ")
    with open("sample.txt", "w") as file:
        file.write(text)

def read_file():
    if not os.path.exists("sample.txt"):
        print("sample.txt not found. Creating a new one.")
        create_sample_file()
    
    with open("sample.txt", "r", encoding="utf-8") as file:
        return file.read().lower()

def count_word_frequency(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return Counter(words)

def save_report(total_words, common_words):
    with open("word_count_report.txt", "w", encoding="utf-8") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top Words:\n")
        for word, count in common_words:
            file.write(f"{word} - {count}\n")

def main():
    text = read_file()
    word_counts = count_word_frequency(text)
    total_words = sum(word_counts.values())
    
    try:
        top_n = int(input("Enter the number of top common words to display: "))
    except ValueError:
        print("Invalid input, defaulting to top 5.")
        top_n = 5
    
    common_words = word_counts.most_common(top_n)
    
    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in common_words:
        print(f"{word} - {count} times")
    
    save_report(total_words, common_words)
    print("Word count report saved to word_count_report.txt")

if __name__ == "__main__":
    main()