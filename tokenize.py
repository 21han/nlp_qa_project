import sys
import os
import nltk
from name_entity_processing import NEP
    
class Tokenize:
    """ tokenize wiki article into sentences with top_k option """ 
    def main(self, k, article, topK = True):
        # print "Check Point 2"
        acc = []
        # 1. tokenize chunk of raw string into sentence
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        target_dir = article
        target_file_object = open(target_dir)
        raw_data = target_file_object.read()
        NEP_output = NEP.transform_pronoun(raw_data)
        raw_data = NEP_output[0]
        NE = NEP_output[1]
        # print "***********", raw_data
        sentences = (tokenizer.tokenize(raw_data))
        # 2. filter out ill-format sentences := ones contain new line symbol
        sentences = [si for si in sentences if "\n" not in si]
        sentences = [s.encode('ascii', 'ignore') for s in sentences]
        # if we want to get top k shortest sentences
        if topK:
            # 3. get top 10 shortest sentences
            sentences_top_k = sorted(sentences, key = len)[:k]
            return [sentences_top_k, NE]
        else:
            return [sentences, NE]

NEP = NEP()