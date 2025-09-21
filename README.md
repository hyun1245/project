# fience

## 프로젝트 개요

이 프로젝트는 Python을 사용하여 데이터 분석 및 머신러닝을 수행하는 코드들을 포함하고 있습니다. 주요 내용은 다음과 같습니다.

- **데이터 분석**: `데이터 분석및 실습 3주차` 파일은 `seaborn`, `pandas`, `matplotlib` 라이브러리를 사용하여 아이리스 데이터셋을 분석하고 시각화하는 과정을 담고 있습니다.
- **머신러닝**: `머신러닝` 파일은 의사결정 트리 모델을 구축하고, 학습 및 평가하는 과정을 포함하고 있습니다.
- **NumPy 활용**: `02.py` 파일은 NumPy 라이브러리를 사용하여 배열을 생성하고, 다양한 연산을 수행하는 방법을 보여줍니다.

## 파일 설명

- `02.py`: NumPy 배열 생성 및 연산 예제 코드
- `데이터 분석및 실습 3주차`: 아이리스 데이터셋을 이용한 데이터 분석 및 시각화 코드
- `머신러닝`: 의사결정 트리 모델 구축 및 평가 코드
- `README.md`: 프로젝트 설명 파일
- `.vscode/settings.json`: VS Code 설정 파일

## 주요 라이브러리

- NumPy
- Pandas
- Seaborn
- Matplotlib
- scikit-learn

## 코드 설명

### 02.py

NumPy를 사용하여 배열을 생성하고, 배열 간 연산, 슬라이싱, 조건문 적용, 통계 연산 등을 수행하는 예제 코드를 포함하고 있습니다.

```python
import numpy as np

# 배열 생성
arr = np.array([1, 2, 3])

# 배열 연산
result = arr * 10

# 조건에 따른 값 변경
arr = np.where(arr > 10, 1, 0)

# 배열 합계 (열/행 기준)
arr = np.arange(8).reshape(4, 2)
print(arr.sum(axis=0)) # 열끼리 더함
print(arr.sum(axis=1)) # 행끼리 더함 


