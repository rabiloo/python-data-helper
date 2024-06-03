import os


def get_relative_path(directory: str, file_path: str):
    file_name = os.path.relpath(file_path, directory)
    return file_name


def normalize_path(file_path: str):
    return os.path.normpath(file_path)


def removesuffix_path(file_path: str):
    return file_path.rsplit(".", 1)[0]


def get_dirname(file_path: str):
    return os.path.dirname(file_path)


def get_filename(file_path: str):
    return os.path.basename(file_path)
