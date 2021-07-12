#! python3

import pyperclip, re

# regex phone numbers
# pattern match 415-555-000, 555-0000, (415) 555-000, 555-000 ext 12345, ext. 12345, x12345
phone_regex = re.compile(r'''(
    ((\d\d\d)|(\(\d\d\d\)))?            # area code
    (\s|-)                              # separator
     \d\d\d                             # first 3 digits
     -                                  # separator
    \d\d\d\d                            # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
    )''', re.VERBOSE)

# regex emails
email_regex = re.compile(r'''
    [a-zA-Z0-9_.+]+                     # username
    @                                   # @ symbol
    [a-zA-Z0-9_.+]+                     # domain name
    ''', re.VERBOSE)
# get text from clipboard
text = pyperclip.paste()

# get phone numbers and emails off of clipboard
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []
for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])

# copy the extracted email/phone to the clipboard
results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)


