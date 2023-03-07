import glob
import csv

files = glob.glob("transcript/*-luu.csv")

for f in files:
    with open(f, "r", encoding="cp932") as fh:
        out_file = "annotation/"+f[11:-4]+"-anno.tsv"
        with open(out_file, "w", encoding="utf-8") as out:
            for l in csv.reader(fh):
                if l[0]=="luuID":
                    print(l[0],l[3],l[4], sep="\t", file=out)
                else:
                    print(l[0],l[3][5:],l[4], sep="\t", file=out)
