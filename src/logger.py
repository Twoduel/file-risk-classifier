import logging
import os


# logs 폴더 경로
log_path = "logs/system.log"

# logs 폴더 없으면 생성
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 콘솔 출력
logger = logging.getLogger()

# 파일 출력