"""
    Prompt: Get the top 3 characters with most occurrence,
            with similar occurrences listed alphabetically.
"""

if __name__ == "__main__":
    letters = {}
    for letter in input():
        letters[letter] = letters.get(letter, 0) + 1
    
    occurrences = {}
    for key, value in letters.items():
        occurrences[value] = occurrences.get(value, []) + [key]

    count = 0
    for occurrence in sorted(occurrences.keys(), reverse=True):
        for letter in sorted(occurrences[occurrence]):
            print(letter, occurrence)
            count += 1
            if count == 3:
                break
        if count == 3:
            break