## GUI 프로그램 (File Drop & Drag 구조)

import sys
import pickle
import numpy as np
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

# 학습된 모델 load
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

class DropGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Malware File Detector")
        self.setGeometry(100, 100, 300 ,200)

        # 드래그 허용
        self.setAcceptDrops(True)

        self.label = QLabel("Drag & Drop File Here", self)
        self.label.setAlignment(Qt.AlignCenter)

        self.result = QLabel("Result: ", self)
        self.result.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.result)

        self.setLayout(layout)

    # 드래그 이벤트
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    # 드롭 이벤트
    def dropEvent(self, event):
        
        file_path = event.mimeData().urls()[0].toLocalFile()

        if not file_path.endswith(".exe"):
            self.result.setText("Not an executable file")
            return

        # file feature 추출
        size = os.path.getsize(file_path)
        has_exe = 1
        download_count = 100

        data = np.array([[size, has_exe, download_count]])

        prediction = model.predict(data)

        if prediction[0] == 1:
            self.result.setText("⚠️ Malware File Detected⚠️")
        else:
            self.result.setText("✅ Safe file✅")

app = QApplication(sys.argv)

window = DropGUI()
window.show()

sys.exit(app.exec_())