#This code takes a JSON file and rewrites it into a txt file. This allows for easier reading and parsing

import json

#The following code opens a different json file to read from (will be refactored if time allows) 

# with open("wikipedia_2025.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# with open("wikipedia_2026.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

with open("british_2025.json", "r", encoding="utf-8") as f:
    data = json.load(f)

wikitext = data["parse"]["wikitext"]["*"]

#The following code writes the json into a txt file. (Refactored if time allows )
# with open("wikipedia_2025_raw.txt", "w", encoding="utf-8") as file:
#     file.write(wikitext.replace("\\n", "\n"))

# with open("wikipedia_2026_raw.txt", "w", encoding="utf-8") as file:
#     file.write(wikitext.replace("\\n", "\n"))

with open("british_2025_raw.txt", "w", encoding="utf-8") as file:
    file.write(wikitext.replace("\\n", "\n"))


print(wikitext[:500])