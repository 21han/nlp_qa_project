#!/usr/bin/env bash

# get the most recent standford core nlp
# please run this at path/nlp_qa_project/
wget http://nlp.stanford.edu/software/stanford-corenlp-latest.zip
unzip stanford-corenlp-latest.zip

# get java
# if you already have java please comment the next two lines
brew update
brew install jenv
brew cask install java

# navigate to downloaded directory and start the Standford Core NLP Server
# please comment the next two lines if you want to do this manually
cd stanford-corenlp-full-2018-10-05/
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000
