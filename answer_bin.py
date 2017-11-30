import sys
import os
import nltk
from stanfordcorenlp import StanfordCoreNLP
import logging
import json
from nltk.parse import stanford
from nltk.tree import Tree as Tree
from parse_sentence import *
from pattern.en import conjugate
from pattern.en import tenses
import nltk, string
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from binary import Binary
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

reload(sys)  
sys.setdefaultencoding('utf8')

Binary = Binary()
sNLP = StanfordNLP()

class Answer_Bin:

	def __init__(self):
		self.stemmer = 0
		self.remove_punctuation_map = 0
		self.vectorizer = 0

	def parse_text(self, filename):
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
		fp = open(filename)
		data = fp.read()
		sentences = tokenizer.tokenize(data)
		sentences = [si for si in sentences if "\n" not in si]
		sentences = [s.encode('ascii', 'ignore') for s in sentences]
		return sentences

	def easy_find(self, text, sentences):
		return process.extractOne(text, sentences, scorer=fuzz.token_sort_ratio)[0]

	def is_bin_q(self, tree):
		for s in tree.subtrees(lambda t: t.label() == "SQ"):
			return True
		return False

	# find_answer_sent(sentences, "In his teens, Did Dempsey maintain these ties playing in a local Mexican-dominated adult league")
	def positive_bin_answer(self, text):
		tree = sNLP.parse(text)
		tree = Tree.fromstring(str(tree))
		for t in tree[0]:
			if t.label() == "VP":
				VP = 1
				for tt in t:
					if tt.label() == "RB":
						return 0
		return 1

	def answer_bin(self, text, filename):
		tree = sNLP.parse(text)
		tree = Tree.fromstring(str(tree))
		if not self.is_bin_q(tree):
			print "This question is not binary."
		sentences = self.parse_text(filename) 
		sent = self.easy_find(text, sentences)
		print sent
		negative_word = self.positive_bin_answer(sent)
		return 

	def get_raw_answer(self, question, answer):
		q_tree = sNLP.parse(question)
		q_tree = Tree.fromstring(str(q_tree))
		a_tree = sNLP.parse(Binary.main(answer))
		a_tree = Tree.fromstring(str(a_tree))
		res = True
		(q_top_level_structure, q_parse_by_structure) = self.get_top_level_structure(q_tree)
		(a_top_level_structure, a_parse_by_structure) = self.get_top_level_structure(a_tree)
		for i in range(0, len(q_top_level_structure)):
			q_label = q_top_level_structure[i]
			if q_label in a_top_level_structure:
				a_index = a_top_level_structure.index(q_label)
			else:
				print "label not found"
				return False
			# print "Result:!!!!!", self.partial_matching(q_parse_by_structure[i], a_parse_by_structure[a_index])
			if not self.partial_matching(q_parse_by_structure[i], a_parse_by_structure[a_index]):
				# print "struct:", q_parse_by_structure[i], a_parse_by_structure[a_index]
				return False
		return True

	def get_top_level_structure(self, tree):
		top_level_structure = []
		parse_by_structure = []
		for t in tree.subtrees(lambda t: t.label() == "SQ"):
			for tt in t:
				top_level_structure.append(tt.label())
				parse_by_structure.append(tt.leaves())
			return (top_level_structure, parse_by_structure)


	def get_synonyms_antonyms(self, word):
		synonyms = []
		antonyms = []
		for syn in wordnet.synsets(word):
			for l in syn.lemmas():
				synonyms.append(l.name())
				if l.antonyms():
					antonyms.append(l.antonyms()[0].name())
			for l in syn.hypernyms():
				synonyms.append(l.name().split(".")[0])
		return synonyms, antonyms

	def partial_matching(self, question_list, answer_list):
		res = True
		question_list = [word for word in question_list if word not in stopwords.words('english')]
		answer_list = [word for word in answer_list if word not in stopwords.words('english')]
		synonyms_list = []
		antonyms_list = []
		for word in question_list:
			synonyms_list.append(word)
			(synonyms, antonyms) = self.get_synonyms_antonyms(word)
			synonyms_list += synonyms
			antonyms_list += antonyms
		# print synonyms_list , antonyms_list
		for word in answer_list:
			if not word in synonyms_list:
				# print "syn: ", synonyms_list
				return False
			if word in antonyms_list:
				# print "anti: ", antonyms_list
				return False
		return True

	def main(self, question, filename):
		tree = sNLP.parse(question)
		tree = Tree.fromstring(str(tree))
		if not self.is_bin_q(tree):
			print "This question is not binary."
		sentences = self.parse_text(filename) 
		answer = self.easy_find(question, sentences)

		positive = self.positive_bin_answer(answer)
		res = self.get_raw_answer(question, answer)
		print question
		print answer
		if res == True:
			if positive == False:
				return "No."
			else:
				return "Yes."
		else:
			if positive == False:
				return "Yes."
			else:
				return "No."

# Answer_Bin = Answer_Bin()
# # print Answer_Bin.answer_bin("On November 27, 1995, did Dempsey loose his then 16-year-old sister Jennifer to a brain aneurysm?", "data/set1/a1.txt")
# # print Binary.main("On November 27, 1995, Dempsey lost his then 16-year-old sister Jennifer to a brain aneurysm.")
# # print Answer_Bin.main("On November 27, 1995, did Dempsey lose his then 16-year-old sister Jennifer to a brain aneurysm?", "data/set1/a1.txt")
# # print Answer_Bin.get_raw_answer("On November 27, 1995, did Dempsey lose his then 16-year-old sister Jennifer to a brain aneurysm?", "On November 27, 1995, Dempsey lost his then 16-year-old sister Jennifer to a brain aneurysm.")

# # print Answer_Bin.partial_matching(['lose', 'his', 'then', '16-year-old', 'sister', 'Jennifer', 'to', 'a', 'brain', 'aneurysm'], 
# 	# ['lose', 'his', 'then', '16-year-old', 'sister', 'Jennifer', 'to', 'a', 'brain', 'aneurysm'])

# print Answer_Bin.main("On November 27, 1995, did Dempsey lose his then 16-year-old sister Jennifer to a brain aneurysm?", "data/set1/a1.txt")

# print Answer_Bin.main("On November 27, 1995, did Dempsey lose his then 16-year-old sister Jennifer to a fever?", "data/set1/a1.txt")









