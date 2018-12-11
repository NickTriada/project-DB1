

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from try_tests import db_project_support


#import db_ops as dbops

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = project_DB1 (root)
    db_project_support.init(root, top)
    root.mainloop()

w = None
def create_project_DB1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = project_DB1 (w)
    db_project_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_project_DB1():
    global w
    w.destroy()
    w = None


class project_DB1:

    def tt(self):
        print("test0")
        print("test1")
        print("test2")
        print("test3")

    def __init__(self, top=None):
        # def test1(self):
        #     name = self.Entry1.get()
        #     print(name)

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 10 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1159x898+500+50")
        top.title("project-DB1")
        top.configure(background="#d9d9d9")





        self.Button1 = Button(top)
        self.Button1.place(relx=0.37, rely=0.03, height=74, width=162)
        self.Button1.configure(activebackground="#d8a600", activeforeground="#000000", disabledforeground="#a3a3a3")
        self.Button1.configure(background="#7777d8", font=font9, foreground="#000000", pady="0", width=162)
        self.Button1.configure(highlightbackground="#d9d9d9", highlightcolor="black")
        self.Button1.configure(text='''write to DB''')
        self.Button1.configure(command=project_DB1.tt(self))


        self.Button2 = Button(top)
        self.Button2.place(relx=0.37, rely=0.12, height=64, width=162)
        self.Button2.configure(activebackground="#d80d0d", activeforeground="white",background="#d80d0d" )
        self.Button2.configure(foreground="#000000", disabledforeground="#a3a3a3", highlightbackground="#d9d9d9",highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Pull DB list''')
        self.Button2.configure(width=162)



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.01, rely=0.02, relheight=0.36, relwidth=0.35)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=555)

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.04, rely=0.08, height=38, width=121)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''First Name''')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.29, rely=0.08,height=34, relwidth=0.66)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=364)



        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.04, rely=0.23, height=38, width=118)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Last Name''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.04, rely=0.37, height=38, width=51)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Office''')

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.04, rely=0.5, height=38, width=62)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Age''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.04, rely=0.64, height=38, width=62)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Salary''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.04, rely=0.79, height=38, width=62)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Data''')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.29, rely=0.23,height=34, relwidth=0.66)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=364)

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.29, rely=0.37,height=34, relwidth=0.66)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=364)

        self.Entry4 = Entry(self.Frame1)
        self.Entry4.place(relx=0.29, rely=0.51,height=34, relwidth=0.66)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(width=364)

        self.Entry5 = Entry(self.Frame1)
        self.Entry5.place(relx=0.29, rely=0.65,height=34, relwidth=0.66)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(width=364)

        self.Entry6 = Entry(self.Frame1)
        self.Entry6.place(relx=0.29, rely=0.79,height=34, relwidth=0.66)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(width=364)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.37, rely=0.2, height=64, width=162)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#bfd884")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''csv''')
        self.Button3.configure(width=162)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.52, rely=0.02, relheight=0.36, relwidth=0.47)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=805)

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.01, rely=0.39, relheight=0.6, relwidth=0.98)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(width=1555)

        self.Scrolledlistbox1 = ScrolledListBox(self.Frame3)
        self.Scrolledlistbox1.place(relx=0.01, rely=0.02, relheight=0.96
                , relwidth=0.98)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.37, rely=0.28, height=74, width=162)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''extra''')
        self.Button4.configure(width=162)





# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()


