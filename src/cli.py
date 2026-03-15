## CLI 예측 프로그램

import pickle
import sys
import numpy as np
import pandas as pd

# 학습된 모델 불러오기
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# 입력받는 인자값 받기
if len(sys.argv) != 4:
    print("사용법(input file information) : ")
    print("python cli.py <size> <has_exe> <download_count>")
    sys.exit()

size = int(sys.argv[1])
has_exe = int(sys.argv[2])
download_count = int(sys.argv[3])

# 입력받는 인자값을 배열로 저장
data = np.array([[size, has_exe, download_count]])

#모델 예측
prediction = model.predict(data)

if prediction[0] == 1:
    print("⚠️ Malware detected⚠️")
else:
    print("✅ safe file✅")