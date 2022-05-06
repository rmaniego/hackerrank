"""
    Prompt: Validate string s.
"""
import re

if __name__ == "__main__":    
    s = input()
    
    print(bool(len(re.findall(r'[a-zA-Z0-9]+', s))))
    print(bool(len(re.findall(r'[a-zA-Z]+', s))))
    print(bool(len(re.findall(r'[0-9]+', s))))
    print(bool(len(re.findall(r'[a-z]+', s))))
    print(bool(len(re.findall(r'[A-Z]+', s))))