#!/usr/bin/env python
# console.py

import sys
import ujson
from pprint import pprint


def main():
    with open(sys.argv[1]) as f:
        jsontxt = f.read()

    data = ujson.loads(jsontxt)
    pprint(data)

