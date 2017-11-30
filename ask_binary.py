import sys
import os
import nltk
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
reload(sys)  
sys.setdefaultencoding('utf8')

class Ask_Binary:
    
    """ tokenize wiki article into sentences with top_k option """ 

    def main(self):
        acc = []
        # 1. tokenize chunk of raw string into sentence
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        target_dir = sys.argv[1]
        target_file_object = open(target_dir)
        raw_data = target_file_object.read()
        sentences = (tokenizer.tokenize(raw_data))
        # 2. filter out ill-format sentences := ones contain new line symbol
        sentences = [si for si in sentences if "\n" not in si]
        # print("*****************", sentences)
        choices = [s.encode('ascii', 'ignore') for s in sentences]
        print process.extract("who was the only American player to score a goal in the tournament", choices, limit=2)
        return 0

run = Ask_Binary()
run.main()
