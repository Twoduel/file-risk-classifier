# 전체적인 코드 구조

import pandas as pd
from sklearn.model_selection import train_test_split  # Train / Test 분리
from sklearn.linear_model import LogisticRegression   # 모델 생성
from sklearn.metrics import accuracy_score            # 정확도 계산

data = pd.read_csv("data/file_data.csv")
print(data)

# 데이터 구조 분석
print("\n데이터 정보")
print(data.info())

# 데이터 분포 분석
print("\n통계 정보")
print(data.describe())

# 특정 컬럼만 보기
print("\n파일 size 컬럼")
print(data["size"])

# 조건으로 데이터 찾기
print("\nexe 파일만 보기")
print(data[data["has_exe"] == 1])

# 악성 파일만 확인
print("\n악성 파일만 확인")
print(data[data["label"] == "malware"])




## 머신러닝 학습용 데이터
# Feature / Label 분리
features = data[["size", "has_exe", "download_count"]]
labels = data["label"]

print("\nFeature 데이터")
print(features)

print("\n Label 데이터")
print(labels)

# label int type으로 변환
labels = data["label"].map({
    "safe": 0,
    "malware": 1
})

print("\n int type으로 변환된 Label")
print(labels)

# Train / Test 분리
X_train, X_test, Y_train, Y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

print("\nTrain 데이터 개수:", len(X_train))
print("Test 데이터 개수:", len(X_test))

# 모델 생성
model = LogisticRegression()

# 모델 학습
model.fit(X_train, Y_train)

# 예측
predictions = model.predict(X_test)
print("\n예측 결과")
print(predictions)

print("\n실제 값")
print(Y_test.values)

# 정확도 계산
acc = accuracy_score(Y_test, predictions)
print("\n모델 정확도:", acc)




## 새 파일 위험도 예측 기능
#"파일 정보(size, exe 여부, 다운로드 수)를 기반으로 머신러닝 모델이 위험 파일을 분류하도록 구현했습니다."
# 새로운 파일 데이터
new_file = [[1500, 1, 700]]
prediction = model.predict(new_file)
print("\n새 파일 예측 결과:", prediction)

# 예측 값 int->str으로 변환
if prediction[0] == 1:
    print("⚠️위험 파일 (malware)⚠️")
else:
    print("✅안전 파일 (safe)✅")




