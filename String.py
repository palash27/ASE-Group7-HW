import re
import Lists


class String:
    def fmt(self, *sControl):
        return print(sControl)

    def oo(self, t):
        print(self.o(t))
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

    def coerce(self, s):

        def fun(s1):
            if s1 == "true":
                return True
            elif s1 == "false":
                return False
            return s1

        return int(s) or float(s) or fun(re.match("^%s*(.-)%s*$", s))
