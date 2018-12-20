# encoding=utf-8
import os
import re

class ParaExtractor:
    def __init__(self,f_targ,f_ign,f_out): # target file, ignore words file, output file
        self.f_targ = f_targ
        self.f_ign = f_ign
        self.f_out = f_out
        self.dic_saved = set()
        self.dic_ign = set()
        # check file
        if not os.path.isfile(f_targ) or not os.path.isfile(f_ign):
            print "ERROR:File not exist!"
            return None
        # load ignore words
        with open(f_ign) as f:
            for i in f.readlines():
                self.dic_ign.add(i.strip())
    def extract(self):
        with open(self.f_targ) as fp_in, open(self.f_out,"w") as fp_out:
            for sentence in fp_in.read().replace('\n',' ').split("."):
                for each_word_raw in re.findall("[a-zA-Z]+",sentence):
                    each_word = each_word_raw.lower()
                    if each_word not in self.dic_ign \
                    and each_word not in self.dic_saved \
                    and len(each_word)>3:
                        self.dic_saved.add(each_word)
                        fp_out.write(each_word+'\n')
                            

if __name__ == "__main__":
    file_article = "article/tp5.txt"
    file_ignoreWords = "dict/grade9.txt.dic"
    file_output = "article/tp5.txt.dic"
    pExt = ParaExtractor(file_article,file_ignoreWords,file_output)
    pExt.extract()
