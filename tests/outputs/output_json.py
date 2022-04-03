# -*- coding: utf-8 -*-

"""Expected results constants."""

RIGHT_JSON = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

WRONG_JSON_1 = '{- follow: False host: hexlet.io - proxy: 123.234.53.22'
WRONG_JSON_2 = '- timeout: 50 + timeout: 20 + verbose: True}'
WRONG_JSON = WRONG_JSON_1 + WRONG_JSON_2

WRONG1_JSON = '''{
  - follow: False
  - proxy: 123.234.53.22
  - timeout: 50
    host: hexlet.io
  + timeout: 20
  + verbose: True
}'''
