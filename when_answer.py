from parse import Parse
from nltk.tree import Tree as Tree
from wh_question import WH

""" identify when question and return a concise (PP) answer """

class When_answer:
    
    """ 
        input  : question and most relevant sentence in str
        output : answer in str
    """
    def get_answer(self, question, relevant):
        r_parsed = P.parse(relevant)
        r_tree = Tree.fromstring(r_parsed)
        for i in range(len(r_tree[0])):
            node = r_tree[0][i]
            if i == 0 and node.label() == "PP" and " ".join(node.leaves()).lower() not in question.lower():
                answer = " ".join(node.leaves()) + "."
                answer = answer[0].upper() + answer[1:]
                # print answer
                # print "^^^"
                return answer
            if node.label() == "VP":
                for sub_node in node:
                    if (sub_node.label() == "PP" or sub_node.label() == "SBAR") and " ".join(sub_node.leaves()).lower() not in question.lower():
                        answer = " ".join(sub_node.leaves()) + "."
                        answer = answer[0].upper() + answer[1:]
                        # print answer
                        return answer
        return relevant

class Where_answer:
    """ 
        input  : question and most relevant sentence in str
        output : answer in str
    """
    def get_answer(self, question, relevant):
        r_parsed = P.parse(relevant)
        r_tree = Tree.fromstring(r_parsed)
        for i in range(len(r_tree[0])):
            node = r_tree[0][i]
            if i == 0 and node.label() == "PP" and " ".join(node.leaves()).lower() not in question.lower():
                answer = " ".join(node.leaves()) + "."
                answer = answer[0].upper() + answer[1:]
                # print answer
                # print "^^^"
                return answer
            if node.label() == "VP":
                for sub_node in node:
                    if (sub_node.label() == "PP" or sub_node.label() == "SBAR") and " ".join(sub_node.leaves()).lower() not in question.lower():
                        answer = " ".join(sub_node.leaves()) + "."
                        answer = answer[0].upper() + answer[1:]
                        # print answer
                        return answer
        return relevant
    


WH = WH()
P = Parse()
# test_q = 'when did Clint Dempsey score against Ghana 29 seconds into the group play match ?'
# test_relevant = 'On June 16, Clint Dempsey scored against Ghana 29 seconds into the group play match.'
# test = When_answer()
# print test_q
# print test_relevant
# test.get_answer(test_q, test_relevant)

# test2 = Where_answer()
# test_q2 = "where did he obtain his master degree"
# test_relevant2 = "In England he obtained his master degree."
# test_relevant3 = "the picture is above the wall"
# test_q3 = "where is the picture?"
# print test_q2
# print test_relevant2
# test2.get_answer(test_q2, test_relevant2)
# print test_q3 
# print test_relevant3
# test2.get_answer(test_q3, test_relevant3)
# test_q4 = 'when did Dempsey won the highest individual honor in football in America? '
# test_relevant4 = 'Dempsy won the highest individual honor in football in America when he was named Honda Player of the Year for 2006, beating Fulham teammates Kasey Keller and Brian McBride in a poll of sportswriters.'
# print test_relevant4
# print test_q4
# test.get_answer(test_q4, test_relevant4)


        
