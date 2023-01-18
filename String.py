import re

class String:
    def fmt(self, *sControl):
        return print(sControl)

    def oo(self, t):
        print(self.o(t))
        return t

    # def o(self, t, isKeys, fun):
    #     if not isinstance(t, str):
    #         return str(t)
    #     def fun(k, v):
    #         if not isinstance(k, str):

    def coerce(self, s):
        def fun(s1):
            if s1 == "true":
                return True
            elif s1 == "false":
                return False
            return s1
        return int(s) or float(s) or fun(re.match("^%s*(.-)%s*$", s))