#same dito ginamit yung sa cleaner.py para walang caps using import
from text_analyzer.cleaner import clean_text 
def word_frequency(text):
    cleaned = clean_text(text)
    words = cleaned.split()
    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq
