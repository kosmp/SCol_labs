import re


def get_amount_of_declarative_sentences(sentences: list) -> int:
    amount = 0
    for sentence in sentences:
        if sentence[-1] == '.' or sentence[-1] == '"' or (
                len(sentence) >= 2 and sentence[-1] == ')' and sentence[-2] == '.'):
            amount += 1
    return amount


def text_input(text_i: str) -> str:
    choice = str(input("Do you want to load text from file: Y or N: "))
    t = ''
    if choice == "Y":
        try:
            while True:
                path_to_file = str(input("Enter path to file you want to load text from"
                                         "(or nothing if you want to use default): "))
                with open(path_to_file, 'r') as file:
                    if not file.read():
                        print("File is empty. Try again after filling this file or enter nothing as a path.")
                        continue
                    file.seek(0)
                    t = ''
                    for line in file:
                        t += line
                    break
        except FileNotFoundError:
            print("Error with file opening or empty input. Default text will be used.")
            return text_i

        for i in t:
            if not re.match(r'(\s|\w|\.|\"|\'|\:|\-|\?|\!|\.|\,|\n|\(|\)|\;)', i):
                print("Incorrect symbols in file.")
                return text_i
        return t
    else:
        return text_i


def get_sentences_list_from_text(text: str) -> list[str]:
    sentences = re.split(r'(?<!Ph\.\sD)(?<!Ph(?=\.\sD\.))(?<!Ph\.D)(?<!Ph(?=\.D))'
                         r'(?<!i\.\se)(?<!i(?=\.\se\.))(?<!i\.e)(?<!i(?=\.e))'
                         r'(?<!e\.\sg)(?<!e(?=\.\sg\.))(?<!e\.g)(?<!e(?=\.g))'
                         r'(?<![A-Z]\.\s[A-Z])(?<![A-Z](?=\.\s[A-Z]\.))(?<![A-Z]\.[A-Z])(?<![A-Z](?=\.[A-Z]))'
                         r'(?<!Mr)(?<!Mrs)(?<!Dr)(?<!Lt)(?<!Rep)(?<!Mr)(?<!etc(?=\.[^\n]))'
                         r'(?<![ap]\.\sm)(?<![ap](?=\.\sm\.))(?<![ap]\.m)(?<![ap](?=\.m))'
                         r'((?<=[A-Za-z0-9])\.|!|\?|\?!|(?<=[A-Za-z0-9])\.\.\.|(?<=\.)\"|(?<=\?)\"|(?<=!)\"|'
                         r'(?<=[A-Za-z0-9])\.\)|!\)|\?|\?!\)|(?<=[A-Za-z0-9])\.\.\.\))'
                         r'(\s|\n|$)', text)

    i = 0
    while i < len(sentences):
        if not len(sentences[i]) == 1:
            sentences[i] = re.sub(r'\n', '', sentences[i])
        i += 1

    i = 0
    while i < len(sentences):
        el = sentences[i]
        if i + 3 < len(sentences) and sentences[i + 1] != '"' and el != '"' and el.count('"') == 1 and el != '' and \
                el[-1] != '.' and el[-1] != '!' and el[-1] != '?':
            sentences[i] = sentences[i] + sentences[i + 1] + sentences[i + 2] + sentences[i + 3]
            el = sentences[i]
            if i + 4 < len(sentences):
                sentences = sentences[:i + 1] + sentences[i + 4:]
            else:
                sentences = sentences[:i + 1]
            continue
        if el == '.' or el == '!' or el == '?' or el == '?!' or el == '...' or el == '"' or \
                el == '.)' or el == '!)' or el == '?)' or el == '?!)' or el == '...)':
            sentences[i - 1] = sentences[i - 1] + el
        if el == '' or el == '.' or el == '...' or el == '!' or el == '?' or el == '?!' or el == ' ' or \
                el == '\n' or el == '"' or el == '.)' or el == '!)' or el == '?)' or el == '?!)' or el == '...)':
            sentences.remove(el)
            i -= 1
        i += 1

    i = 0
    while i < len(sentences):
        if (i == 0 or (i > 0 and sentences[i - 1][-1] == '.' or sentences[i - 1][-1] == '!' or
                       sentences[i - 1][-1] == '?')) and sentences[i].count('"') == 2 and sentences[i][0] == '"' and\
                sentences[i][-1] == '"' and i + 1 < len(sentences):
            sentences[i] = sentences[i] + ' ' + sentences[i + 1]
            sentences = sentences[:i + 1] + sentences[i + 2:]
        i += 1

    print("Final list of sentences: " + str(sentences))
    return sentences


def get_words_and_num_of_chars(sentences: list[str]) -> tuple[list[str], int]:
    words_in_text = []
    total_num_of_chars_in_words = 0
    for sentence in sentences:
        words_in_sentence = re.split(r'(\s|\n|\"|\(|(?<=[A-Z])\.|(?<=i)\.|(?<=e)\.|(?<=Ph)\.'
                                     r'|(?<=a)\.|(?<=m)\.|(?<=Dr)\.|(?<=Mr)\.|(?<=Mrs)\.|(?<=Rep)\.|(?<=Lt)\.)',
                                     sentence)
        i = 0
        while i < len(words_in_sentence):
            el = words_in_sentence[i]
            if el == '' or el == '.' or el == ' ' or el.isnumeric():
                words_in_sentence.remove(el)
                i -= 1
            i += 1

        i = 0
        while i < len(words_in_sentence):
            for el in words_in_sentence[i]:
                words_in_sentence[i] = re.sub(r'\.|\?|!|,|;|\(|\)|\s|:|-|\"|\'|_', '', words_in_sentence[i])
            total_num_of_chars_in_words += len(words_in_sentence[i])
            i += 1

        i = 0
        while i < len(words_in_sentence):
            el = words_in_sentence[i]
            if el == '' or el == ' ':
                words_in_sentence.remove(el)
                i -= 1
            i += 1

        words_in_text += words_in_sentence
        print("Final list of words in the sentence: " + str(words_in_sentence))
    return words_in_text, total_num_of_chars_in_words


def get_dictionary_of_ngrams(words: list[str], n: int) -> dict:
    groups_of_ngrams = dict()
    key_group = []
    j = 0
    for i in range(len(words) - 1):
        if len(words) - j >= n:
            for counter in range(n):
                key_group.append(words[j + counter])
            j = i + 1
            if not tuple(key_group) in groups_of_ngrams:
                groups_of_ngrams[tuple(key_group)] = 1
            else:
                groups_of_ngrams[tuple(key_group)] = groups_of_ngrams[tuple(key_group)] + 1
            key_group.clear()
    return groups_of_ngrams


def get_list_of_top_k_ngrams(ngrams: dict[str, int], k: int) -> list[str]:
    sorted_ngrams = dict(sorted(ngrams.items(), key=lambda item: item[1], reverse=True))
    top_k = []
    i = 0
    for a in sorted_ngrams.items():
        if i >= k:
            break
        if i < len(sorted_ngrams):
            top_k.append(a[0])
        i += 1
    return top_k
