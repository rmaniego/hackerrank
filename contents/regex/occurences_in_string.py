import re

sentences = [
                "lilikoi li lili_-likoikoili,li(li+lilikoi)lilikoi",
                "alien,aleles licorice kokopi (loko)koko_lipsum"
            ]
substrings = ["li", "koi"]

# sentence = input()
# substring = input()
for substring in substrings:
    count = 0
    for sentence in sentences:
        pattern = fr"(?<!^)(?<! )(?<!\W){substring}(?!\W)(?! )(?!$)"
        matches = re.findall(pattern, sentence)
        count += len([x.strip() for x in matches if x.strip() != ""])
    print(count)