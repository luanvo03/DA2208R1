import pandas as pd
df = pd.read_csv("data\OnlineRetail.csv", encoding="ISO-8859-1")

#1
print("The number of rows: ", df.shape[0])
print("The number of columns: ", df.shape[1])
print(df.dtypes)

#2
csv = df.iloc[:,2:4]
csv.to_csv("OnlineRetail.csv")

#3
xlxs = df.head(1000)
xlxs.to_excel("OnlineRetail.xlsx")

#4
h5 = df.loc[df.Quantity >= 10]
h5.to_hdf("OnlineRetail.h5")

#5
json = df.iloc[1000:2001,3:6]
json.to_json("OnlineRetail.json")

#6
html = df.loc[df.InvoiceNo == "536365"]
html.to_html("OnlineRetail.html")