from tkinter import *


root = Tk()
root.geometry("600x800")

#creating the label widget
label = Label(root,text="new text", font=("ariel",30,"bold"))
label.pack()


def click():
    #print("I got clicked")
    #label.config(text="I got clicked")
    label.config(text=input.get())
    

#creating the button widget
click_btn = Button(root,text="click me",command=click)
click_btn.pack()

#creating the entry widget
in_str = StringVar()
input = Entry(root,width=15,textvariable=in_str)
input.pack(pady=10)

#creating the text box widget
text_box = Text(root,width=30, height=8,relief=GROOVE)
text_box.pack()
#puts cursor in the text box 
text_box.focus()

def spinbox():
    print(spin_box.get())
#creating the spinbox widget
spin_box = Spinbox(root,from_=0, to=100,command=spinbox)
spin_box.pack(pady=5)

def scale_used(value):
    print(value)
#creating the scale widget
scale_wid = Scale(root,from_=0, to=100,command=scale_used)
scale_wid.pack()

def checkbutton():
    print(check_state.get())

#creating the check button widget
check_state = IntVar()
check_btn = Checkbutton(root,text="Is On",font=('ariel',17,'bold'),
                        variable=check_state,command=checkbutton)
check_btn.pack()

def radiobutton():
    print(radio_state.get())
#creating the radio button widget
radio_state = IntVar()
radio_btn1 = Radiobutton(root, text="Option 1",variable=radio_state,
                         value=1,command=radiobutton)
radio_btn1.pack()

radio_btn2 = Radiobutton(root, text="Option 2",variable=radio_state,
                         value=2,command=radiobutton)
radio_btn2.pack()

def listbox_used(event):
    #get current selelction of listbox 
    print(list_box.get(list_box.curselection()))

list_box = Listbox(root,width=30, height=8)
list_box.pack()

fruits = ["Apple", "Pear", "Orange", "Banana", "Mango"] 
for item in fruits:
    list_box.insert(fruits.index(item), item) 
    
list_box.bind("<<ListboxSelect>>", listbox_used)
     
""" def list_things():
    things = list_entry.get()
    list_box.insert(END, things)
    list_entry.delete(0,END) """
    
#creating the listbox widget

""" list_entry = Entry(root,width=15)
list_entry.pack(pady=7)

list_btn = Button(root,text="Click", command=list_things)
list_btn.pack(pady=7)
 """




root.mainloop()