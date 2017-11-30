

class NEP:
    def transform_pronoun(self, raw_data):
        # tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        # target_dir = sys.argv[1]
        # target_file_object = open(target_dir)
        # raw_data = target_file_object.read()
        word_list = raw_data.lower().split(" ")
        ne_gender = None
        he_count = word_list.count("he")
        she_count = word_list.count("she")
        if he_count >= she_count:
            ne_gender = "he"
        else:
            ne_gender = "she"
        sentences = raw_data.split("\n")
        NE = sentences[0]
        first_name = NE.split(" ")[0]
        last_name = NE.split(" ")[1]
        sentences_nep = []
        if ne_gender == "he":
            for s in sentences:
                tmp = s.replace(" he ", " " + NE + " ")
                tmp = tmp.replace(" He ", " " + NE + " ")
                tmp = tmp.replace("He ", NE + " ")
                tmp = tmp.replace(" his ", " " + NE + "'s ")
                tmp = tmp.replace(" His ", " " + NE + "'s ")
                tmp = tmp.replace(" him ", " " + NE + " ")
                sentences_nep.append(tmp)
        else:
            for s in sentences:
                tmp = s.replace(" she ", " " + NE + " ")
                tmp = tmp.replace(" She ", " " + NE + " ")
                tmp = tmp.replace(" Her ", " " + NE + "'s ")
                sentences_nep.append(tmp)
        return ["\n".join(sentences_nep), [NE, first_name, last_name]]
    
        


# NEP = NEP()
# output = NEP.transform_pronoun()
# # print(test) 
# print("************************ \n\n\n\n *******************")
# print(output)

