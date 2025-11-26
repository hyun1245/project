from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

# Inpur 과 target 데이터의 크기 확인 → shape 속성 사용
print(diabetes.data.shape, diabetes.target.shape)

# 입력데이터와 타겟 데이터 자세히 보기
print(diabetes.data[:3])
print(diabetes.target[:3])

# 산점도 시각화
import matplotlib.pyplot as plt
plt.scatter(diabetes.data[:,2], diabetes.target) # 입력데이터의 3번째 변수와 타깃데이터
plt.xlabel('x')
plt.ylabel('y')
# plt.show()

# Train 데이터 준비
x = diabetes.data[:,2]  # 입력 데이터의 3번째 변수 사용
y = diabetes.target      # 타깃 데이터

print(x[0:5]) # 입력 데이터 일부 확인
print(y[0:5]) # 타깃 데이터 일부 확인