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

class Parse:

    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP(host, port=port,
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }
    def main(self):
        # 1. tokenize chunk of raw string into sentence
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        target_dir = sys.argv[1]
        target_file_object = open(target_dir)
        raw_data = target_file_object.read()
        sentences = (tokenizer.tokenize(raw_data))
        # 2. filter out ill-format sentences := ones contain new line symbol
        sentences = [si for si in sentences if "\n" not in si]
        

run = Parse()
run.main()

if __name__ == '__main__':
    run = Parse()
    run.main()