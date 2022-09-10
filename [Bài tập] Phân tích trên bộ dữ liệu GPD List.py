import pandas as pd
df = pd.read_csv("data\GDPlist.csv", encoding="ISO-8859-1")

#1
print("The number of rows: ", df.shape[0])
print("The number of columns: ", df.shape[1])
print(df.dtypes)

#2
df.rename(columns={"Country":"Nuoc", "Continent":"Chauluc", "GDP (millions of US$)":"GDP (trieu $)"}, inplace=True)

#3
df.insert(0, "Thanhpho", pd.Series(df.loc[:,"Nuoc"]))

#4
df['Thanhpho'].replace(df.iloc[123,0],'Hanoi',inplace = True)

#5
df.drop(df.loc[df.Chauluc == "Asia"].index, axis= 0, inplace = True)

print(df)
