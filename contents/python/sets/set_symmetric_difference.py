"""
    Prompt: Get the number of students with English or French subscriptions only.
"""
if __name__ == "__main__":
    subscriptions = int(input())
    english = set(map(int, input().split(" ")))
    subscriptions += int(input())
    french = set(map(int, input().split(" ")))
    
    # C = A ^ B
    diff = english.symmetric_difference(french)
    print(len(diff))