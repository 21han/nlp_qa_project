from nltk.tree import Tree
import re

class BinQuestion:
    
    def bin_question_extract(self, tree):
        t = Tree.fromstring(tree)
        t_pos = t.pos()
        return t_pos

    def leaves_of_label(self, t, LABEL):
        target_sub_t = t.subtrees(lambda t: t.label() == LABEL)
        for s in target_sub_t:
            return(" ".join(s.leaves()))

    def find_verb(self, vp, complement = False):
        if not complement:
            return(" ".join(vp[0].leaves()))
        else:
            acc = []
            if len(vp) >= 1:
                for i in vp[1:]:
                    acc += i.leaves()
                return(" ".join(acc))
            else:
                return("")

    def find_vp(self, tree):
        for t in tree[0]:
            if t.label() == 'VP':
                return t

    def find_np(self, tree):
        for t in tree[0]:
            if t.label() == "NP":
                return " ".join(t.leaves())
    
    def bin_q_type(self, tree):
        tree = Tree.fromstring(str(tree))
        # print(tree)

        BE_VB_LIST = ["is", "was", "are", "am", "were"]
        VB_LIST = ["VBZ", "VBP", "VBD"]
        top_level_structure = []

        for t in tree[0]:
            top_level_structure.append(t.label())
            
        # print("running *** : ", " ".join(top_level_structure))
        if "NP" not in top_level_structure and "VP" not in top_level_structure:
            print('Failure Message: Cannot Convert Into Simple Binary Question')
            return

        VP = self.find_vp(tree)
        NP = self.find_np(tree)
        verb = self.leaves_of_label(VP, "VBZ")
        verb = self.find_verb(VP)
        verb_comp = self.find_verb(VP, True)

        # print("NP ***** ", NP)
        # print("VP  **** ", VP)
        # print("verb *** ", verb)
        # print("verb_comp", verb_comp)
        
        acc = ""
        for i in tree[0]:
            if i.label() not in {"NP", "VP", "."}:
                acc += " ".join(i.leaves())
                acc += " "
            elif i.label() == "NP":
                acc += verb + " " + NP + " " + verb_comp
        print(acc + " ?")
            
    def tree_to_words(self, tree):
        tree = re.split(' ',tree)
        res = []
        for s in tree:
            for i in range(0, len(s)):
                if s[i] == ")":
                    res.append(s[0:i])
                    break
        return res
    

