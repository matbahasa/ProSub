def Extract(file_name):
    with open(file_name, "r", encoding="utf-8") as fh:
        f = json.load(fh)

    # file id
    ID = f["id"]

    # Extract utterance
    text = []
    utt = f["document"][0]["utterance"]
    for u in utt:
      speaker = u["speaker_id"]
      form = u["form"]
      original_form = u["original_form"]
      text.append((speaker,form,original_form))

    return ID,text

# Read json file
import glob,json
#file_path = "./NIKL_SPOKEN_v1.1/"
#files = glob.glob(file_path+"NIKL_SPOKEN_v1.1/*.json")
file_path = "./NIKL_DIALOGUE_2020_v1.1/"
files = glob.glob(file_path+"*.json")

# Conversion
import os
dirs = ["form","original_form"]
for d in dirs:
    os.makedirs(file_path+"Converted/"+d)

IDs = []
for f in files:
    ID,text = Extract(f)

    print(ID)
    IDs.append(ID)

    # Format 1: speaker [TAB] form
    with open(file_path+"Converted/form/"+ID+"-form.txt", "w", encoding="utf-8") as out:
      for i in text:
        print(i[0], i[1], sep="\t", file=out)

    # Format 2: speaker [TAB] original_form
    with open(file_path+"Converted/original_form/"+ID+"-original_form.txt", "w", encoding="utf-8") as out:
      for i in text:
        print(i[0], i[2], sep="\t", file=out)

# Create file list
with open(file_path+"file_list.txt", "w", encoding="utf-8") as out:
    for f in files:
        print(f, file=out)
