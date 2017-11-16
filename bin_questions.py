from parse import Parse
from nltk.tree import Tree

class BinQuestion:
    binary_questions = []
    def main(self, k):
        binary_questions = []
        sentences_top_k = Parse.main(k)
        for si in sentences_top_k:
            si_pt = Parse.parse(si)
            bin_attemp = self.bin_question_extract(si_pt)
            if bin_attemp:
                binary_questions.append(bin_attemp)
        for q in binary_questions:
            print(q)

    def bin_question_extract(self, tree):
        tree_list = tree.split("\n")
        person_index = 0
        target_index = None
        acc = []
        person = None
        verb = None
        if "(NP " not in tree or "(VP " not in tree:
            return "Failure"
        for t in tree_list:
            if (len(t) - len(t.lstrip(" ")) == 4):
                if "(NP " in t:
                    person = (t.split(" ")[-1].rstrip(")"))
                    target_index = person_index
                    acc += [t]
                elif "(VBZ" in t:
                # (t.split(" ")[5]) == "(VBZ":
                    verb = (t.split(" ")[-1].rstrip(")"))
                    acc += [t.replace(verb, person)]
                else:
                    acc += [t]
            else:
                acc += [t]
            person_index += 1
        if person is None or verb is None:
            return None
        acc[target_index] = acc[target_index].replace(person, verb)
        acc_str = ("".join(acc))
        q_ls = Tree.fromstring(acc_str).leaves()
        q_ls[-1] = "?"
        return(" ".join(q_ls))

if __name__ == '__main__':
    Parse = Parse()
    run = BinQuestion()
    run.main(20)