# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
########### 머신러닝 강의노트 1 ##############

# bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7,
# 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5,
# 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0,
# 38.5, 38.5, 39.5, 41.0, 41.0]
# bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0,
# 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0,
# 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0,
# 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2,
# 12.4, 13.0, 14.3, 15.0]
# smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4,
# 12.2, 19.7, 19.9]

# length = bream_length+smelt_length
# weight = bream_weight+smelt_weight
# # print(length)
# # print(weight)

# fish_data = [[l, w] for l, w in zip(length, weight)]
# print(fish_data[0:5])
# import pandas as pd 
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn import metrics

# iris = datasets.load_iris()
# print(iris.data[0:5])
# print(iris.target[0:5])

# data = pd.DataFrame(
# {'sepal length': iris.data[:, 0], 'sepal width': iris.data[:, 1],
# 'petal length': iris.data[:, 2], 'petal width': iris.data[:, 3],
# 'species': iris.target}
# )
# print(data.head())

# x = data[['sepal length', 'sepal width', 'petal length', 'petal width']]
# y = data['species']
# print(x.head())
# print(y.head())

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# print(len(x_train))
# print(len(x_test))
# print(len(y_train))
# print(len(y_test))

# forest = RandomForestClassifier(n_estimators=100, max_features = 3)
# # n_estimators : 생성할 tree의 개수, max_features : 최대 선택할 특성의 개수
# forest.fit(x_train, y_train)

# y_pred = forest.predict(x_test)
# print(y_pred)
# print(list(y_test))
# print(metrics.accuracy_score(y_test, y_pred))

# 데이터 가져오기
# 데이터 train, test 분리
# 모형 구축
# 모형 성능 평가

# import seaborn as sns

# abalone = sns.load_dataset('abalone')
# print(abalone.head())

########### 머신러닝 강의노트 2 ############

import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset('iris')
# print(iris.tail(6))

input_var = iris.iloc[:, :-1] # 마지막 열을 제외한 모든 열
# print(input_var)
target_var = iris.iloc[:, [-1]] # 마지막 열
# print(target_var)

sns.scatterplot(x='sepal_length', 
                y='sepal_width',
                hue='species', #species의 종류에따라 색상 구분
                style ="species", #species의 종류에따라 점(markers, point) 형태 구분
                s=100, #점의 크기 지정
                data=iris)
# plt.show()

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(input_var) #(평균, 표준편차)를 '학습', '기억' 하는 단계
input_scaled = ss.transform(input_var) 
# print(input_scaled[0:5,])

from sklearn.decomposition import PCA
pca = PCA(n_components=2) #2차원으로 축소
pca.fit(input_scaled) #PCA 모형 학습   
iris_pca = pca.transform(input_scaled) #PCA 변환
# print(iris_pca.shape) #(150, 2)
# print(iris_pca[0:6,])

import pandas as pd
iris_pca = pd.DataFrame(iris_pca, columns=['PCA1', 'PCA2'])
# print(iris_pca)

sns.scatterplot(x='PCA1',
                y='PCA2',
                hue = target_var,
                style= target_var,
                s=100,
                data=iris_pca)
plt.show()


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
########### 머신러닝 과제 1 ##############
 