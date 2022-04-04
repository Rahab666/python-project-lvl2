# -*- coding: utf-8 -*-

"""Expected results constants."""

RIGHT_YAML = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

WRONG_YAML_1 = '{- follow: False host: hexlet.io - proxy: 123.234.53.22'
WRONG_YAML_2 = '- timeout: 50 + timeout: 20 + verbose: True}'
WRONG_YAML = WRONG_YAML_1 + WRONG_YAML_2

WRONG1_YAML = '''{
  - follow: False
  - proxy: 123.234.53.22
  - timeout: 50
    host: hexlet.io
  + timeout: 20
  + verbose: True
}'''
