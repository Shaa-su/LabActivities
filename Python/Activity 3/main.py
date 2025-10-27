# dito dapata mag run whcih is yung main 

from text_analyzer.analyzer import analyze_text
from text_analyzer.stats import word_frequency

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