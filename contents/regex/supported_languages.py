# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

supported = """12345 JAVA
12345 ABC
12345 PYTHON"""
pattern = r'\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'

# for _ in range(int(input())):
for language in supported.split("\n"):
    print(re.findall(pattern, language))
    if len(re.findall(pattern, language)):
        print("VALID")
    else:
        print("INVALID")