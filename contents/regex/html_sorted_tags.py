import re

elements = [
           '< p><br/><h6></h6 ><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p><div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>' 
        ]

# Enter your code here. Read input from STDIN. Print output to STDOUT
tags = set()
pattern_tags = r'(?<=<)(\s*)(\w{1,})([1-6]*)'
for element in elements:
    matches = re.findall(pattern_tags, element)
    for match in matches:
        tag = [tag.strip() for tag in match if tag.strip() != ""][0]
        tags.add(tag)
print(";".join(sorted(tags)))