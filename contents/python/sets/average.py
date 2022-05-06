"""
    Prompt: Get the average of the set,
            then format with 3 decimal places.
"""
def average(array):
    arr = set(array)
    avg = sum(arr) / len(arr)
    return f"{avg:.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)