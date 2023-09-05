import re

txt = "I love teach python."
match = re.match("i love", txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
print(txt[start:end])

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search("first", txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
print(txt[start:end])


match = re.findall("language", txt, re.I)
print(match)

match = re.findall("python|Python", txt)
print(match)

match = re.findall("[pP]ython", txt)
print(match)

match_replaced = re.sub('Python|python', 'JavaScript', txt, )
# JavaScript is the most beautiful language that a human being has ever created.
print(match_replaced)
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, )
# JavaScript is the most beautiful language that a human being has ever created.
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

match_replaced = re.sub("%", "", txt)
print(match_replaced)

print(re.split("\n", match_replaced))


regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']


regex_pattern = r'\d+'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
# ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
print(matches)

# this square bracket means a and . means any character except new line
regex_pattern = r'[a].'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']


txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4,}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
# ^ in set character means negation, not A to Z, not a to z, no space
regex_pattern = r'[^A-Za-z ]+'
matches = re.findall(regex_pattern, txt)
print(matches)
