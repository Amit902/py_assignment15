#Q.1- Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
#desired_output = [('zuck26', 'facebook', 'com'),
#                 ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]


import re

email1="zuck26@facebook.com"
email2="page33@google.com"
email3="jeff42@amazon.com"
p=re.compile(r"([a-zA-Z0-9._]+)@([a-zA_Z]+).([a-z)]+)")

def display(email):
    # print (results)
    result = p.match(email)

    print(result)
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))

display(email1)
display(email2)
display(email3)
print("\n")


#Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter,
# So she bought some better butter, To make the bitter butter better."
# with ‘b’ or ‘B’ from the following text.

#import re

text="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
p=re.compile(r"([bB][a-zA-Z]+)")
result=p.findall(text)
#print(text)

for text in result:
    print(text)
print("\n")


#Q.3- Split the following irregular sentence into words
#sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence"

import re

sen="A, very very; irregular_sentence"
res=re.sub(r"[^a-zA-Z]"," ",sen)
print(res)
print("\n")


#Optional Question
#Q.4- Clean up the following tweet so that it contains only the user’s message.
# That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently
#            if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# desired_output = 'Good advice What I would do differently if I was learning to code today'


import re

tweets="Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"

p=re.compile(r"(.+)! RT (.+): (.+) http(.+)")
res=p.findall(tweets)
print(res[0][0],res[0][2])
print("\n")