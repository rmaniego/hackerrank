"""
    Prompt: Get total score of a sentence.
    
    1 point per word and another point per word
    if it contains with even vowels.
"""

def score_words(words):
    score = len(words)
    for word in words:
        num_vowels = len([x for x in word if x in "aeiouy"])
        if (num_vowels % 2) == 0:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))