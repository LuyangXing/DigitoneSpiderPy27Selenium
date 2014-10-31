#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'luyang'
__Email__ = 'Leon.LuyangXing@gmail.com'

import os, random, string


def gen_pass():
    foo = random.SystemRandom()
    print foo

    length = 64
    chars = string.letters + string.digits
    print foo.choice(string.digits)

    return ''.join(foo.choice(chars) for i in xrange(length))

print gen_pass()

