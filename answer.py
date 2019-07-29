import sys
from tokenize import Tokenize
from parse import Parse
from nltk.tree import Tree as Tree
from when_answer import WhenAnswer
from where_answer import WhereAnswer
from answer_bin import Answer_Bin


class Answer:
    """ command:  ./answer article.txt questions.txt """

    def get_label(self, question):
        tree = Parse().parse(question)
        tree = Tree.fromstring(str(tree))
        for s in tree.subtrees(lambda t: t.label() == "WP" or t.label() == "WRB"):
            if "who" in s.leaves() or "Who" in s.leaves():
                return "who"
            if "what" in s.leaves() or "What" in s.leaves():
                return "what"
            if "why" in s.leaves() or "Why" in s.leaves():
                return "why"
            if "where" in s.leaves() or "Where" in s.leaves():
                return "where"
            if "when" in s.leaves() or "When" in s.leaves():
                return "when"
            else:
                return "other"
        for _ in tree.subtrees(lambda t: t.label() == "WP$"):
            return "other"
        return "binary"

    @staticmethod
    def read_txt(dir):
        with open(dir) as f:
            body = f.readlines()
        body = [x.strip() for x in body]
        return body

    def main(self):
        sentences = Tokenize.main(20, article, False)[0]
        for question in self.read_txt(questions):
            print(question)
            label = self.get_label(question)
            relevant = Answer_Bin.easy_find(question, sentences)
            if label == "when":
                print(WhenAnswer().get_answer(question, relevant))
            elif label == "where":
                print(WhereAnswer().get_answer(question, relevant))
            else:
                print(relevant)


if __name__ == '__main__':
    Answer_Bin = Answer_Bin()
    Tokenize = Tokenize()
    article = sys.argv[1]
    questions = sys.argv[2]
    A = Answer()
    A.main()
