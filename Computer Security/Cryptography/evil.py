#!/usr/bin/python3
# coding: latin-1
blob = """ """
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())