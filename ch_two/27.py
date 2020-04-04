# The polysemy of a word is the number of senses 
# it has. Using WordNet, we can determine that the noun 
# dog has 7 senses with: len(wn.synsets('dog', 'n')). 
# Compute the average polysemy of nouns, 
# verbs, adjectives and adverbs according to WordNet.

import nltk
from nltk.corpus import wordnet as wn

poly_nouns = list(wn.all_synsets('n'))
poly_adjectives = list(wn.all_synsets('a'))
poly_verbs = list(wn.all_synsets('v'))
poly_adverbs = list(wn.all_synsets('r'))


def calc_words(synset):
	all_words = []
	for syn in synset:
		all_words += syn.lemma_names()
	# eliminates duplicates and gets the count
	total = len(set(all_words))
	return total

def total_senses(synset):
	senses = sum(1 for x in synset)
	return senses


def average_polysemy(synset):
	average = total_senses(synset) / calc_words(synset)
	return average

print("Polysemy for Nouns: \n")
print(average_polysemy(poly_nouns))
print("Polysemy for adjectives: \n")
print(average_polysemy(poly_adjectives))
print("Polysemy for Verbs: \n")
print(average_polysemy(poly_verbs))
print("Polysemy for Adveb: \n")
print(average_polysemy(poly_adverbs))
