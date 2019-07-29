from bin_questions import BinQuestion
from binary import Binary
from wh_question import WH
from tokenize import Tokenize


class Ask:

    def main(self, k):
        print("\n\n\n\n")
        print("Check Point 0")
        T = Tokenize.main(k, "einstein.txt")
        sentences_top_k = T[0]
        NE = T[1]
        # print(sentences_top_k)
        questions = []
        for si in sentences_top_k:
            print("	*** org  : ", si)
            # print(" *** original sentence: ", si)
            bin_attempt = Binary.main(si)
            wh_attempt = WH.main(bin_attempt, si, NE)
            if bin_attempt:
                print("	*** bin : ", bin_attempt)
                questions.append(bin_attempt)
            if wh_attempt:
                questions.append(wh_attempt)
            print("\n")
        print("\n\n\n\n")
        # for q in questions:
        #     print q


if __name__ == '__main__':
    Tokenize = Tokenize()
    BinQuestion = BinQuestion()
    Binary = Binary()
    WH = WH()
    run = Ask()
    run.main(20)
