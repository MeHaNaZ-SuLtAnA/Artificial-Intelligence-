from tkinter import *
 
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
     
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello,WELCOME!!")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi,WELCOME!!")
    elif (e.get() == 'how are you?'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif (e.get()== 'what is your name?'):
         text.insert(END, "\n" + "Bot:Hi, my name is pikachu")
    elif (e.get() == 'good morning'):
        text.insert(END, "\n" + "Bot:good morning,have a nice day!!")
    elif (e.get() == 'thank you'):
            text.insert(END, "\n" + "Bot: you're welcome! ")
    elif (e.get() == 'course name'):
            text.insert(END, "\n" + "Bot: Artificial Intelligence ")
    elif (e.get() == 'Who made you?'):
            text.insert(END, "\n" + "Bot: JUTHI & EMON ")
    elif (e.get() == 'university name?'):
            text.insert(END, "\n" + "Bot:Metropolitan University ")
    elif (e.get() == 'What day is it today?'):
            text.insert(END, "\n" + "Bot: thursday ")
    elif (e.get() == ' date'):
            text.insert(END, "\n" + "Bot:28/08/2022")
    elif (e.get() == 'Where do you live?'):
            text.insert(END, "\n" + "Bot:Bangladesh  ")
    elif (e.get() == 'You’re smart'):
            text.insert(END, "\n" + "Bot: Thank you ")
    elif (e.get() == 'Are you part of the Matrix?'):
            text.insert(END, "\n" + "Bot: i am the part of python ")
    elif (e.get() == 'Are you human?'):
            text.insert(END, "\n" + "Bot: no i am a chatbot.  ")
    elif (e.get() == 'Which languages can you speak?'):
            text.insert(END, "\n" + "Bot: English ")
    elif (e.get() == 'bye!!see you again'):
            text.insert(END, "\n" + "Bot: bye, take care ")
   
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root,bg='lightblue', fg='black')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='blue', fg='white', width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('Pikachu')
root.mainloop()
