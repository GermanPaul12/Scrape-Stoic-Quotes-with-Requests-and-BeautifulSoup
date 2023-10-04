import pandas as pd
with open("quotes.txt") as f:
    quotes = f.readlines()
df = pd.DataFrame(quotes, columns=["quote"])
df["length"] = df["quote"].apply(len)
df.sort_values(by="length", ascending=True, inplace=True)
with open("quote.txt", "w") as f:
    for i in df["quote"]:
        f.write(i)
