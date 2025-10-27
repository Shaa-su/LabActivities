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
