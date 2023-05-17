import os, sys
try:
    __import__("FREE").main()
except Exception as e:
    exit(str(e))
