
from tkinter import*
from tkinter import filedialog as fd
def newfile():
    t.delete("1.0",END)
def openfile():
    f=fd.askopenfile()
    t.insert("1.0",f.read())
def savefile():
    f=fd.asksaveasfile()
    msg=t.get("1.0",END)
    f.write(msg)     
    
root=Tk()
root.title("My Editor")
root.geometry ("400x400")
t=Text(root)
t.pack(expand=1,fill='both')
menubar =Menu(root)
root.config(menu=menubar)
menubar.add_command(label="New File",command=newfile)
menubar.add_command(label="Open File",command=openfile)
menubar.add_command(label="Save File",command=savefile)
menubar.add_command(label="Exit",command=exit)
menubar.add_command(label="Font Style")
root.mainloop()

