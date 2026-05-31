import os

import yaml


#yaml文件读取
def read_yaml(file_path):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    real_file_path = os.path.normpath(os.path.join(base_dir, file_path))
    with open(real_file_path, mode="r",encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data

#yaml文件写入
def write_yaml(file_path, data):
    with open(file_path, mode="a+",encoding="utf-8") as f:
        yaml.dump(data, f)

#yaml文件清空
def clear_yaml(file_path):
    with open(file_path, mode="w",encoding="utf-8") as f:
        f.truncate()

if __name__ == "__main__":
    print(read_yaml("../data/test_student_login.yaml"))