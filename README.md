# NLP Question Answering Project

description: natural language processing question answering final project repo

## 1. Parse
To run `prase.py` file, please follow the [steps](https://www.khalidalnajjar.com/setup-use-stanford-corenlp-server-python/) and run the following command: 

```java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000```

