import re

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phone_regex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo.group())
