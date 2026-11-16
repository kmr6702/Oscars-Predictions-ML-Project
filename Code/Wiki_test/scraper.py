#This code called Wikipedias built in API to scrape a Wikipedia page and writes the contents of the page to a JSON file. 

import requests
import json

def scrape(wiki_page, json_file):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "parse",
        "page" : wiki_page,
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

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


    wikitext = data["parse"]["wikitext"]["*"]

    print("Saved!")