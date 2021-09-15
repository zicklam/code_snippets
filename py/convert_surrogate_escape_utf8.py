#!/usr/bin/env python3

"""
Simple convert an surrogate escaped strings into readable utf-8 string:
Example JSON input with "\udcc3\udca4" correctly encode to "ä"
"""

import json
JSON = json.loads('{"element":"\udcc3\udca4\udcc3\udcb6\udcc3\udcbc\udcc3\udc9c\udcc3\udc84\udcc3\udc96\udcc3\udc9f"}')

print(JSON.get('element').encode('utf-8','surrogateescape').decode('utf-8'))
