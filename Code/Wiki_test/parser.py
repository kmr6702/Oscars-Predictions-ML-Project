# with open("wikipedia_2025_raw.txt", "r", encoding="utf-8") as file:
#     wikitext = file.read()

with open("wikipedia_2026_raw.txt", "r", encoding="utf-8") as file:
    wikitext = file.read()

tables = wikitext.split("{|")

print(f"Number of table sections: {len(tables) - 1}")

for i, table in enumerate(tables[1:], start=1):
    print(f"\n--- TABLE {i} ---")
    print(table[:500]) 