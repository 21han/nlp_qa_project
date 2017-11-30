from stanfordcorenlp import StanfordCoreNLP
import logging
import json
from nltk.parse import stanford
from nltk.tree import Tree
import sys
reload(sys)  
sys.setdefaultencoding('utf8')


class StanfordNLP:

    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

if __name__ == '__main__':
    sNLP = StanfordNLP()
    text = 'he will be her in china.'
    tree = sNLP.parse(text)
    # print "parse:", [str(tree)]
    # # print "tree:", Tree.fromstring(str(tree))[0][1][0]

    # t = Tree.fromstring(str(tree))
    # for tt in t[0]:
    # 	print "tree: ", tt
    # print "pos: ", (sNLP.pos(text)[1][1]) == "NN"









