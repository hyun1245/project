import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
iris_50 = iris.iloc[:50, :]
print(iris_50)

import pandas as pd
df_iris = pd.DataFrame(iris)
df_iris.iloc[:50, :]
# species를 기준으로 그룹화후 기술통계량 산출 및 전치
df_iris.groupby('species').describe().transpose()
