#!/usr/bin/python3

import sys
import pymd5
from urllib.parse import quote, urlparse
from pymd5 import md5, padding
from pymd5 import md5, md5_compress




##########################
# Example URL parsing code:
res = urlparse('https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

    #################################
    # Your length extension code here

res1 = urlparse(url)
newCommand = "&command=UnlockSafes"
commands = quote(newCommand)

URLcommands = res1.query[39:]


token = res1.query[6:38]

msg_padding = padding(((len(URLcommands)+8)*8))
bits = ((len(URLcommands) + len(msg_padding))+8) * 8 
# padded_msg = commands + str(bits)

hash = md5(state=bytes.fromhex(token), count=bits)
hash.update(newCommand)

# hash = md5(state=bytes.fromhex(token), count=bits)
# padded_msg = padding(bits)
# print(padded_msg)
# md5_compress(token, padded_msg)
# hash.md5(compressed_msg).hexdigest()
# print(hash.hexdigest())

finalURL = url[0:67] + hash.hexdigest() + "&" + URLcommands + quote(msg_padding) + newCommand
print(finalURL)



