#This code takes a JSON file and rewrites it into a txt file. This allows for easier reading and parsing

import json

def analyze(json_file, txt_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    wikitext = data["parse"]["wikitext"]["*"]

    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(wikitext.replace("\\n", "\n"))


