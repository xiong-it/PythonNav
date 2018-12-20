# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('UTF8')

__author__ = 'Haobin'

import logging

class LevelFilter(logging.Filter):
    def __init__(self, name):
        self.name = name

    def filter(self, record):
        return record.levelname == self.name
