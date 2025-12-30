import tkinter as tk
'''Imports Tkinter module tk is an alias for easy access'''

def press(v):
    entry.insert(tk.END,v)
    '''Called when a number or operator button is clicked
        Inserts the pressed value at end of Entry widget'''
    
#clear fucntion
def clear():
    entry.delete(0,tk.END)
    '''Clears the calculator screen 
        Deletes all characters from index 0 to END'''
    
#calculation function 
def calc():
    try:
        result = eval(entry.get())
        '''entry.get() retrieves the expression (eg. 5+3)
            eval() evaluates the string as a python expression'''
        
        entry.delete(0,tk.END)
        '''clears the old expression'''
        entry.insert(0,result)
        '''Displays the result of expression'''

    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Invalid Expression!!")
        '''Handles invalid expressions(eg 5++)
            displays "error" instead of crashing'''
        
#Main window creation

root = tk.Tk()
'''Creates the main application window'''

root.title("Calculator")
'''Sets window title'''

root.configure(bg="#1e1e1e")
'''Sets the background color(dark theme)'''

root.resizable(False, False)

#ENtry widegts (Display screen)

entry = tk.Entry(
    root,
    font=("Times new Roman",20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
'''Acts as calculator display
Right-aligned for better calculator look'''

entry.grid(row=0, column=0, columnspan=4,padx=12, ipady=10)
'''Place entry at top
    columnspan=4 makes it stretch across 4 coloumns'''

#Button labels
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

'''Represent calculator buttons stored in list to reduce repetetive code'''

r=1
c=0
'''Rows and columns counters for grid layout'''

for b in buttons: #iterates through each button label 
    cmd = calc if b == "=" else lambda x=b: press(x)
    '''if button is "=", cal calc()
    otherwise call press with the button value 
    lambda x=b prevents late binding issue '''

    tk.Button(
        root,
        text = b,
        command = cmd, #these three lines will create the button widgets
        font = ("Calibri",14),
        width = 5,
        height =2,
        bg = "#ff9500" if b in "+_*/" else "#d44b4b",
        #operator buttons are orange, number buttons are gray
        fg = "red",
        bd = 0,
        ).grid(row=r, column = c, padx=6 , pady=6)
    
    c+=1
    #after 4 columns, move to next row 
    if c==4:
        r+=1
        c=0
        #Moves to next row after 4 buttons

        #clear button
        tk.Button(
            root,
            text="c",
            command = clear,
            font=("calibri",14),
            bg="#f3bf3b",
            fg="Black",
            bd=0,
            width=22,
            height=2
        ).grid(row=r, column=0, columnspan=4, pady=0)
'''Clears the calculator span across all columns'''

#Event loop
root.mainloop()

'''Keeps the window running listens for users '''
