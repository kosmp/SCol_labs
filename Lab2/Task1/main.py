import re


text = '''
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
Charlie fell out of the bag. (I wasn’t fast enough to stop him!) At least we won’t have to sweep the floor.
(Hi there!) (Mbfs vfs?)
'''

sentences = re.split(r'(?<!Ph\.\sD)(?<!Ph(?=\.\sD\.))(?<!Ph\.D)(?<!Ph(?=\.D))'
                     r'(?<!B\.\sA)(?<!B(?=\.\sA\.))(?<!B\.A)(?<!B(?=\.A))'
                     r'(?<!i\.\se)(?<!i(?=\.\se\.))(?<!i\.e)(?<!i(?=\.e))'
                     r'(?<!e\.\sg)(?<!e(?=\.\sg\.))(?<!e\.g)(?<!e(?=\.g))'
                     r'(?<!Mr)(?<!Mrs)(?<!Dr)(?<!Lt)(?<!Rep)(?<!Mr)(?<!etc(?=\.[^\n]))'
                     r'(?<![ap]\.\sm)(?<![ap](?=\.\sm\.))(?<![ap]\.m)(?<![ap](?=\.m))'
                     r'((?<=[A-Za-z0-9])\.|!|\?|\?!|(?<=[A-Za-z0-9])\.\.\.|(?<=\.)\"|(?<=\?)\"|(?<=!)\"|'
                     r'(?<=[A-Za-z0-9])\.\)|!\)|\?|\?!\)|(?<=[A-Za-z0-9])\.\.\.\))'
                     r'(\s|\n|$)', text)

print(sentences)

# To remove extra newlines at the beginning of 1st sentence.
if len(sentences) > 0:
    lastNewLineInd = sentences[0].rfind('\n')
    if not len(sentences[0]) == lastNewLineInd + 1:
        sentences[0] = sentences[0][lastNewLineInd + 1:]

i = 0
while i < len(sentences):
    el = sentences[i]
    if i + 3 < len(sentences) and sentences[i + 1] != '"' and el != '"' and el.count('"') == 1 and el != '' and\
            el[-1] != '.' and el[-1] != '!' and el[-1] != '?':
        sentences[i] = sentences[i] + sentences[i + 1] + sentences[i + 2] + sentences[i + 3]
        el = sentences[i]
        if i + 4 < len(sentences):
            sentences = sentences[:i + 1] + sentences[i + 4:]
        else:
            sentences = sentences[:i + 1]
        continue
    if el == '.' or el == '!' or el == '?' or el == '?!' or el == '...' or el == '"' or\
            el == '.)' or el == '!)' or el == '?)' or el == '?!)' or el == '...)':
        sentences[i - 1] = sentences[i - 1] + el
    if el == '' or el == '.' or el == '...' or el == '!' or el == '?' or el == '?!' or el == ' ' or\
            el == '\n' or el == '"' or el == '.)' or el == '!)' or el == '?)' or el == '?!)' or el == '...)':
        sentences.remove(el)
        i -= 1
    i += 1

i = 0
while i < len(sentences):
    if (i == 0 or (
            i > 0 and sentences[i - 1][-1] == '.' or sentences[i - 1][-1] == '!' or sentences[i - 1][-1] == '?')) and\
            sentences[i].count('"') == 2 and sentences[i][0] == '"' and\
            sentences[i][-1] == '"' and i + 1 < len(sentences):
        sentences[i] = sentences[i] + ' ' + sentences[i + 1]
        sentences = sentences[:i + 1] + sentences[i + 2:]
    i += 1

# print("Final list of sentences: " + str(sentences))

print("Amount of sentences in the text: " + str(len(sentences)))

amountOfDeclarativeSentences = 0
for sentence in sentences:
    if sentence[-1] == '.' or sentence[-1] == '"' or (
            len(sentence) >= 2 and sentence[-1] == ')' and sentence[-2] == '.'):
        amountOfDeclarativeSentences += 1

print("Amount of declarative sentences in the text: " + str(amountOfDeclarativeSentences))
print("Amount of non-declarative sentences in the text: " + str(len(sentences) - amountOfDeclarativeSentences))

wordsInText = []
countOfWordsInText = 0
totalSumOfCharsInWords = 0
for sentence in sentences:
    wordsInSentence = re.split(r'(\s|\n|\"|\(|(?<=i)\.|(?<=e)\.|(?<=B)\.|(?<=A)\.|(?<=Ph)\.|(?<=D)\.'
                               r'|(?<=a)\.|(?<=m)\.|(?<=Dr)\.|(?<=Mr)\.|(?<=Mrs)\.|(?<=Rep)\.|(?<=Lt)\.)', sentence)
    i = 0
    while i < len(wordsInSentence):
        el = wordsInSentence[i]
        if el == '' or el == '.' or el == ' ' or not el[0].isalpha():
            wordsInSentence.remove(el)
            i -= 1
        i += 1

    i = 0
    while i < len(wordsInSentence):
        for el in wordsInSentence[i]:
            wordsInSentence[i] = re.sub(r'\.|\?|!|,|;|\(|\)|\s|:|-|\"|\'|_', '', wordsInSentence[i])
            totalSumOfCharsInWords += len(wordsInSentence[i])
        i += 1
    countOfWordsInText += len(sentence)
    wordsInText += wordsInSentence
    # print("Final list of words in the sentence: " + str(wordsInSentence))

print("Average length of the sentence in characters(words count only): " + str(countOfWordsInText / len(sentences)))
print("Average length of the word in the text in characters: " + str(totalSumOfCharsInWords / countOfWordsInText))

try:
    print("If you dont want to change default values enter blank.")
    N = int(input("Enter N to see N-grams: "))
    K = int(input("Enter K to see top-K repeated N-grams: "))
except ValueError:
    print("No correct int values in input. Default values: N = 4, K = 10 will be set.")
    N = 4
    K = 10

groupsOfNGrams = dict()
keyGroup = []
j = 0
for i in range(len(wordsInText) - 1):
    if len(wordsInText) - j >= N:
        for counter in range(N):
            keyGroup.append(wordsInText[j + counter])
        j = i + 1
        if not tuple(keyGroup) in groupsOfNGrams:
            groupsOfNGrams[tuple(keyGroup)] = 1
        else:
            groupsOfNGrams[tuple(keyGroup)] = groupsOfNGrams[tuple(keyGroup)] + 1
        keyGroup.clear()

print("Dictionary of N-grams: " + str(groupsOfNGrams))

sorted_NGrams = dict(sorted(groupsOfNGrams.items(), key=lambda item: item[1], reverse=True))

topK_list = []
i = 0
for a in sorted_NGrams.items():
    if i >= K:
        break
    if i < len(sorted_NGrams):
        topK_list.append(a[0])
    i += 1

print(f"Top-K N-grams: {topK_list}")
