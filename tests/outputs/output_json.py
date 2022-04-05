# -*- coding: utf-8 -*-

"""Expected results constants."""

RIGHT = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

WRONG1_1 = '{- follow: False host: hexlet.io - proxy: 123.234.53.22'
WRONG1_2 = '- timeout: 50 + timeout: 20 + verbose: True}'
WRONG1 = WRONG1_1 + WRONG1_2

WRONG2 = '''{
  - follow: False
  - proxy: 123.234.53.22
  - timeout: 50
    host: hexlet.io
  + timeout: 20
  + verbose: True
}'''

RIGHT1 = {"host": "hexlet.io",
          "timeout": 50,
          "proxy": "123.234.53.22",
          "follow": False
          }
