#This code converts a text file into a csv file. It is specifically designed to work with a text file of wikitext. It speficially parses wikipedia tables 

import wikitextparser as wtp
import pandas as pd

# with open("wikipedia_2025_raw.txt", "r", encoding="utf-8") as f:
#     american_films_2025 = f.read()

with open("wikipedia_2026_raw.txt", "r", encoding="utf-8") as f:
     american_films_2026 = f.read()


# p = wtp.parse(american_films_2025)
p = wtp.parse(american_films_2026)


all_table = []

for i, table in enumerate(p.tables, start=1):
    rows = table.data()

    if not rows:
        continue 

    df = pd.DataFrame(rows[1:], columns=rows[0])
    df["Source table"] = i
    all_table.append(df)

for table in all_table[1:]:
    table.columns = [
        "Opening Month" if i == 0 and col == "Opening"
        else "Opening Day" if i == 1 and col == "Opening"
        else col
        for i, col in enumerate(table.columns)
    ]
dataset = pd.concat(all_table, ignore_index=True)

# dataset.to_csv(
#     "american_films_2025.csv",
#     index=False,
#     encoding="utf-8-sig"
# )

dataset.to_csv(
    "american_films_2026.csv",
    index=False,
    encoding="utf-8-sig"
)
