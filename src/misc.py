import math 
import re
import sys


#Numerics
help = """   
script.lua : an example script with help text and a test suite
(c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
ACTIONS:
  -g  the	show settings
  -g  rand	generate, reset, regenerate same
  -g  sym	check syms
  -g  num	check nums
"""


def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def rand(lo, hi, Seed):
    lo, hi = lo or 0, hi or 1
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces=3):
    mult = 10 ** (nPlaces)
    return math.floor(n * mult + 0.5) / mult

#Lists

#strings

def coerce(s):
    def fun(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return False
        else:
            return s1
    if s.isnumeric():
        return int(s)
    elif type(s) != bool:
        return fun(re.search('^[\s]*[\S+]*[\s]*$', s).group(0))



def oo(t):
    print(o(t))
    return t

def o(t):
    keys = list(t.keys())
    keys = sorted(keys)
    sorted_t = {i: t[i] for i in keys }
    output = "{"
    for k, v in sorted_t.items():
        output = output + ":"+str(k) + " " + str(v) + " "
    output = output + "}"
    return output

def settings(s):
    t = {}
    for k,v in re.findall("[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", s): 
        t[k] = coerce(v)
    return t

def cli(command_line_args):
    options = {}
    options = settings(help)
    for k, v in options.items():
        v = str(v)
        for n, x in enumerate(command_line_args):
            if x == '-'+k[0] or x == '--'+k:
                if v == "true":
                    v = "false"
                elif v == "false":
                    v = "true"
                else:
                    v = command_line_args[n+1]
        options[k] = coerce(v)

    return options

