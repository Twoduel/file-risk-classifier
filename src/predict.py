## 새 파일 예측 (저장된 모델 사용)

from sklearn.linear_model import LogisticRegression
from utils import load_data

import pickle
import sys
import pandas as pd

# 학습된 모델 불러오기
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

features, labels = load_data()

model = LogisticRegression()

model.fit(features, labels)

new_file = pd.DataFrame(
    [[1500, 1, 700]],
    columns=["size", "has_exe", "download_count"]
)
prediction = model.predict(new_file)

if prediction[0] == 1:
    print("⚠️ 위험 파일 (malware)⚠️")
else:
    print("✅ 안전 파일 (safe)✅")

