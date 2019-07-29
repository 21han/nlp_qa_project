from nltk.tree import Tree as Tree
from parse import Parse
from pattern.en import conjugate
from pattern.en import tenses


sNLP = Parse()

BE_VB_LIST = ["is", "was", "are", "am", "were", "will", "would", "could", "might", "may", "should", "can"]
DO_DID_DOES = ["do", "did", "does"]
VB_LIST = ["VBZ", "VBP", "VBD"]


class Binary:

	def convert(self, text, tree):
		parse_by_structure = []
		NEG = 0
		NP = 0
		VP = 0
		for t in tree[0]:
			if t.label() == "VP":
				VP = 1
			if t.label() == "NP":
				NP = 1
			if t.label() != "VP":
				parse_by_structure += (t.leaves())
			else:
				for tt in t:
					if tt.label() != "RB":
						parse_by_structure += (tt.leaves())
					else:
						NEG = 1
		sent = " ".join(parse_by_structure)
		is_binary = NP and VP
		return (sent, NEG, is_binary)

	def bin_q_type(self, tree, text, neg):
		(top_level_structure, parse_by_structure) = self.get_top_level_structure(tree)
		verb_index = top_level_structure.index("VB")
		verb = parse_by_structure[verb_index]
		np_index = top_level_structure.index("NP")
		if verb in BE_VB_LIST or neg == 1:
			return self.be_q(parse_by_structure, verb_index, np_index)
		else:
			return self.do_q(parse_by_structure, verb_index, np_index)


	def get_top_level_structure(self, tree):
		top_level_structure = []
		parse_by_structure = []
		for t in tree[0]:
			if t.label() == "VP":
				parse_by_structure += self.get_VB(t)
				top_level_structure += ["VB", "OTHER"]
			else:
				parse_by_structure.append(" ".join(t.leaves()))
				top_level_structure.append(t.label())
		return (top_level_structure, parse_by_structure)


	def get_VB(self, subtree):
		res = []
		for t in subtree:
			if t.label() in VB_LIST:
				res.append(" ".join(t.leaves()))
			else:
				res.append(" ".join(t.leaves()))
		return (res)


	def be_q(self, parse_by_structure, verb_index, np_index):
		verb = parse_by_structure[verb_index]
		nb = parse_by_structure[np_index]
		sent = parse_by_structure
		sent[verb_index] = nb
		sent[np_index] = verb
		sent[-1] = "?"
		sent = " ".join(sent)
		return sent

	def do_q(self, parse_by_structure, verb_index, np_index):
		verb = parse_by_structure[verb_index]
		(tense, person, a, b, c) = tenses(verb)[0]
		present_verb = str(conjugate(verb, tense = "present", person = 1))
		sent = parse_by_structure
		sent[verb_index] = present_verb
		if tense == 'past':
			sent.insert(np_index, "did")
		elif tense == 'present' and person == 3:
			sent.insert(np_index, "does")
		else :
			sent.insert(np_index, "do")
		sent[-1] = "?"
		sent = " ".join(sent)
		return sent 


	def main(self, text):
		print(f"check poin A: {text}")
		try:
			text = str(text)
			tree = sNLP.parse(text)
			tree = Tree.fromstring(str(tree))
			(sent, NEG, is_binary) = self.convert(text, tree)
			if not is_binary:
				print("*********************", text)
				print("It could not be converted to binary question.")
				return False
			tree = sNLP.parse(sent)
			tree = Tree.fromstring(str(tree))
			# print self.bin_q_type(tree, sent, NEG)
			return self.bin_q_type(tree, sent, NEG)
		except Exception as e:
			print(e)