import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    if word in data: 
    	return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        while True :
            answer=input("Did you mean " + get_close_matches(word,data.keys())[0] +" please answer yes or no :").lower()
            if answer == "yes":
                word = get_close_matches(word,data.keys())[0]
                return data[word]
                break
            elif answer == "no":
                word = input("Enter the word again : ").lower()
                return translate(word)
    else:
        print("OH sorry.. but this word doesn't exist in our dictionary !! \nPlease try again '-' ")
        word = input("Enter the word : ").lower()
        return translate(word)
    
word = input("Enter a  word: ").lower()
output = translate(word)
print(output)
