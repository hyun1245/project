# Python → ⑴ 최소 제곱 : Linear Regression(sklearn) [STAT]
#          ⑵ 경사 하강법                            [ML]

from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version = 1, as_frame = False)
# print(mnist.keys())
# 사이킷런으로 받아들인 데이터셋들은 일반적으로 딕셔너리(dictionary) 구조를 가짐

x,y = mnist["data"], mnist['target']
# print(x.shape)
# print(y.shape)

import matplotlib.pyplot as plt
import matplotlib as mpl

some_digit = x[0]
some_digit_image = some_digit.reshape(28,28)
plt.imshow(some_digit_image, cmap = mpl.cm.binary)
# plt.show()
# cmap = mpl.cm.binary → 회색조(흑백)로 출력

import numpy as np
# print(y[0:10])
y = y.astype(np.uint8)
# print(y[0:10])
# unit8 → 2⁸ 개의 부호없는 정수표현 (0~255), 그레이 스케일 또는 3 채널 컬러 이미지 등에 사용

# 컬러로 표현할때는 R(red, 0~255), G(green, 0~255), B(blue, 0~255) 으로 표현되기 때문에
# matrix 형태로 표현이 안되기 때문에 3차원 배열로 표현해야 함 

# MNIST 데이터셋은 훈련 세트와 테스트 세트로 이미 나누어져 있음
# 훈련 세트 : 처음 60,000개 / 테스트 세트 : 마지막 10,000개
x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]

# 이진 분류기 훈련
y_train_5 = (y_train == 5) # 5이면 True, 아니면 False
y_test_5 = (y_test == 5) # 5이면 True, 아니면 False
# print(y_train_5)
# print(y_test_5)
# print(y_train_5.shape)
# print(y_test_5.shape)

from sklearn.linear_model import SGDClassifier
# max_iter = 1000 : 최대반복회수 1000회
# tol = 1e-3(손실함수) : 허용오차 0.001
sgd_clf = SGDClassifier(max_iter = 1000, tol = 1e-3, random_state=42)
sgd_clf.fit(x_train, y_train_5)

# 성능 측정
# ⑴ 모형의 정확도 계산 및 과대 적합 확인
# print(sgd_clf.score(x_train, y_train_5))
# print(sgd_clf.score(x_test, y_test_5))

# ⑵ SGD 모델을 사용하여 숫자 5 감지
# print(sgd_clf.predict([some_digit]))

# ⑶ Confusion Matrix (혼동 행렬) 생성
y_test_pred = sgd_clf.predict(x_test)

from sklearn.metrics import confusion_matrix
# print(confusion_matrix(y_test_5, y_test_pred))

# Confusion Matrix의 행 : 실제 클래스 (actual class) (1행 - '5 아님', 2행 - '5')
# Confusion Matrix의 열 : 예측 클래스 (predicted class) (1열 - '5 아님', 2열 - '5')

# print((8780 + 785) / (8780 + 401 + 107 + 785)) # 정확도(accuracy) 계산

# ⑷ 정밀도(precision)와 재현율(recall) 계산
from sklearn.metrics import precision_score, recall_score
# print(precision_score(y_test_5, y_test_pred))
# print(recall_score(y_test_5, y_test_pred))

# ⑸ F1 점수 계산
from sklearn.metrics import f1_score
# print(f1_score(y_test_5, y_test_pred))