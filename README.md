# File Risk Classification System
| Machine Learning project that predicts whether a file is malware based on file features.


## 프로젝트 소개

파일의 기본 정보를 기반으로 위험 파일(malware) 여부를 분류하는 간단한 머신러닝 기반 파일 분류 시스템 입니다.

파일 크기, 실행 파일 여부, 다운로드 횟수를 feature로 사용하여 Logistic Regression 모델을 학습하고 
새로운 파일의 위험도를 시스템이 자동으로 예측할 수 있도록 구현했습니다.



## 프로젝트 구조

file-risk-classifier
│
├─ data
│   └─ file_data.csv
│
├─ src
│   ├─ train.py
│   ├─ predict.py
│   └─ utils.py
│
└─ README.md



## 데이터 설명
|     Feature    |                설명                  |
|----------------|--------------------------------------|
|      size      |             파일 크기 (KB)            |
|     has_exe    | 실행 파일 여부 (1: exe 존재 / 0: 없음) |
| download_count |             다운로드 횟수             |
|      label     |       파일 분류 (safe / malware)      |



## Tech Stack
- Python
- Pandas
- Scikit-learn



## 모델 학습

Logistic Regression 모델을 사용하여 파일 정보를 기반으로 위험 파일 여부를 분류하도록 학습했습니다.

Train / Test 데이터를 분리하여 모델 성능을 평가했습니다.



## 실행 방법
# 모델 학습
python src/train.py

# 파일 위험도 예측
python src/predict.py
