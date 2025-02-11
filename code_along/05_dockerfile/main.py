from pathlib import path 

import pandas as pd
data_path=path(__file__).parent / "data"

print(data_path / "prog_book.csv")

df= pd.read_cvs(data_path)
print(df.head())
