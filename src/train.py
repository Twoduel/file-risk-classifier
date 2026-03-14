## 모델 학습

from sklearn.model_selection import train_test_split   # Train / Test 분리
from sklearn.linear_model import LogisticRegression    # 모델 생성
from sklearn.metrics import accuracy_score             # 정확도 계산

import pickle                  # 학습한 모델 저장
import os

from utils import load_data    # utils 파일의 load_data()

# 데이터 로드
features, labels = load_data()

# Train / Test 분리
X_train, X_test, Y_train, Y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

# 모델 생성
model = LogisticRegression()

# 모델 학습
model.fit(X_train, Y_train)

# 결과 예측
predictions = model.predict(X_test)

# 정확도 계산
acc = accuracy_score(Y_test, predictions)

print("모델 정확도: ", acc)

# model 폴더가 없으면 model 생성
os.makedirs("model", exist_ok=True)

# 학습된 모델 저장
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("모델 저장 완료!")