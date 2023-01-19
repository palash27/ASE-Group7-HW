import String
import re

class Main:
    def cli(self, options):
        for k, v in options.items():
            v = str(v)
            for n, x in options.items():
                if x == "-"+re.sub(1, 1, k) or x == "--"+k:
                    v = v == "false" and "true" or v == "true" and "false" or options[n+1]
            options[k] = String.coerce(v)
        return options

    # def settings(self, s):
    #     t = {}
    #     re.sub('\n[%s]+[-][%S]+[%s]+[-][-]([%S]+)[^\n]+= ([%S]+)',lambda k,v: t[k]= String.coerce(v), s)