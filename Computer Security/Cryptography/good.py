#!/usr/bin/python3
# coding: latin-1
blob = """AAAAAAAAAAAAAAA®i}Æ|TVãL¥¬¿@Ú?`è,:@ð¥/"nxÍª/¥úò¤ãPc¿YÏH3èeYúN$sL7¡f{¨äÅfîùÃ>Íð˜’5`IÅúTMtuæ>jÑ~Íìþñ¸{¦Êÿ=j"M—ÈÄåè[¢Z±›u§Íë.Ì¤û"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())