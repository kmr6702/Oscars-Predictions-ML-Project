import pandas as pd

df1 = pd.read_csv("Full_Data_2000-2024.csv.csv")
df2 = pd.read_csv("movies_2000 - movies_2000.csv.csv")

df1["title_clean"] = df1["Title"].astype(str).str.strip().str.lower()
df2["title_clean"] = df2["Title"].astype(str).str.strip().str.lower()

df2 = df2.rename(columns={
    "Production Companny": "Production Company",
    "Production company": "Production Company",
    "title": "Title"
})
df1 = df1.rename(columns={
    "Production Companny": "Production Company",
    "Production company": "Production Company",
    "title": "Title"
})

df2_unique = df2.drop_duplicates(subset=["title_clean"])

cols_to_merge = ["title_clean", "Opening Month", "Stars", "Directors", "Production Company"]

df1 = pd.merge(
    df1,
    df2_unique[cols_to_merge],
    on="title_clean",
    how="left"
)

df1 = df1.drop(columns=["title_clean"])
df1.to_csv("Finished_2000_to_2024.csv", index=False)