from bin_questions import BinQuestion
from binary import Binary
from parse import Parse
from tokenize import Tokenize

class Ask:

    def main(self, k):
        binary_questions = []
        sentences_top_k = Tokenize.main(k)
        print(sentences_top_k)
        for si in sentences_top_k:
            # print("**** si is : ", si)
            print("************* ", si)
            bin_attemp = Binary.main(si)
        #     if bin_attemp:
        #         binary_questions.append(bin_attemp)
        # for q in binary_questions:
        #     print(q)

if __name__ == '__main__':
    Tokenize = Tokenize()
    BinQuestion = BinQuestion()
    Binary = Binary()
    run = Ask()
    run.main(3)
    # run.test()
