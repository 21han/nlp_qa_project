from parse import Parse
from nltk.tree import Tree as Tree


class WhereAnswer:
    @staticmethod
    def get_answer(question, relevant):
        r_parsed = Parse().parse(relevant)
        r_tree = Tree.fromstring(r_parsed)
        for i in range(len(r_tree[0])):
            node = r_tree[0][i]
            if i == 0 and node.label() == "PP" and " ".join(node.leaves()).lower() not in question.lower():
                answer = " ".join(node.leaves()) + "."
                answer = answer[0].upper() + answer[1:]
                return answer
            if node.label() == "VP":
                for sub_node in node:
                    if (sub_node.label() == "PP" or sub_node.label() == "SBAR") and \
                            " ".join(sub_node.leaves()).lower() not in question.lower():
                        answer = " ".join(sub_node.leaves()) + "."
                        answer = answer[0].upper() + answer[1:]
                        return answer
        return relevant
