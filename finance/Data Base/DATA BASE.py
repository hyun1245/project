import pandas as pd
df = pd.read_csv("data/충북소상공인.csv", encoding='cp949')
# print(df.head())
# print(df.isnull().sum())
# print(df.info())

# print(df.info()) # 데이터 정보
# selected = list(range(33)) + [35]
# df3 = df.iloc[:, selected]
# df2 = df.dropna(axis = 1)  # 결측치 제거
# print(df3.info())
# print(df3.head())

# 파일로 저장할 DataFrame이 'df'라고 가정합니다.
# 인덱스(index) 없이, 'cp949' 인코딩을 사용하여 CSV 파일로 저장합니다.

# df3.to_csv("data/충북소상공인_결측치제거2.csv", index=False, encoding='cp949')

# print(df3.info())
# print(df3.isnull().sum())  # 각 열의 결측치 개수 출력

# df4 = df3.dropna(axis = 0)  # 결측치가 있는 행 제거
# print(df4.info())
# print(df4.isnull().sum())  # 각 열의 결측치 개수 출력
# print(df4)
# print(str(df4['지번부번지']))

columns_to_drop = ["건물본번지", "건물부번지", "건물명", "지번본번지", "지번부번지","동정보", "호정보", "경도", "위도","구우편번호"]

# 원본 df에서 목록에 있는 열을 제거하고 새 DataFrame 생성
df5 = df.drop(columns=columns_to_drop, axis=1)

# print(df5.info())
# print(df5.isnull().sum())
# print(df5.dropna(axis = 0))

df6 = df5.dropna(axis = 0)
# print(df6.info())
df6.rename(columns={'신우편번호': '우편번호'}, inplace=True)
# print(df6.head())
print(df6.isnull().sum())
# df6.to_csv("data/충북소상공인_열 전처리2.csv", index=False, encoding='cp949')