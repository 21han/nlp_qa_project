from parse import Parse
from nltk.tree import Tree as Tree
from binary import Binary
from why import Why
from what_who import What_Who
import operator
import re

class WH:

    """ wh : why, where, when, what, who type of questions  
        build upon binary questions """
    
    """ PP : WHEN """
    def when_check(self, node):
        """ check if time related PP """
        if (node.label() == "PP"):
            node_ner = Parse.ner(" ".join(node.leaves()))
            time_set = set(["DATE", "TIME"])
            if any(t in time_set for t in reduce(operator.concat, node_ner)):
                return True
            node_leaves = (" ".join(node.leaves())).lower()
            if re.search( r'in (.*?) time', node_leaves, re.M|re.I):
                return True
        return False
    
    def when(self, binary_t):
        acc = ""
        time = False
        for i in range(len(binary_t[0])):
            node = binary_t[0][i]
            if self.when_check(node) and i == 0:
                acc += "when"
                time = True
            elif time and node.label() == ",":
                acc += ""
            else:
                acc += " ".join(node.leaves())
            if i != 0:
                acc += " "
        if time:
            return acc
        else:
            return None
    
    """ PP : WHERE """
    def contain_loc(self, s):

        """ check if s contains prepositions of place and direction """ 

        loc_set = set(["above", "across", "after", 
                       "against", "along", "among",
                       "around", "at", "behind", "below", 
                       "beside", "between", "by", "close to",
                       "down", "from", "in front of", "inside",
                       "in", "into", "near", "next to", "off", "on",
                       "onto", "opposite", "out of", "outside", "over", 
                       "past", "through"])

        tree = Tree.fromstring(Parse.parse(s))
        for i in tree[0]:
            if (str(i.label()) == "PP" and 
                any(str(j).lower() in loc_set for j in i.leaves()) and
                not(self.when_check(i))):
                return "PP"
            if (str(i.label())) == "VP":
                for j in i:
                    # print j.label(), j.leaves()
                    if (str(j.label()) == "PP" and
                       any(str(k).lower() in loc_set for k in j.leaves()) and 
                       not(self.when_check(j))):
                       return "VP"
        return None

    def PP_location_deletion(self, si, C):
        acc = ""
        tree = Tree.fromstring(Parse.parse(si))
        if C == "PP":
            for node in tree[0]:
                if node.label() == "PP" or node.label() == ",":
                    acc += ""
                else:
                    acc += " ".join(node.leaves())
                acc += " "
            return acc
        elif C == "VP":
            # print "***************************"
            for node in tree[0]:
                # print "&&&", node.label(), " ".join(node.leaves())
                if node.label() == "VP":
                    for sub_node in node:
                        # print "&&&", sub_node.label(), " ".join(sub_node.leaves())
                        if sub_node.label() == "PP":
                            acc += ""
                        else:
                            acc += " ".join(sub_node.leaves())
                        acc += " "
                else:
                    acc += " ".join(node.leaves())
                acc += " "
            # print "$$$$$$$$$$", acc
            return acc
        else:
            # print "Error : Invalid Case"
            return None

    def where(self, si):
        C = self.contain_loc(si)
        if C:
            si_filtered = self.PP_location_deletion(si, C)
            binary_q = Binary.main(si_filtered)
            binary_q = binary_q[0].lower() + binary_q[1:]
            si_binary = binary_q
            if si_binary:
                return "where " + si_binary
            else:
                return None
        return None
                
    def main(self, binary, si, NE):
        # binary is string rep of binary question
        if binary:
            binary_t = Tree.fromstring(Parse.parse(binary))
            when = self.when(binary_t)
            where = self.where(si)
            why = Why.main(si)
            what_who = What_Who.main(si, NE)
            if when:
                print("	*** when : ", str(when))       
            if where:
                print(" *** wher : ", str(where))
            if why:
                print(" *** why  : ", str(why))
            if what_who:
                print(" *** www  : ", str(what_who))

Parse = Parse()
Binary = Binary()
Why = Why()
What_Who = What_Who()


