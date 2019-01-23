from tkinter import *
import json
from difflib import get_close_matches as match

rxdic = json.load(open("076 data.json","r")) # Load the dictionary file
dic_keys = rxdic.keys()
count = 0
word = ""


window = Tk() # creates a tkinter object

def dict_main3():
    global rxdic
    global word
    global count
    reply = ent.get()
    if reply.lower() == "y":
        ent.delete(0,END)
        if type(rxdic[word[2]]) == list:
            txt.delete("active",END)# Clears the content of a text-output object
            for each_ans in rxdic[word[2]]:
                txt.insert(END,each_ans)
        else:
            txt.delete("active",END)
            txt.insert(rxdic[word[2]])
        count = 0
        return ()
    elif reply.lower() == "n":
        ent.delete(0,END)
        txt.delete("active",END)
        txt.insert(END,"sorry, word doesn't exist in this dictionary. check and try again senor")
        count = 0
        return ()
    else:
        count = 0
        dict_main() # Recursion

def dict_main2():
    global rxdic
    global count
    global word
    reply = ent.get()
    if reply.lower() == "y":
        ent.delete(0,END)
        if type(rxdic[word[1]]) == list:
            txt.delete("active",END)
            for each_ans in rxdic[word[1]]:
                txt.insert(END,each_ans)
        else:
            txt.delete("active",END)
            txt.insert(rxdic[word[1]])
        count = 0
        return ()
    elif reply.lower() == "n":
        ent.delete(0,END)
        if len(word) == 2:
            txt.delete("active",END)
            txt.insert(END,"sorry, word doesn't exist in this dictionary. check and try again senor")
            count = 0
            return ()
        count += 1
        txt.delete("active",END)
        txt.insert(END,"do you mean "+word[2]+"?, (y or n): " )
        return ()
    else:
        count = 0
        dict_main() # Recursion

def dict_main1():
    global rxdic
    global count
    global word
    reply = ent.get()
    if reply.lower() == "y":
        ent.delete(0,END)
        if type(rxdic[word[0]]) == list:
            txt.delete("active",END)
            for each_ans in rxdic[word[0]]:
                txt.insert(END,each_ans)
        else:
            txt.delete("active",END)
            txt.insert(rxdic[word[0]])
        count = 0
        return ()
    elif reply.lower() == "n":
        ent.delete(0,END)
        if len(word) == 1:
            txt.delete("active",END)
            txt.insert(END,"sorry, word doesn't exist in this dictionary. check and try again senor")
            count = 0
            return ()
        count += 1
        txt.delete("active",END)
        txt.insert(END,"do you mean "+word[1]+"?, (y or n): " )
        return ()
    else:
        count = 0
        dict_main() # Recursion

def dict_main():
###############
#1 Declerations
##############
    global dic_keys
    global rxdic
    global count
    global word
###############
#2 Declerations
##############


###############
#1 this section executes during word surgestions (when you search for an existing word)
###############
    if count == 1:
        dict_main1()
        return ()
    elif count == 2:
        dict_main2()
        return ()
    elif count == 3:
        dict_main3()
        return ()
###############
#2 this section executes during word surgestions (when you search for an existing word)
###############


###############
#1 dict_main main program
##############
    word = ent.get()
    ent.delete(0,END)

#    x = input("please what is your name? ")
#    entry.insert(x)

    word = word.lower() # makes variable lower-case
#    if word == "exit123":
#        exit()
    try:
        if type(rxdic[word]) == list:
            txt.delete("active",END)
            for each_ans in rxdic[word]:
                txt.insert(END,each_ans)
        else:
            txt.delete("active",END)
            txt.insert(END,rxdic[word])
    except:
        word = match(word,dic_keys,n = 3)
        if len(word) == 0:
            txt.delete("active",END)
            txt.insert(END,"sorry, word doesn't exist in this dictionary. check and try again senor")
            return ()
        txt.delete("active",END)
        txt.insert(END,"do you mean "+word[0]+"?, (y or n): " )
        count += 1
###############
#2 dict_main main program
##############

#    while(1):
#        xxx(input(x+" input a word : "))


#    txt.insert(END,result)


###############
#1 tkinter main program
##############
but = Button(window,text = "Find Meaning",command = dict_main) # Creates a tkinter button object
but.grid(row = 0,column = 0)

ent = Entry(window,textvariable = StringVar(),width = 40) # Creates a tkinter input object
ent.grid(row = 0, column = 1)

txt = Listbox(window,height = 5,width = 55) # Creates a tkinter ouput object
txt.grid(row = 1,column = 0,columnspan = 2)

ba = Scrollbar(window)
ba.grid(row = 1, column = 3)

ba1 = Scrollbar(window)
ba1.grid(row = 3, column = 0,columnspan = 2)

txt.configure(yscrollcommand = ba.set,xscrollcommand = ba1.set)
ba.configure(command = txt.yview)
ba1.configure(command = txt.xview)


window.mainloop()# ensures tkinter is in continous loop
###############
#2 tkinter main program
##############
