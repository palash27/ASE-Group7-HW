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
