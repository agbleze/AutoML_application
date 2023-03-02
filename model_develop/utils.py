
import os


def get_path(folder_name: str, file_name: str):
    dirpath = os.getcwd()
    filepath = f'{dirpath}/{folder_name}/{file_name}'
    return filepath

