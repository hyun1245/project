# import os
# import pandas as pd

# xls = os.listdir("data1")
# print(xls)
# dfs = []
# for i in xls:
#     df = pd.read_excel(f"data1/{i}", index_col = 0, dtype = {"code": str})
#     dfs.append(df)
# df = pd.concat(dfs)

# print(df.head())

# cond = df['day'] == "12월 결산"
# df = df[cond]

# print(df.head())

# cond = (df['roic'] > 0) & (df['ev/ebitda'] > 0)

# df2 = df[cond].copy()
# print(df2.head())

# df2['rank1'] = df2['roic'].rank(ascending = False)
# print(df2)

# df2['rank2'] = df2['ev/ebitda'].rank()
# print(df2)

# df2['rank'] = df2['rank1'] + df2['rank2']
# print(df2)

# print(df2.sort_values(by = 'rank').head(n=30))

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# import pandas as pd
# url = "http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701"
# dfs = pd.read_html(url)

# df = dfs[0]
# print(df)

# df2 = df.set_index(df.columns[0])
# print(df2)

# print(df2.filter(regex = "^2020").loc["매출총이익"].values[0])

# df3 = dfs[2]
# df4 = df3.set_index(df3.columns[0])
# print(df4)

# print(df4.filter(regex = "^2020").loc["자산"].values[0])

# url = "http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN="
# dfs = pd.read_html(url)
# dfs[0].iloc[4,1]

# url = "https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A005930"
# dfs = pd.read_html(url)

# df5 = dfs[10]
# df6 = df5.set_index(df5.columns[0])
# df6["Annual"].filter(regex = "^2020").loc["PBR"].values[0]

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# import os
# import pandas as pd

# #read excels and concat dataframe
# xls = os.listdir("data/data1")
# dfs = []
# for i in xls: 
#     df = pd.read_excel(f"data/data1/{i}", index_col = 0, dtype = {"code": str})
#     dfs.append(df)
# df = pd.concat(dfs)

# #filter
# cap_bound = df.sort_values(by = 'cap').iloc[20]['cap']
# cond = df['day'] == "12월 결산"
# df = df[cond]

# #screening
# cond = ((df['gp/a'] >0) & (df['pbr'] > 0))
# df2 = df[cond].copy()

# df2['rank1'] = df2['gp/a'].rank(ascending = False) # gp/a는 높으면 1등
# df2['rank2'] = df2['pbr'].rank()                     # pbr는 낮으면 1등
# df2['rank'] = df2['rank1'] + df2['rank2']
# print(df2.set_index('code', inplace = True))

# print(cap_bound)

# df3 = df2.sort_values(by = 'rank')

# cond = df3['cap'] < cap_bound
# print(df3[cond].head(n=30))

