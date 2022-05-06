"""
    Prompt: Validate email addresses.
"""

import re


def fun(s):
    return bool(re.findall(r'^[\w\d\-]+@[a-zA-Z\d]+\.[a-zA-Z]{1,3}$', s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)