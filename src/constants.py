import sys

MAX_VALUE = sys.maxsize
MIN_VALUE = -1 * sys.maxsize

help = '''   
script.lua : an example script with help text and a test suite
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = all
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
'''
egs = dict()

options =  dict()