import sys
import os
import nltk
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from stanfordcorenlp import StanfordCoreNLP
import logging
import json
from nltk.parse import stanford
from nltk.tree import Tree as Tree

''' 
Parts of our parse function is based on the following source
Citation: https://www.khalidalnajjar.com/setup-use-stanford-corenlp-server-python/
''' 

class Parse:

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

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def main(self, k):
        acc = []
        # 1. tokenize chunk of raw string into sentence
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        target_dir = sys.argv[1]
        target_file_object = open(target_dir)
        raw_data = target_file_object.read()
        sentences = (tokenizer.tokenize(raw_data))
        # 2. filter out ill-format sentences := ones contain new line symbol
        sentences = [si for si in sentences if "\n" not in si]
        # 3. get top 10 shortest sentences
        sentences_top_k = sorted(sentences, key = len)[:k]
        o = 2
        test_tree_str = self.parse(sentences_top_k[o])
        print(sentences_top_k[o])
        self.get_toplevel_struct(test_tree_str)
        test_tree = Tree.fromstring(test_tree_str)
  
    
    def get_toplevel_struct(self, tree):
        tree_list = tree.split("\n")
        person_index = 0
        target_index = None
        acc = []
        be = None
        person = None
        if "(NP " not in tree or "(VP " not in tree:
            return "Failure"
        for t in tree_list:
            if (len(t) - len(t.lstrip(" ")) == 4):
                if "(NP " in t:
                    person = (t.split(" ")[-1].rstrip(")"))
                    target_index = person_index
                    acc += [t]
                elif (t.split(" ")[5]) == "(VBZ":
                    verb = (t.split(" ")[-1].rstrip(")"))
                    acc += [t.replace(verb, person)]
                else:
                    acc += [t]
            else:
                acc += [t]
            person_index += 1
        acc[target_index] = acc[target_index].replace(person, verb)
        acc_str = ("".join(acc))
        q_ls = Tree.fromstring(acc_str).leaves()
        q_ls[-1] = "?"
        print(" ".join(q_ls))

if __name__ == '__main__':
    run = Parse()
    # user defined top K shortest sentences in a wiki article
    run.main(20)
