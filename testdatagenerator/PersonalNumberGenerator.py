#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from testdatagenerator import Utilities


class PersonalNumberGenerator:
    def __init__(self):
        pass

    def pnr(self):
        year = str(randint(0, 99))
        month = str(randint(1, 12))
        day = str(randint(1, 28))
        pnr = year.zfill(2) + month.zfill(2) + day.zfill(2) + "-"
        pnr += str(randint(0, 999)).zfill(3)

        luhn = Utilities.luhn(pnr)

        pnr = ("19" if int(year) > 18 else "20") + pnr
        return pnr + str(luhn)

    def generator(self):
        return self.pnr()
