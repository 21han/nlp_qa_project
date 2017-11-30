import sys
import os
import nltk
from collections import Counter

from stanfordcorenlp import StanfordCoreNLP
import logging
import json
from nltk.parse import stanford
from nltk.tree import Tree as Tree
from parse_sentence import *
from pattern.en import conjugate
from pattern.en import tenses
from binary import *
reload(sys)  
sys.setdefaultencoding('utf8')

from nltk import word_tokenize, pos_tag, ne_chunk

# sNLP = StanfordNLP()
Binary = Binary()

class What_Who:

	def is_who(self, text, NE):
		for ne in NE:
			if ne in text:
				return True
		tt =  ne_chunk(pos_tag(word_tokenize(text)))
		for s in tt.subtrees(lambda t: t.label() == "PERSON"):
			return True
		return False


	def main(self, text, NE):
		tree = sNLP.parse(text)
		tree = Tree.fromstring(str(tree))
		(top_level_structure, parse_by_structure) = Binary.get_top_level_structure(tree)
		np_index = top_level_structure.index("NP")
		if self.is_who(parse_by_structure[np_index], NE):
			parse_by_structure[np_index] = "who"
		else:
			parse_by_structure[np_index] = "what"
		parse_by_structure[-1] = "?"
		sent = " ".join(parse_by_structure)
		print sent
		return sent


# What_Who = What_Who()

# What_Who.main("Dempsey is the firt place.", ["Dempsey"])
# What_Who.main("Earth orbits the sun.", ["Dempsey"])
