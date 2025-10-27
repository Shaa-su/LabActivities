#ginamit dito yung sa cleaner.py para walang caps using import
from text_analyzer.cleaner import clean_text #ginamit dito yung sa cleaner.py para walang caps using import

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
