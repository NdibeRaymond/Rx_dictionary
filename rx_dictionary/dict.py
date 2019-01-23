import json
from difflib import get_close_matches as match
x = input("please what is your name? ")
rxdic = json.load(open("076 data.json","r"))
dic_keys = rxdic.keys()

def xxx(query):
    query = query.lower()
    if query == "exit123":
        exit()
    try:
        if type(rxdic[query]) == list:
            for each_ans in rxdic[query]:
                print(each_ans)
        else:
            print(rxdic[query])
    except:
        matches = match(query,dic_keys,n = 3)
        for word in matches:
            inpt = input("do you mean "+word+"?, (y or n): " )
            if inpt.lower() == "y":
                if type(rxdic[word]) == list:
                    for each_ans in rxdic[word]:
                        print(each_ans)
                else:
                    print(rxdic[word])
                return
        print("sorry, word doesn't exist in this dictionary. check and try again senor")

while(1):
    xxx(input(x+" input a word : "))
