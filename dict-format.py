# encoding=utf-8
import re

def dict_format(infile):
    outfile = infile+".dic"
    words_set = set()
    with open(infile) as fin:
        for i in re.findall("[a-zA-Z]+",fin.read()):
            words_set.add(i)
    with open(outfile,"w") as fout:
        for i in words_set:
            fout.write(i+'\n')
    return outfile

if __name__ == "__main__":
    infile = "dict/grade9.txt"
    outfile = dict_format(infile)
    if outfile:
        print "Format successfully ! "
        print "Output file :",outfile
    else:
        print "Format filed!"
