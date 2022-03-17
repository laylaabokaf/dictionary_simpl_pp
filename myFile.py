import json



def Search_and_get_Difnition(word,data):
    definition = ""
    for item in data :
        if(item == word):
            definition = data[item][0]
            break
    if(definition == ""):
       print("sorry we didn't find a definition for " + word + " try another one \n")
    else:
       print("' " + definition +" '\n")



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