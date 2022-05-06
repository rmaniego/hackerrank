"""
    Prompt: Get the number of unique subscriptions.
"""
if __name__ == "__main__":
    subscriptions = int(input())
    english = set(map(int, input().split(" ")))
    subscriptions += int(input())
    french = set(map(int, input().split(" ")))
    
    # C = A | B, fix below
    english.union(french)
    unique = french - english
    students = len(english) + len(unique)
    print(students)