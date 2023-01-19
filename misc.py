import math 
import re


Seed=937162211

def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def rand(lo, hi):
    lo, hi = lo or 0, hi or 1
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces):
    mult = 10 ** (nPlaces or 3)
    return math.floor(n * mult + 0.5) / mult

def map(t,fun):
    u = {}
    for k,v in t.items():
        v,k = fun(v)
        u[k or (1 + len(u))] = v
    return u

def kap(t,fun):
    u = {}
    for k,v in t.items():
        v,k = fun(k,v)
        u[k or (1 + len(u))] = v
    return u

def sort(t, fun=None):
    if fun is None:
        fun = lambda x: x[0]
    tmp = sorted(t.items(), key=fun)
    t = dict(tmp)
    return t

def keys(t):
    sorted_keys = sorted(t.keys())
    res = {}
    for i in range(1,len(sorted_keys)+1):
        res[i] = sorted_keys[i-1]
    return res

def fmt(*sControl):
    return print(sControl)

def oo(t):
    print(o(t))
    return t

# def o(self, t, isKeys):
#     if not isinstance(t, dict):
#         return str(t)
#
#     def fun(k, v):
#         if not re.findall("^_", str(k)):
#             return self.fmt(":%s %s", self.o(k), self.o(v))
#         else:
#             return None
#     fun = fun()
#
#     return "{" + len(t) > 0 and not isKeys and Lists.map(t, self.o) or Lists.sort(Lists.kap(t, fun)) + " }"

def coerce(s):

    def fun(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return False
        return s1

    return int(s) or float(s) or fun(re.match("^%s*(.-)%s*$", s))
