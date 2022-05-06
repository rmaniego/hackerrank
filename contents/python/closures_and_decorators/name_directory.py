"""
    Prompt: Sort directory based on numerical order of age.
"""

from operator import itemgetter

def person_lister(f):
    def inner(people):
        # Cast age to integer to get appropriate sorting.
        people = [[people[i][0], people[i][1], int(people[i][2]), people[i][3]] for i in range(len(people))]
        return [f(person) for person in list(sorted(people, key=itemgetter(2)))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')