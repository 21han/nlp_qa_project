# NLP Question Answering Project

description: natural language processing question answering final project repo

## 1. Parse
To run `prase.py` file, please follow the [steps](https://www.khalidalnajjar.com/setup-use-stanford-corenlp-server-python/) (Only the first two steps are relevant. i.e. download the stanford core nlp library and running the server in terminal) and run the following command in the terminal: 

```java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000```



