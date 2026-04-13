import sys


def get_word_abbreviations(num_of_words: int) -> None:
    words = [None] * num_of_words

    write, read, join, lower, strip, range_ = sys.stdout.write, sys.stdin.readline, "\n".join, str.lower, str.strip, range

    for i in range_(num_of_words):
        word: str = strip(read())
        word_len: int = len(word)
        
        if word_len <= 10:
            words[i] = word

        else:
            words[i] = f"{lower(word[0])}{len(word) - 2}{lower(word[-1])}"

    write(join(words))


def main() -> None:
    get_word_abbreviations(int(sys.stdin.readline()))
    sys.stdout.write("\n")

    
if __name__ == '__main__':
    main()
