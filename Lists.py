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