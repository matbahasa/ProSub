import json

def doccano2UAM(jsonl,filename):
    """
    Convert doccano jsonl to UAM tab-delimited text
    """
    annotations = []
#    check= open("corpus_validation.txt","w",encoding="utf-8")
    with open(jsonl, "r", encoding="utf-8") as f:
        json_list = list(f)
        start = 0 #start index of the line in the entire file
        for i in json_list:
            item = json.loads(i)
#            print(item["text"], file=check)
            if item["label"]:
                for l in item["label"]:
                    ID,s,e,tag,sent = item["id"],l[0],l[1],l[2],item["text"]
                    s = int(s) #index in each line
                    e = int(e)
                    text = sent[s:e]
                    s = s + start #index in the entire file
                    e = e + start
                    annotations.append((ID,s,e,text,tag))
            start += len(item["text"]) + 2 #Windows line break \r\n
#    check.close()
    with open(filename[:-4]+"-prosub.txt", "w", encoding="utf-8") as out:
        print("Subcorp\tFilename\tID\tStart\tEnd\tText\tComment\tRole\tParentID\tdoc_completeness\tprosub\t1st\t2nd\taddress", file=out)
        for a in annotations:
            ID,s,e,text,tag = a
            if tag == "Speaker":
                print("Texts",filename,ID,s,e,text,"\t\t\t\t1\t1\t0\t0", sep="\t",
                        file=out)
            elif tag == "Addressee":
                print("Texts",filename,ID,s,e,text,"\t\t\t\t1\t0\t1\t0", sep="\t",
                        file=out)
            elif tag == "AddressTerm":
                print("Texts",filename,ID,s,e,text,"\t\t\t\t1\t0\t0\t1", sep="\t",
                        file=out)

def ETA2doccano(summary):
    """
    Convert ETA summary table to doccano jsonl
    """
    filename = ""
    text_length = 0 #need this b/c # of columns varies depending on texts
    json = []
    count = 0
    with open(summary, "r", encoding="utf-8") as f:
        for l in f:
            items = l.strip("\n").split("\t")
            if items[0] == "File Name":
                filename = items[1]
            elif items[0] == "Text":
                text_length = len(items) - 8 #1st, 2nd, 3rd, null * 2 = 8
            elif items[0] and items[0] not in ["Feature", "Editor's Name"]:
                text = "\t".join(items[:text_length])
#                print(text)
                labels = ""
                if items[-7]:
                    words = items[-7].split(";")
#                    print(words)
                    current_position = 0 #where in the text to start searching from
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text[current_position:].index(w) + current_position
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"1st"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"1st"')
                        current_position = e
                if items[-5]:
                    words = items[-5].split(";")
#                    print(words)
                    current_position = 0 #where in the text to start searching from
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text[current_position:].index(w) + current_position
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"2nd"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"2nd"')
                        current_position = e
                if items[-3]:
                    words = items[-3].split(";")
#                    print(words)
                    current_position = 0 #where in the text to start searching from
                    for w in words:
                        if "【" in w: #exclude comments
                            w = w[:w.index("【")]
                        s = text[current_position:].index(w) + current_position
                        e = s + len(w)
                        if labels:
                            labels += ",[{},{},{}]".format(str(s),str(e),'"address"')
                        else:
                            labels += "[{},{},{}]".format(str(s),str(e),'"address"')
                        current_position = e
                text = text.replace("\t","\\t")
                text = text.replace('\"','\\"')
                string = '{"id":'+str(count)+',"text":"'+text+'","label":['+labels+']}'
                json.append(string)
                count += 1
    with open(filename[:-4]+"-prosub.jsonl", "w", encoding="utf-8") as out:
        for j in json:
            print(j, file=out)

if __name__ == "__main__":
#    #jsonl to UAM
#    f = "./tha/data_tha-prosub.jsonl"
#    filename = "data_tha.txt"
#    doccano2UAM(f, filename)

    #ETA to jsonl
    #f = "./jpn/data_jpn-summary.txt"
    #f = "data_jav-summary.txt"
    #ETA2doccano(f)
