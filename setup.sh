#!/usr/bin/env bash

# get standford core nlp
wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip
unzip stanford-corenlp-full-2018-10-05.zip

# get java if you already have java skip this section
brew update
brew install jenv
brew cask install java

# navigate to file
cd stanford-corenlp-full-2018-10-05/
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000