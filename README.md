# Python Data Helper

[![Testing](https://github.com/rabiloo/python-data-helper/actions/workflows/test.yml/badge.svg)](https://github.com/rabiloo/python-data-helper/actions/workflows/test.yml)
[![Latest Version](https://img.shields.io/pypi/v/datas-helper.svg)](https://pypi.org/project/datas-helper)
[![Downloads](https://img.shields.io/pypi/dm/datas-helper.svg)](https://pypi.org/project/datas-helper)
[![Pypi Status](https://img.shields.io/pypi/status/datas-helper.svg)](https://pypi.org/project/datas-helper)
[![Python Versions](https://img.shields.io/pypi/pyversions/datas-helper.svg)](https://pypi.org/project/datas-helper)

## About Data Helper

[Data Helper](https://github.com/rabiloo/python-data-helper) is a set of support functions when dealing with files

## Install

```
$ pip install data-helper
```

## Usage

```
from data_helper import file 
from data_helper import path 
from data_helper import image 
from data_helper import compare_content 

print(compare_content.compare_file(src_file, dest_file))

for line in text_line_reader(file_path):
    print(line)
```

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Please see [CONTRIBUTING](.github/CONTRIBUTING.md) for details.

## Security Vulnerabilities

Please review [our security policy](../../security/policy) on how to report security vulnerabilities.

## Credits

- [Dao Quang Duy](https://github.com/duydq12)
- [All Contributors](../../contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
