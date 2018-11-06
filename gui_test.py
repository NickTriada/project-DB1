import tkinter as tk
import sys
import db_ops as dbops

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("480x170+800+250")
        self.title("project-DB1")
        toolbar = tk.Frame(self)
        toolbar.pack(side="top", fill="x")
        b1 = tk.Button(self, text="write to DB", command=self.print_stdout)
        b2 = tk.Button(self, text="print to stderr", command=self.print_stderr)
        b1.pack(in_=toolbar, side="left")
        b2.pack(in_=toolbar, side="left")

        self.text = tk.Text(self, wrap="word")
        self.text.place(x=300, y=5, height=155, width=170)

        self.lbl1 = tk.Label()
        self.lbl1.configure(text='''Number=0''')
        self.lbl1.place(x=5, y=35, height=25, width=80)

        yy = 35
        self.ent1 = tk.Entry()
        self.ent1.place(x=90, y=yy, height=25, width=200)


        self.lbl2 = tk.Label()
        self.lbl2.configure(text='''First Name''')
        self.lbl2.place(x=5, y=yy+25, height=25, width=80)

        self.ent2 = tk.Entry()
        self.ent2.place(x=90, y=yy+25, height=25, width=200)

        self.lbl3 = tk.Label()
        self.lbl3.configure(text='''Position''')
        self.lbl3.place(x=5, y=yy+50, height=25, width=80)

        self.ent3 = tk.Entry()
        self.ent3.place(x=90, y=yy+50, height=25, width=200)


        self.lbl4 = tk.Label()
        self.lbl4.configure(text='''Office''')
        self.lbl4.place(x=5, y=yy+75, height=25, width=80)

        self.ent4 = tk.Entry()
        self.ent4.place(x=90, y=yy+75, height=25, width=200)

        self.lbl5 = tk.Label()
        self.lbl5.configure(text='''Age''')
        self.lbl5.place(x=5, y=yy+100, height=25, width=80)

        self.ent5 = tk.Entry()
        self.ent5.place(x=90, y=yy+100, height=25, width=200)


        sys.stdout = TextRedirector(self.text, "stdout")
        sys.stderr = TextRedirector(self.text, "stderr")

    def print_stdout(self):
        ent_1 = self.ent1.get()
        x = dbops.main(int(ent_1), Firstname=self.ent2.get(), Position=self.ent3.get(), Office=self.ent4.get(), Age=self.ent5.get())


        '''Illustrate that using 'print' writes to stdout'''
        # print("this is stdout")

    def print_stderr(self):
        '''Illustrate that we can write directly to stderr'''
        sys.stderr.write("this is stderr\n")

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

app = ExampleApp()
app.mainloop()