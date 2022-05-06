"""
    Prompt: Get the number of students with multiple subscriptions.
"""
if __name__ == "__main__":
    subscriptions = int(input())
    english = set(map(int, input().split(" ")))
    subscriptions += int(input())
    french = set(map(int, input().split(" ")))
    
    # C = A & B
    common1 = english.intersection(french)
    common2 = french.intersection(english)
    common3 = common1.intersection(common2)
    print(len(common3))