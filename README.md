[![Python CI](https://github.com/sudobooo/python-project-lvl2/actions/workflows/pyci.yml/badge.svg)](https://github.com/sudobooo/python-project-lvl2/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/8fe2be79fbeabd5ced89/maintainability)](https://codeclimate.com/github/sudobooo/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8fe2be79fbeabd5ced89/test_coverage)](https://codeclimate.com/github/sudobooo/python-project-lvl2/test_coverage)

# Gendiff

The second project written for the academic purposes of a Hexlet's course on learning a programming language Python.

## About the project

Gendiff is the Difference Generator is a program that looks for differences between two files.

- Suppported formats: YAML, JSON
- The following output formats are available: json, plaind and stylish
- Can be used as CLI tool or library

## How to install and use

### Install
`python3 -m pip install git+https://github.com/sudobooo/python-project-lvl2`

### Use as a library
```
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2, format_name)
print(diff)
```
Default argument for format format_name='stylish'

### Use as a CLI
```
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

## Demonstration of the program

### Asciinema format stylish for flat json files
[![asciicast](https://asciinema.org/a/488127.svg)](https://asciinema.org/a/488127)

### Asciinema format stylish for flat yaml files
[![asciicast](https://asciinema.org/a/488128.svg)](https://asciinema.org/a/488128)

### Asciinema format stylish for json and yaml files has nested structures
[![asciicast](https://asciinema.org/a/488129.svg)](https://asciinema.org/a/488129)

### Asciinema format plain for json and yaml files has nested structures
[![asciicast](https://asciinema.org/a/488131.svg)](https://asciinema.org/a/488131)

### Asciinema format json for json files has nested structures
[![asciicast](https://asciinema.org/a/488135.svg)](https://asciinema.org/a/488135)
