import pytest

from data_helper import path


@pytest.mark.parametrize(
    "directory,file_path,expected",
    (
        ("/tmp/abcd", "/tmp/abcd/def.jpg", "def.jpg"),
        ("/tmp/abcdr", "/tmp/abcd/def.jpg", "../abcd/def.jpg"),
    ),
)
def test_get_relative_path(directory: str, file_path: str, expected: str):
    assert path.get_relative_path(directory, file_path) == expected


@pytest.mark.parametrize(
    "file_path,expected",
    (
        ("/tmp/abcd/def.jpg/", "/tmp/abcd/def.jpg"),
        ("/tmp//abcd//def.jpg", "/tmp/abcd/def.jpg"),
    ),
)
def test_normalize_path(file_path: str, expected: str):
    assert path.normalize_path(file_path) == expected


@pytest.mark.parametrize(
    "file_path,expected",
    (("/tmp/abcd/def.jpg", "/tmp/abcd/def"),),
)
def test_removesuffix_path(file_path: str, expected: str):
    assert path.removesuffix_path(file_path) == expected


@pytest.mark.parametrize(
    "file_path,expected",
    (("/tmp/abcd/def.jpg", "/tmp/abcd"),),
)
def test_get_dirname(file_path: str, expected: str):
    assert path.get_dirname(file_path) == expected


@pytest.mark.parametrize(
    "file_path,expected",
    (("/tmp/abcd/def.jpg", "def.jpg"),),
)
def test_get_filename(file_path: str, expected: str):
    assert path.get_filename(file_path) == expected
