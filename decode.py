#!/usr/bin/env python

import email.header, sys

words = email.header.decode_header(sys.stdin.read())
words = [s.decode(c or "utf-8") for (s, c) in words]
print("".join(words))
