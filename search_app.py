from tkinter import * # importing the tkinter module 
import wikipedia as wk # importing the wikipedia module 

# Making the window appear 
window = Tk()

# Making the title 
window.title('Search App')

# Defining the main function
def show_result():

    # Extractinf the query
    entry_query = Ent.get()
    TxtBox.delete(1.0, END)
    try:# try and except block for error handling 
        answer_value = wk.summary(entry_query)
        TxtBox.insert(INSERT, answer_value)
        
    except:
        TxtBox.insert(INSERT, 'Please check your input or Network connection')
        
         
# Making a Frame(Top)
TopFrame = Frame(window)

# Writing some text 
lb = Label(TopFrame, text = 'Search Wikipedia', bg = 'Red', fg = 'yellow', pady = 5)
lb.pack(side = TOP, fill = X)

# Making a entry field 
Ent = Entry(TopFrame, width = 70)
Ent.pack(side = TOP)

# Making a button 
Bt = Button(TopFrame, text = 'GO', command = show_result, bg = 'Blue', fg = 'Yellow', width=10)
# Packing the button 
Bt.pack()

# Packing the TopFrame 
TopFrame.pack(side = TOP)

# Making the BottomFrame
BottomFrame = Frame(window)

# Making the scrollbar 
scrollbar = Scrollbar(BottomFrame)

# Packing the scrollbar 
scrollbar.pack(side = RIGHT, fill = Y)

# Making the textbox 
TxtBox = Text(BottomFrame, width = 70, yscrollcommand = scrollbar.set, wrap = WORD)

# Packing the textbox 
TxtBox.pack()

scrollbar.config(command = TxtBox.yview)

# Packing the BottomFrame 
BottomFrame.pack()

# Running the mainloop function 
window.mainloop()
