import csv
import gzip
import hashlib
import json
import os
import pickle
import re
import tarfile
import warnings

from typing import IO, Any, Dict, Generator


def text_reader(path: str) -> str:
    with open(path, "r") as fp:
        return fp.read()


def text_line_reader(path: str) -> Generator[str, Any, None]:
    with open(path, "r") as fp:
        for line in fp:
            line = line.strip()
            if line:
                yield line


def text_writer(path: str, data: str) -> None:
    with open(path, "w") as fwrite:
        fwrite.write(data)


def raw_reader(path: str) -> bytes:
    with open(path, "rb") as fp:
        bin_data = fp.read()
    return bin_data


def csv_line_reader(path: str, delimiter: str, skip_header: bool) -> Generator[Any, Any, None]:
    with open(path, "r") as fp:
        reader = csv.reader(fp, delimiter=delimiter)

        if skip_header:
            next(reader)

        for row in reader:
            yield row


def gzip_text_line_reader(path: str) -> Generator[str, Any, None]:
    with gzip.open(path, "rt") as fp:
        for line in fp:
            line = line.strip()
            if line:
                yield line


def tar_gzip_file_reader(path: str, pattern: str) -> Generator[IO, Any, None]:
    pattern = re.compile(pattern)
    tarf = tarfile.open(path, "r:gz")
    for filename in tarf.getnames():
        if re.search(pattern, filename):
            fp = tarf.extractfile(filename)
            yield fp


def json_reader(path: str) -> Dict[str, Any]:
    with open(path, "r") as fp:
        data = json.load(fp)
    return data


def json_writer(path: str, data: Any, indent=None) -> None:
    with open(path, "w") as fp:
        json.dump(data, fp, indent=indent)


def get_md5_file(path):
    bin_data = raw_reader(path)
    return hashlib.md5(bin_data).hexdigest()


def dump_pickle(obj):
    """
    Serialize an object.

    Returns :
        The pickled representation of the object obj as a bytes object
    """
    return pickle.dumps(obj)


def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
    else:
        warnings.warn(f"{file_path} Not a file")
