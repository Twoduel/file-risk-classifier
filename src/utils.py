## 데이터 로딩 등 공통 코드 파일

import pandas as pd

def load_data():
    data = pd.read_csv("data/file_data.csv")

    featuers = data.drop("label", axis=1)

    labels = data["label"].map({
        "safe": 0,
        "malware": 1
    })

    return featuers, labels
 