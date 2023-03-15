import json

def ETA2doccano(summary):
    """
    Convert ETA summary table to doccano jsonl
    """
    filename = ""
    text_length = 0 #need this b/c # of columns vary depending on texts
    json = []
    count = 0
    with open(summary, "r", encoding="utf-8") as f:
        for l in f:
            items = l.strip("\n").split("\t")
            if items[0] == "File Name":
                filename = items[1]
            elif items[0] == "Text":
                text_length = len(items) - 8
            elif items[0] and items[0] not in ["Feature", "Editor's Name"]:
                text = "\t".join(items[:text_length])
#                print(text)
                labels = ""
                if items[-33]:
                    words = items[-33].split(";")
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"1st"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"1st"')
                if items[-25]:
                    words = items[-25].split(";")
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"1st"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"1st"')
                if items[-23]:
                    words = items[-25].split(";")
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"1st"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"1st"')
                if items[-13]:
                    words = items[-25].split(";")
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"1st"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"1st"')
                if items[-7]:
                    words = items[-7].split(";")
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"1st"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"1st"')
                if items[-31]:
                    words = items[-31].split(";")
#                    print(words)
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"2nd"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"2nd"')
                if items[-21]:
                    words = items[-21].split(";")
#                    print(words)
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"2nd"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"2nd"')
                if items[-19]:
                    words = items[-19].split(";")
#                    print(words)
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"2nd"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"2nd"')
                if items[-11]:
                    words = items[-11].split(";")
#                    print(words)
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"2nd"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"2nd"')
                if items[-5]:
                    words = items[-5].split(";")
#                    print(words)
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"2nd"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"2nd"')
                if items[-27]:
                    words = items[-27].split(";")
#                    print(words)
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text.index(w)
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"address"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"address"')
                text = text.replace("\t","\\t")
                string = '{"id":'+str(count)+',"text":"'+text+'","label":['+labels+']}'
                json.append(string)
                count += 1
    with open(filename+"-prosub.jsonl", "w", encoding="utf-8") as out:
        for j in json:
            print(j, file=out)

if __name__ == "__main__":
    import glob
    files = glob.glob("./gogeki2002/*-summary.txt")
    for f in files:
        print(f)
        ETA2doccano(f)
