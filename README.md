## NLP Question Answering Project

CMU 11-411 NLP Question Answering Project

`last_modified_date = 2019/07/28`: 

+ upgraded to Python 3.7
+ Python 2 is officially deprecated
+ added `requirement.txt` file as requested by many people on Youtube and personally
+ added `setup.sh` to get `stanfordcorenlp` and `java`
+ cleaned up `Readme.md` and removed some junk files to keep things tidy

## Requirements

Try the followings:

+ `pip install -r requirement.txt`
+ `./setup.sh`, please open and read this file before running.

## How to use 

```
python ask.py einstein.txt 20
```

```
python answer.py einstein.txt questions.txt
```

## Big Picture
I have explained the big picture (definitions of the problem, syntactic versus semantics method, parsing approach, type of grammars, overall architecture of code, possible improvements) in the following Youtube Video:
https://youtu.be/ohM7D21C_8Q or for your convenience: you may click [here](https://youtu.be/ohM7D21C_8Q)


## Credits

I collaborated with Angela Liang during the oldest version (prior 2018).
Now, I am only maintaining it per requests. Please drop issues if you have trouble running codes.
Usually, I will get back to you within 48 hours as courtesy.
