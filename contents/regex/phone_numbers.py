import re

numbers = ["1 877 2638277", "91-011-23413627", "1000--abc"]

# for _ in range(int(input())):
for number in numbers:
    # number = input()
    pattern = r"^(\d{1,3})(?:\ )(\d{1,3})(?:\ )(\d{6,10})|(\d{1,3})(?:\-)(\d{1,3})(?:\-)(\d{6,10})$"
    for matches in re.findall(pattern, number):
        codes = [x.strip() for x in matches if x.strip() != ""]
        print(f"CountryCode={codes[0]},LocalAreaCode={codes[1]},Number={codes[2]}")