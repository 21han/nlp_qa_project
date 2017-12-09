# NLP Question Answering Project

description: natural language processing question answering system

## 1. Packages
To run `prase.py` file, please follow the [steps](https://www.khalidalnajjar.com/setup-use-stanford-corenlp-server-python/) (Only the first two steps are relevant. i.e. download the stanford core nlp library and running the server in terminal) and run the following command in the terminal: 

```java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000```

Here is a list of python modules I am using:

```{python}
# python default library
import sys
import operator
import re
import os
import random

# project modules
from bin_questions import BinQuestion
from parse import Parse
from tokenize import Tokenize

# installed packages
import nltk
from nltk.tree import Tree as Tree
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag, ne_chunk
from stanfordcorenlp import StanfordCoreNLP

from pattern.en import conjugate
from pattern.en import tenses
```
## 2. Running 
The command line for question generation takes 2 parameters: a directory of a .txt file and a number specifying how many questions to be generated.

```
./ask einstein.txt 20
```

The command line for answering takes 2 parameters: one directory of .txt file (source) and a directory of .txt file that contains a list of questions. The program will return a list of answer corresponding to each question.

```
./answer einstein.txt questions.txt
```

## 3. Overall Idea
I have explained the big picture in the following Youtube Video:
https://youtu.be/ohM7D21C_8Q or for your convenience: you may click (here)[https://youtu.be/ohM7D21C_8Q]




