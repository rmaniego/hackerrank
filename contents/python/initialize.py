import os
from maguro import Maguro

template = """\n
if __name__ == "__main__":
    pass
"""

topics = ["Introduction", "Basic Data Types", "Strings", "Sets", "Math", "Itertools", "Collections", "Date and Time", "Errors and Exceptions", "Classes", "Built-Ins", "Python Functionals", "Regex and Parsing", "XML", "Closures and Decorators", "Numpy", "Debugging"]

for topic in topics:
    filepath = topic.replace(" ", "_").lower()
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    if not os.path.isfile(f"{filepath}/template.py"):
        with open(f"{filepath}/template.py", "w+") as f:
            f.write(template)