from stanfordcorenlp import StanfordCoreNLP
import logging
import json
class StanfordNLP:
	def __init__(self, host='http://localhost', port=9000):
		self.nlp = StanfordCoreNLP(host, port=port,
		timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
		self.props = {
		'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
		'pipelineLanguage': 'en',
		'outputFormat': 'json'}
	def word_tokenize(self, sentence):
		return self.nlp.word_tokenize(sentence)
if __name__ == '__main__':
	sNLP = StanfordNLP()
	text = 'A blog post using Stanford CoreNLP Server. Visit www.khalidalnajjar.com for more details.'
	print("Tokens:", sNLP.word_tokenize(text))