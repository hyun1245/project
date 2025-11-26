import numpy as np
perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
    21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
    22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
    27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
    36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
    40.0, 42.0, 43.0, 43.0, 43.5, 44.0] )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
    110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
    130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
    197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
    514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
    820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
    1000.0, 1000.0])


from sklearn.model_selection import train_test_split

# 훈련 세트와 테스트 세트로 분할
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42
)

# 훈련과 테스트의 input을 행렬 데이터로 바꿈
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(train_input, train_target)
# print(reg.coef_, reg.intercept_)

# Score 메서드
# 회귀모형의 결정계수 R² 계산
# print(reg.score(train_input, train_target))
# print(reg.score(test_input, test_target))

print(reg.predict([[50]]))  # 50cm 농어의 무게 예측

import matplotlib.pyplot as plt
plt.scatter(train_input, train_target)
plt.plot([15,50], [15*reg.coef_ + reg.intercept_, 50*reg.coef_ + reg.intercept_])
plt.scatter(50,1241, marker='^')
# plt.show()

from sklearn.metrics import mean_squared_error
train_pred = reg.predict(train_input)
mse_train = mean_squared_error(train_target, train_pred)
# print(mse_train)
test_pred = reg.predict(test_input)
mse_test = mean_squared_error(test_target, test_pred)
# print(mse_test)

# iris 데이터셋을 활용한 실습
import seaborn as sns
iris = sns.load_dataset('iris')
x = iris['petal_length']
y = iris['sepal_length']
x = x.to_numpy()
print(x)
print(y)

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    x, y, random_state=42
)
train_x = train_input.reshape(-1, 1)
test_x = test_input.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
reg_iris = LinearRegression()
reg_iris.fit(train_x, train_target)
print(reg_iris.coef_, reg_iris.intercept_)



