import os

from glob import glob

from lmdbsystem.lmdb import Lmdb
from lmdbsystem.read_adapters.text import TextReadAdapter
from tqdm import tqdm

from .path import get_relative_path


def compare_txt_lmdb_file(src_file, dest_file):
    src_adapter = TextReadAdapter(path=src_file)
    dest_adapter = TextReadAdapter(path=dest_file)

    if src_adapter.length != dest_adapter.length:
        raise ValueError(
            f"Number key of source {os.path.basename(src_file)}: {src_adapter.length} "
            f"different "
            f"Number key of destination {os.path.basename(dest_file)}: {dest_adapter.length}"
        )

    src_lmdb = Lmdb(adapter=src_adapter)
    dest_lmdb = Lmdb(adapter=dest_adapter)
    for i, key in enumerate(tqdm(src_adapter.keys)):
        src_value = src_lmdb.read_key(key)
        dest_value = dest_lmdb.read_key(dest_adapter.keys[i])
        if src_value != dest_value:
            raise ValueError(
                f"Content of source {src_file}: {src_value} "
                f"different"
                f"Content of destination {dest_file}: {dest_value}"
            )


def compare_file(src_file, dest_file):
    content_src = open(src_file, "r").read()
    content_dest = open(dest_file, "r").read()
    if content_src != content_dest:
        print(
            f"Content of source {src_file}: {content_src[:50]} "
            f"different"
            f"Content of destination {dest_file}: {content_dest[:50]}"
        )


def compare_folder(src_dir, dest_dir, suffix):
    path_dest_misses = []
    content_dest_misses = []
    content_src_misses = []
    list_src = sorted(glob(f"{src_dir}/**/*{suffix}", recursive=True))

    for i, path_src in tqdm(enumerate(list_src)):
        relative_path = get_relative_path(src_dir, path_src)
        path_dest = os.path.join(dest_dir, relative_path)

        if not os.path.isfile(path_dest):
            if open(path_src, "r").read() != "{}":
                path_dest_misses.append(path_dest)
                print(
                    f"Not found destination file {path_dest}\n"
                    f"source file has value: {open(path_src, 'r').read()[:50]}"
                )
            continue

        content_src = open(path_src, "r").read()
        content_dest = open(path_dest, "r").read()
        if content_src != content_dest:
            if content_dest.strip() == "{}":
                content_dest_misses.append(path_dest)

            if content_src.strip() == "{}":
                content_src_misses.append(path_src)
            print(
                f"Content of source {path_src}: {content_src[:50]} "
                f"different\n"
                f"Content of destination {path_dest}: {content_dest[:50]}"
            )

    print("PATH DESTINATION MISSES", path_dest_misses)
    print("############################")
    print("PATH SOURCE MISSES", content_src_misses)
    print("############################")
    print("CONTENT DESTINATION MISSES", content_dest_misses)
