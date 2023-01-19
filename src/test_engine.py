
from Sym import *
from Num import *
from misc import *
import random

egs = {}
def eg(key, str, fun):
    egs[key] = fun

def SYM(the):
    sym = Sym()
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    if "a" == sym.mid() and 1.379 == rnd(sym.div()):
        return True
    else:
        return False

def NUM(the):
    num = Num()
    for x in [1,1,1,1,2,2,3]:
        num.add(x)
    if 11/7 == num.mid() and 0.787 == rnd(num.div()):
        return True
    else:
        return False

def THE(the):
    oo(the)

def RAND(the):
    num1  = Num()
    num2 = Num()
    random.seed = the["seed"]
    for _ in range(1, (10**3)):
        num1.add(rand(0, 1, the["seed"]))
    random.seed = the["seed"]
    for _ in range(1, (10**3)):
        num2.add(rand(0, 1, the["seed"]))
    m1 = rnd(num1.mid(), 10)
    m2 = rnd(num2.mid(), 10)
    # print(m1)
    # print(m2)
    # print(rnd(m1,1))
    if m1 == m2 and .6  == rnd(m1, 1):
        return True
    else:
        return False

eg("sym", "check syms", SYM)
eg("num", "check nums", NUM)
eg("the", "show settings", THE)
eg("rand", "generate, reset, regenerate same", RAND)



def test(the):
    fails = 0
    for what, fun in egs.items():
        if the['go'] == "all" or what == the['go']:
            random.seed = the["seed"]
            if egs[what] == "SYM" or egs[what] == "NUM":
                if egs[what]() == False:
                    fails += 1
                    print("❌ fail:",what)
                else:
                    print("✅ pass:",what) 
            else:
                if egs[what](the) == False:
                    fails += 1
                    print("❌ fail:",what)
                else:
                    print("✅ pass:",what)  

