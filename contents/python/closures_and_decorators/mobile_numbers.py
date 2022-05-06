"""
    Prompt: Standardize mobile numbers using a decorator.
"""

from operator import itemgetter

def wrapper(f):
    # `f` is a function that needs to be called
    # using the modified input
    def fun(l):
        for i in range(len(l)):
            s = len(l[i])
            if s == 12:
                l[i] = "+"+l[i]
            elif s == 11 and l[i][0] == "0":
                l[i] = "+91"+l[i][1:]
            elif s == 10:
                l[i] = "+91"+l[i]
            temp = list(l[i])
            temp.insert(3, " ")
            temp.insert(9, " ")
            l[i] = "".join(temp)
        # return function(arg)
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 