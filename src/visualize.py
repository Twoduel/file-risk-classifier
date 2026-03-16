## 데이터 시각화

import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv("data/file_data.csv")

os.makedirs("images", exist_ok=True)

# 파일 크기 분포
plt.hist(data["size"])

plt.title("File Size Distribution")
plt.xlabel("File Size")
plt.ylabel("Count")

# 이미지 저장
plt.savefig("images/file_size_distribution.png")

plt.show()
plt.clf()



# 다운로드 수 분포
plt.hist(data["download_count"])

plt.title("Download Count Distribution")
plt.xlabel("Download Count")
plt.ylabel("Count")

plt.savefig("images/dwonload_distribution.png")

plt.show()
plt.clf()



# malware VS. safe 파일 비율
data["label"].value_counts().plot(kind="bar")

plt.title("Malware VS. Safe Files")

plt.savefig("images/malware_ratio.png")

plt.show()