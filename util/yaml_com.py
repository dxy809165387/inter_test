import yaml
import os


def read_yaml(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='gbk') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    else:
        raise FileNotFoundError('文件不存在')


def write_yaml(file_path, data: dict):
    if os.path.exists(file_path):
        with open(file_path, 'a', encoding='gbk') as f:
            yaml.dump(data, f, allow_unicode=True)
    else:
        raise FileNotFoundError('文件不存在')


def clean_yaml(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'w', encoding='gbk') as f:
            f.truncate()
    else:
        raise FileNotFoundError('文件不存在')


if __name__ == '__main__':
    data_dict = clean_yaml('../case_yaml/cach.yaml')

