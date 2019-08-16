import tkinter as tk
import tkinter.ttk as ttk
from tkinter import ttk

from tkinter import *
master = Tk()
master.geometry("500x500")


# style = ttk.Style()
# style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
# # Modify the font of the body
# style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold'))
# # Modify the font of the headings
# style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
# # Remove the borders
# tree=ttk.Treeview(master,style="mystyle.Treeview")
# tree.insert(folder1, "end", "", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6KB"),tags = ('odd',))
# tree.insert(folder1, "end", "", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2KB"),tags = ('even',))
# tree.insert(folder1, "end", "", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1KB"),tags = ('odd',))
# tree.tag_configure('odd', background='#E8E8E8')
# tree.tag_configure('even', background='#DFDFDF')


tree=ttk.Treeview(master)
tree["columns"]=("one","two","three")
tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=400, minwidth=200)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)

tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Date modified",anchor=tk.W)
tree.heading("two", text="Type",anchor=tk.W)
tree.heading("three", text="Size",anchor=tk.W)


# Level 1
folder1=tree.insert("", 1, "", text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
tree.insert("", 2, "", text="text_file.txt", values=("23-Jun-17 11:25","TXT file","1 KB"))
# Level 2
# tree.insert(folder1, "end", "", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"))
# tree.insert(folder1, "end", "", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2 KB"))
# tree.insert(folder1, "end", "", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1 KB"))

tree.pack(side=tk.TOP,fill=tk.X)

master.mainloop()
