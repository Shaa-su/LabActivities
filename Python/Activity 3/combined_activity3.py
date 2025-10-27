# ++++ cleaner ++++
# para pang lowercase

def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove leading and trailing spaces
    text = text.strip()

    # Remove punctuation marks
    for char in [".", ",", "!", "?"]:
        text = text.replace(char, "")

    return text

# ++++ analyzer ++++
# from text_analyzer.cleaner import clean_text #ginamit dito yung sa cleaner.py para walang caps using import

def analyze_text(text):

    cleaned = clean_text(text)

    
    words = cleaned.split()

    # pang bilang
    total_words = len(words)

    # pang bilang ng unque words
    unique_words = len(set(words))

    # get yung pinaka mahaba na word
    longest_word = max(words, key=len) if words else ""

    # Return results as a dictionary
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "longest_word": longest_word
    }

# ++++ stats ++++
# from text_analyzer.cleaner import clean_text #ginamit dito yung sa cleaner.py para walang caps using import

def word_frequency(text):
    cleaned = clean_text(text)
    words = cleaned.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

# ++++ main ++++
# dito dapata mag run whcih is yung main

# from text_analyzer.analyzer import analyze_text
# from text_analyzer.stats import word_frequency

# pang input lang
sentence = input("Enter a sentence: ")

# dito ginagamit yung function ng stats saka analyzer
result = analyze_text(sentence)
freq = word_frequency(sentence)

# Display with borders
border = "+" * 30  # Simple border using '+'
print(f"\n{border}")
print("Analysis Results:")
print(f"Total Words: {result['total_words']}")
print(f"Unique Words: {result['unique_words']}")
print(f"Longest Word: {result['longest_word']}")
print(f"{border}")

print(f"{border}")
print("\nWord Frequency:")
for word, count in freq.items():
    print(f"{word}: {count}")
print(f"{border}")