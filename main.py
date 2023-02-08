import pandas

#  Get user input of what keyword they are searching for
keyword = str(input("What flavour are you looking for? "))

pandas.set_option('display.max_colwidth', 200)
df = pandas.read_csv("hotchoccontents.csv")
df = df[df['Content'].str.contains(keyword)]
print(df["Link"].to_string())

