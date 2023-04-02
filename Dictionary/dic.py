import json
# data="hi"
from difflib import get_close_matches
data=json.load(open("data.json"))

def dictionary(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.title()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean this %s word "%get_close_matches(word,data.keys())[0])
        decide=input("If Above word right Enter 'y' otherwise 'n' :")
        if decide=='y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "Invalid word"
    else:
        return "Invalid word"




word=input("Enter the word:")
output=dictionary(word)
if type(output)== list:
    for i in output:
        print(i)
else:
    print(output)
