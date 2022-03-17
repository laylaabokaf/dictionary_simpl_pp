import json
from difflib import get_close_matches

def try_again(word,data):
    decide = input("press y for yes or n for no")
    decide = decide.lower()
    decide = decide.strip()
    if decide == "y":
        for defin in data[get_close_matches(word, data.keys())[0]]:
            print("' " + defin + " '\n")
    elif decide == "n":
         print("sorry we didn't find a definition for " + word + " try another one \n")
    else:
         print("You have entered wrong input ")
         try_again(word,data)


def Search_and_get_Difnition(word,data):
    if word in data:
        for defin in data[word] :
          print("' " + defin + " '\n")
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead" % get_close_matches(word, data.keys())[0])
        try_again(word,data)
    else:
        print("sorry we didn't find a definition for " + word + " try another one \n")




f = open("data.json", "r")
data = json.load(f)

while(True):
    word =  input("write a word to get definition or 0 to exit the program \n")
    word = word.lower()
    word = word.strip()
    if(word == "0"):
        break
    word_isalpha = word.replace(" ","")
    bool3 = word_isalpha.isalpha()
    bool(bool3)
    if (bool3 == False):
        print("write just letters, try again ")
    else :
        Search_and_get_Difnition(word,data)


f.close()