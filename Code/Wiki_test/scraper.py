#This code called Wikipedias built in API to scrape a Wikipedia page and writes the contents of the page to a JSON file. 

import requests
import json


url = "https://en.wikipedia.org/w/api.php"

#To change what page the API scrapes, change the page param to have the title of the page that you want the API to access
#Pages accessed for this project:
    # "page" : "List of American films of 2025",
    # "page" : "List of American films of 2026",
    # "page" : "List of British films of 2025",
    # "page" : "List of British films of 2026",
params = {
    "action": "parse",
    "page" : "List of British films of 2026",
    "prop" : "wikitext",
    "format" : "json"
}

#Wikipedia requires a contact method when utlizing thier API to prevent over-utlization of resources
headers = {
    "User-Agent": "OscarsMLProject/1.0 (kmr4232@rit.edu)" 
}

response = requests.get(url, params=params, headers=headers)

print(response.status_code)
print(response.text[:500])

data = response.json()

#The following code dumps the json into a file. Each commented section of code correlates to a different file. I will recator this to accept arguments instead of
#hardcoding if I have time
# with open("wikipedia_2025.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)

# with open("wikipedia_2026.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)

# with open("british_2025.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)

with open("british_2026.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)


wikitext = data["parse"]["wikitext"]["*"]

print("Saved!")