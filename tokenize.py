import sys
import os
import nltk

    
class Tokenize:
    """ tokenize wiki article into sentences with top_k option """ 
    def main(self, k, topK = True):
        acc = []
        # 1. tokenize chunk of raw string into sentence
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        target_dir = sys.argv[1]
        target_file_object = open(target_dir)
        raw_data = target_file_object.read()
        sentences = (tokenizer.tokenize(raw_data))
        # 2. filter out ill-format sentences := ones contain new line symbol
        sentences = [si for si in sentences if "\n" not in si]
        # if we want to get top k shortest sentences
        if topK:
            # 3. get top 10 shortest sentences
            sentences_top_k = sorted(sentences, key = len)[:k]
            return sentences_top_k
        else:
            return sentences