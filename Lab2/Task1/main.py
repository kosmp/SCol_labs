import parser

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

sentences_list = parser.get_sentences_list_from_text(parser.text_input(text_to_process))
print("Amount of sentences in the text: " + str(len(sentences_list)))

amount_of_declarative_sentences = parser.get_amount_of_declarative_sentences(sentences_list)
print("Amount of declarative sentences in the text: " + str(amount_of_declarative_sentences))
print("Amount of non-declarative sentences in the text: " + str(len(sentences_list) - amount_of_declarative_sentences))

list_of_words, total_num_of_chars = parser.get_words_and_num_of_chars(sentences_list)
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

dict_of_n_grams = parser.get_dictionary_of_ngrams(list_of_words, N)
print("Dictionary of N-grams: " + str(dict_of_n_grams))

top_k_list = parser.get_list_of_top_k_ngrams(dict_of_n_grams, K)
print(f"Top-K N-grams: {top_k_list}")
