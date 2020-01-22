from tkinter import * 
import wikipedia as wk 

window = Tk()

window.title('Search App')

# Defining the main function
def show_result():

    # Extracting the query
    entryQuery = Ent.get()
    TxtBox.delete(1.0, END)

    try:
        answerValue = wk.summary(entryQuery)
        TxtBox.insert(INSERT, answerValue)
        
    except:
        TxtBox.insert(INSERT, 'Please check your input or Network connection')
        
         
# Making a Frame(Top)
TopFrame = Frame(window)

lb = Label(TopFrame, text = 'Search Wikipedia', bg = 'Red', fg = 'yellow', pady = 5)
lb.pack(side = TOP, fill = X)

Ent = Entry(TopFrame, width = 70)
Ent.pack(side = TOP)

Bt = Button(TopFrame, text = 'GO', command = show_result, bg = 'Blue', fg = 'Yellow', width=10)

Bt.pack()

TopFrame.pack(side = TOP)

# Making the BottomFrame
BottomFrame = Frame(window)

scrollbar = Scrollbar(BottomFrame)

scrollbar.pack(side = RIGHT, fill = Y)

TxtBox = Text(BottomFrame, width = 70, yscrollcommand = scrollbar.set, wrap = WORD)

TxtBox.pack()

scrollbar.config(command = TxtBox.yview)

BottomFrame.pack()

window.mainloop()
