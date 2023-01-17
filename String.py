class String:
    def fmt(self, *sControl):
        return print(sControl)

    def oo(self, t):
        print(self.o(t))
        return t

    # def o(self, t, isKeys, fun):
    #     if not isinstance(t, str):
    #         return str(t)
    #     fun = lambda k, v: if not isinstance(k, str):