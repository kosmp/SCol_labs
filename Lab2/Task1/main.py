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
                         r'(?<!B\.\sA)(?<!B(?=\.\sA\.))(?<!B\.A)(?<!B(?=\.A))'
                         r'(?<!i\.\se)(?<!i(?=\.\se\.))(?<!i\.e)(?<!i(?=\.e))'
                         r'(?<!e\.\sg)(?<!e(?=\.\sg\.))(?<!e\.g)(?<!e(?=\.g))'
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

    # print("Final list of sentences: " + str(sentences))
    return sentences


def get_number_of_words_and_num_of_chars(sentences: list[str]) -> tuple[list[str], int]:
    words_in_text = []
    total_num_of_chars_in_words = 0
    for sentence in sentences:
        words_in_sentence = re.split(r'(\s|\n|\"|\(|(?<=i)\.|(?<=e)\.|(?<=B)\.|(?<=A)\.|(?<=Ph)\.|(?<=D)\.'
                                     r'|(?<=a)\.|(?<=m)\.|(?<=Dr)\.|(?<=Mr)\.|(?<=Mrs)\.|(?<=Rep)\.|(?<=Lt)\.)',
                                     sentence)
        i = 0
        while i < len(words_in_sentence):
            for el in words_in_sentence[i]:
                words_in_sentence[i] = re.sub(r'\.|\?|!|,|;|\(|\)|\s|:|-|\"|\'|_', '', words_in_sentence[i])
                total_num_of_chars_in_words += len(words_in_sentence[i])
            i += 1

        i = 0
        while i < len(words_in_sentence):
            el = words_in_sentence[i]
            if el == '' or el == '.' or el == ' ' or el.isnumeric():
                words_in_sentence.remove(el)
                i -= 1
            i += 1
        words_in_text += words_in_sentence
        # print("Final list of words in the sentence: " + str(wordsInSentence))
    return words_in_text, total_num_of_chars_in_words


def get_dictionary_of_ngrams(words: list[str], n: int) -> dict:
    groups_of_ngrams = dict()
    key_group = []
    j = 0
    for i in range(len(list_of_words) - 1):
        if len(list_of_words) - j >= n:
            for counter in range(n):
                key_group.append(list_of_words[j + counter])
            j = i + 1
            if not tuple(key_group) in groups_of_ngrams:
                groups_of_ngrams[tuple(key_group)] = 1
            else:
                groups_of_ngrams[tuple(key_group)] = groups_of_ngrams[tuple(key_group)] + 1
            key_group.clear()
    return groups_of_ngrams


def get_list_of_top_k_ngrams(ngrams: dict[str, int], k: int) -> list[str]:
    sorted_ngrams = dict(sorted(dict_of_n_grams.items(), key=lambda item: item[1], reverse=True))
    top_k = []
    i = 0
    for a in sorted_ngrams.items():
        if i >= k:
            break
        if i < len(sorted_ngrams):
            top_k.append(a[0])
        i += 1
    return top_k


text_to_process = '''
Abf gr32f 4vd d4g75 32 5 ad, ba, cb etc.
Vcdgfd ad? Bdf ... cvvkd 3 64 f!
Nvf fs?!
Cdgdg e.g. gf dv, Dr. Smith. Vfgd vsd3.
Vsafassf vf...
My mother loved to remind me of the old saying "waste not, want not." Mvdsd gfd.
Robert De Niros character Travis Bickle famously asks, "Are you talkin to me?!"
"... Cdfds ngf!", John said to them.
Absaf! "Where were you yesterday?" Mr. Fox asked Grandpa.
Bob said to me "Vdsgshd cag. Bvdad gda32! Fvff msd."
A b a b a b, "Hello there!" Mvdssd bfd. C d a c d a c d a c d a c d a c d a!
Charlie fell out of the bag. (I wasnt fast enough to stop him!) At least we wont have to sweep the floor.
(Hi there!) (Mbfs vfs?)
'''

sentences_list = get_sentences_list_from_text(text_input(text_to_process))
print("Amount of sentences in the text: " + str(len(sentences_list)))

amount_of_declarative_sentences = get_amount_of_declarative_sentences(sentences_list)
print("Amount of declarative sentences in the text: " + str(amount_of_declarative_sentences))
print("Amount of non-declarative sentences in the text: " + str(len(sentences_list) - amount_of_declarative_sentences))

list_of_words, total_num_of_chars = get_number_of_words_and_num_of_chars(sentences_list)
print("Average length of the sentence in characters(words count only): "
      + str(len(list_of_words) / len(sentences_list)))
print("Average length of the word in the text in characters: "
      + str(total_num_of_chars / len(list_of_words)))

try:
    print("If you dont want to change default values enter blank.")
    N = int(input("Enter N to see N-grams: "))
    K = int(input("Enter K to see top-K repeated N-grams: "))
except ValueError:
    print("No correct int values in input. Default values: N = 4, K = 10 will be set.")
    N = 4
    K = 10

dict_of_n_grams = get_dictionary_of_ngrams(list_of_words, N)
print("Dictionary of N-grams: " + str(dict_of_n_grams))

top_k_list = get_list_of_top_k_ngrams(dict_of_n_grams, K)
print(f"Top-K N-grams: {top_k_list}")
