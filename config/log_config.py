import logging
import os

#日志目录
log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
os.makedirs(log_path, exist_ok=True)

#获取root logger并配置
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# 清空已有的handler，避免重复输出
root_logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)

file_handler = logging.FileHandler(
    os.path.join(log_path, "student_test.log"),
    mode='w',
    encoding="utf-8"
)
file_handler.setFormatter(formatter)
root_logger.addHandler(file_handler)


def get_test_logger(name="test"):
    return logging.getLogger(name)
