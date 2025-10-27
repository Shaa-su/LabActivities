# para pang lowercase

def clean_text(text):
    # pang lowercase
    text = text.lower()

    
    text = text.strip()

   
    for char in [".", ",", "!", "?"]:
        text = text.replace(char, "")

    return text
