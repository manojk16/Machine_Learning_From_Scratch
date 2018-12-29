import json
from difflib import get_close_matches

data =json.load(open("data.json"))

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    #print(w)
    if w in data:
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead Enter Y/N ?" %get_close_matches(w,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]

        elif yn=="n":

            return "The word does not exist Please double check"

        else:
            return "I didn't Understand your input "
    else:
        return "The word does not exist Please double check"
word=input("Enter the word\n")

#print(translate(word)) # Out put is like

output=translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)