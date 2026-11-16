from scraper import scrape
from analyze_wiki import analyze
from txt_to_csv import to_csv

def main():
    num_loops = int(input("How many pages would you like to process? "))

    for loops in range(num_loops):
        wiki_page = input("What page would you like to scrape? ")
        json_file = input("What is the name of the JSON file? ")
        txt_file = input("What is the name of the txt_file? ")

        scrape(wiki_page, json_file)
        analyze(json_file, txt_file)
        to_csv(txt_file)

        print("Finished processing page!")


if __name__ == "__main__":
    main()