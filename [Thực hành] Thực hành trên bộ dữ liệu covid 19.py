import pandas as pd

df = pd.read_csv("data\subset-covid-data.csv", encoding = "UTF-8")

# Tổng số lượng người mắc bệnh của từng châu lục
# df_group = df.groupby("continent").agg("sum")["cases"]
df_group = df.groupby("continent")["cases"].agg("sum")
print("Tổng số lượng người mắc bệnh của từng châu lục")
print(df_group)

#Top 5 quốc gia có số ca nhiễm mới cao nhất
df_covid = df.groupby("country")["cases"].sum().sort_values(ascending=False).head(5)
print("*"*30)
print("Top 5 quốc gia có số ca nhiễm mới cao nhất")
print((df_covid))

#Tổng số lượng ca tử vong của từng châu lục
print("*"*30)
print("Tổng số lượng ca tử vong của từng châu lục")
df_deaths = df.groupby("continent")["deaths"].sum()
print(df_deaths)

#Top 5 quốc gia có số lượng ca tử vong lớn nhất
print("*"*30)
print("Top 5 quốc gia có số lượng ca tử vong lớn nhất")
df_top5deaths = df.sort_values("deaths", ascending=False).head(5)
print(df_top5deaths)