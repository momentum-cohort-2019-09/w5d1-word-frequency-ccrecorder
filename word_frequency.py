import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def clean_text(text):
    text = text.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    text_to_keep = ""
    for char in text:
        if char in all_letters:
            text_to_keep += char
    return text_to_keep

def clean_texts(text):
    text = text.strip(string.punctuation)
    text = text.lower()
    if text[-2:] == "'s":
        text = text[:-2]
    return text

def get_longest_word(words):
    return sorted(words, key=len, reverse=True)[0]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    with open(file) as text_file:
        contents = text_file.read()

    words = contents.split()

    clean_words = []

    for word in words:
        clean_words.append(clean_texts(word))

    go_words = [word for word in clean_words if word not in STOP_WORDS]

    word_count = {}

    for go_word in go_words:
        word_count.update({go_word: go_words.count(go_word)})

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    longest_word_len = len(get_longest_word(sorted_word_count))

    for word, sorted_word in sorted_word_count[:10]:
        print(word.rjust(longest_word_len), "|", str(sorted_word).ljust(3), "*" * sorted_word)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
