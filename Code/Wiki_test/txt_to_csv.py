#This code converts a text file into a csv file. It is specifically designed to work with a text file of wikitext. It speficially parses wikipedia tables 

import wikitextparser as wtp
import pandas as pd


def to_csv(txt_file):
    with open(txt_file, "r", encoding="utf-8") as f:
        movies_2000 = f.read()

    p = wtp.parse(movies_2000)


    all_table = []

    for i, table in enumerate(p.tables, start=1):
        rows = table.data()

        if not rows or len(rows) < 2:
            continue 

        header= rows[0]
        data_rows = rows[1:]

        valid_rows = [row for row in data_rows if len(row) == len(header)]
        if not valid_rows:
            continue

        df = pd.DataFrame(valid_rows, columns=header)

        df = df.loc[:, ~df.columns.duplicated()]

        if i > 1:
            df.columns = [
                "Opening Month" if i == 0 and col == "Opening"
                else "Opening Day" if i == 1 and col == "Opening"
                else col
                for i, col in enumerate(df.columns)
            ]

        df["Source table"] = i
        all_table.append(df)

    dataset = pd.concat(all_table, ignore_index=True)

    dataset.to_csv(
        "movies_2000.csv",
        mode="a",
        header=False,
        index=False,
        encoding="utf-8-sig"
    )
