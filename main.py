from tkinter import *
from functools import partial
from playsound import playsound
import webbrowser
from time import sleep
import subprocess
import tkinter.messagebox as tmsg


def welcome_message(root):
    Label(root,text="Hello user! welcome to assistant",font=default,bg="yellow").pack(anchor="w",pady=15,padx=15)

def response(root,listbox):
    global variable
    variable = "e"
    command = query.get().lower()
    command = "Me: " + command
    listbox.insert(END,command)
    fetch(root,listbox,query.get())


def nikal(root):
    root.destroy()

def fetch(root,listbox,in_put):
    flag = 0
    if 'launch' in in_put or ('open' in in_put and 'apk' in in_put) or ('open' in in_put and '.exe' in in_put):
        l = in_put.split(' ')  
        if 'launch' in in_put:
            l.remove('launch')
        if 'open' in in_put:
            l.remove('open')
        if 'apk' in in_put:
            l.remove('apk')
        apk = ' '.join(l)
        print(apk)
        if '.exe' not in apk:
            apk = apk + '.exe'
        try:
            subprocess.call(apk)
            flag = 1
            my_response = f'Bot : apk {apk} launched'
            listbox.insert(END,my_response)
        except:
            pass
            # my_response = f'Bot : Oops we are trying our best to sort it out.'
            # listbox.insert(END,my_response)
        if not flag:
            try:
                for line in file:
                    if line == '':
                        break
                    data = line.strip().split('-')
                    name = data[0] + '.exe'
                    path = data[1]
                    if name == apk:
                        flag = 1
                        subprocess.call(path)
                        my_response = f'Bot : apk {apk} launched'
                        listbox.insert(END,my_response)
                        break
                if not flag:
                    my_response = f'Bot : Could not found apk {apk} to be launched'
                    listbox.insert(END,my_response)
            except:
                tmsg.showerror('File missing!','You will be redirect to your editor within 4 sec.')
                sleep(4)
                exit()
        

    elif 'search' in in_put and 'youtube' in in_put:
        l = in_put.split(' ')
        try:
            l.remove('search')
            l.remove('youtube')
            l.remove('on')
        except:
            pass
        query = '+'.join(l)
        my_response = f'Bot : Opening {query} on youtube at your default Browser'
        listbox.insert(END,my_response)
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
        
    elif 'open browser' in in_put or 'open webbrowser' in in_put:
        my_response = f'Bot : Opening Your Default Browser'
        listbox.insert(END,my_response)
        webbrowser.open('https://google.com/')
    elif 'open wikipedia' in in_put:
        my_response = f'Bot : Opening Wikipedia in your default Browser'
        listbox.insert(END,my_response)
        webbrowser.open('https://en.wikipedia.org/wiki/')
    elif 'wikipedia' in in_put:
        l = in_put.split(' ')
        try:
            l.remove('wikipedia')
            l.remove('search')
            l.remove('on')
        except:
            pass
        for i in range(len(l)):
            l[i] = l[i].capitalize()
        content = '_'.join(l)
        my_response = f'Bot : Searching {content} on wikipedia'
        listbox.insert(END,my_response)
        webbrowser.open(f'https://en.wikipedia.org/wiki/{content}')
    elif 'open youtube' in in_put:
        my_response = f'Bot : Opening Youtube in your default Browser'
        listbox.insert(END,my_response)
        webbrowser.open('https://www.youtube.com')
    elif 'play' in in_put and 'youtube' in in_put:
        l = in_put.split(' ')
        try:
            l.remove('play')
            l.remove('youtube')
            l.remove('on')
        except:
            pass
        query = '+'.join(l)
        my_response = f'Bot : Opening {query} on youtube at your default Browser'
        listbox.insert(END,my_response)
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
    elif 'play' in in_put:
        l = in_put.split()
        try:
            l.remove('play')
            l.remove('on')
            l.remove('music')
        except:
            pass
        music = ''.join(l)
        try:
            playsound(music)
        except:
            my_response = f'Bot : Did not found {music} in same directory.'
            listbox.insert(END,my_response)

    else:
        my_response = f'Bot : Searching is limited please follow Given pattern.'
        listbox.insert(END,my_response)


if __name__ == "__main__":
    default = "Courier 10 normal"
    root = Tk()
    variable = "e"
    root.geometry("700x600")
    root.maxsize(700,600)
    root.minsize(700,600)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT,fill=Y)
    listbox = Listbox(root,yscrollcommand=scrollbar.set)
    listbox.pack(fill=BOTH,ipady=200)
    listbox.insert(END ,'Please Follow patterns :-> ')
    listbox.insert(END ,'1. search carryminati on youtube')
    listbox.insert(END ,'2. play bye pewdiepie on youtube')
    listbox.insert(END ,'3. search amitabh bachahan on wikipedia')
    listbox.insert(END ,'4. open browser')
    listbox.insert(END ,'5. launch notepad')
    listbox.insert(END ,'6. lauch vscode (if path is available in apk_path.txt)')
    listbox.insert(END ,'7. lauch C://Users//exper//AppData//Local//Programs//Microsoft VS Code//Code.exe')
    listbox.insert(END ,'8. play songname.mp3')
    listbox.insert(END ,'9. We are working to make it a good assistant <-:::->')
    scrollbar.config(command=listbox.yview)

    Button(root,text="Exit",bg="red",command=partial(nikal,root)).place(x=100,y=570)

    query = StringVar()
    Entry(root,textvariable=query,font=default).place(x=200,y=570,width=300,height=26)

    Button(root,text="Go",bg="green",command=partial(response,root,listbox)).place(x=520,y=570)

    try:
        file = open('apk_path.txt','r')
    except:
        tmsg.showerror('File Missing','Would you want to continue?')

    root.mainloop()