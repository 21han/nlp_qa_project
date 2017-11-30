import sys
import os
import nltk
from collections import Counter
from stanfordcorenlp import StanfordCoreNLP
import logging
import json
from parse import Parse
from binary import Binary
from nltk.parse import stanford
from nltk.tree import Tree
reload(sys)  
sys.setdefaultencoding('utf8')

class Similarity:
    def main(self, original, question):
        # question = raw_input("Please enter your question: ")
        question = question[0].upper() + question[1:]
        q_parsed = P.parse(question)
        q_tree = Tree.fromstring(str(q_parsed))
        print "q_tree\n", q_tree
        o = B.main(original)
        o = o[0].upper() + o[1:]
        o_parsed = P.parse(o)
        o_tree = Tree.fromstring(o_parsed)
        print "o_tree\n", o_tree

        o_tree_body = o_tree[0]
        for i in range(len(o_tree_body)):
            node = o_tree_body[i]
            level_leaves = node.leaves()
            
            if i < len(q_tree[0]) and q_tree[0][i].label() == node.label():
                print level_leaves
                print q_tree[0][i].leaves()

            
            
            


        print '\n\n\n\n\n'









question = "is life like an onion?"
test = "life is not like a vegetable."

P = Parse()
B = Binary()
S = Similarity()
S.main(test, question)

