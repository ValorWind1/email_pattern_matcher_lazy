import pyperclip
import re

email_regular_expressions = re.compile('''([a-zA-Z0-9. %+-]+@[a-zA-ZA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''',re.VERBOSE)

msg = str(pyperclip.paste())
pattern_matches = []

for i in email_regular_expressions.findall(msg):
    pattern_matches.append(i[0])

if len(pattern_matches) >0:
    pyperclip.copy("\n".join(pattern_matches))
    print("The copy from clipboard was Succesful!")
    print("\n".join((pattern_matches)))
else:
    print("No Email addresses found.")