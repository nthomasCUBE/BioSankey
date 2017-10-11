#!/usr/bin/python3


import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

from os.path import basename

class BioSankey:

    def __init__(self, master):

        
        self.master = master
        self.frame = tk.Frame(self.master)

        self.frame.configure()

        self.space = Label(self.frame, height=1, text="")
        self.space.grid(row=0,column=0)
        self.help = Text(self.frame, height=4, width=60, wrap=WORD)
        self.help.insert(INSERT, "Biosankey is a tool to visualize the microbial abundancies and the gene expression")
        self.help.grid(row=1,column=0, columnspan=3)

        self.e1_text = Label(self.frame, width=15, text="Expression: ", anchor='w')
        self.e1_file = Label(self.frame, width=18, text="", anchor='w', bg = "white", padx=6, borderwidth=2, relief="sunken")
        self.e1_btn = Button(self.frame, width=5, height=2, bg='lightgrey', text='Select', command=self.expression)
        self.e1_text.grid(row=2,column=0)
        self.e1_file.grid(row=2,column=1)
        self.e1_btn.grid(row=2,column=2)
        
        self.e2_text = Label(self.frame, width=15, text="DEGs: ", anchor='w')
        self.e2_file = Label(self.frame, width=18, text="", anchor='w', bg = "white", padx=6, borderwidth=2, relief="sunken")
        self.e2_btn = Button(self.frame, width=5, height=2, bg='lightgrey', text='Select', command=self.degs)
        self.e2_text.grid(row=3,column=0)
        self.e2_file.grid(row=3,column=1)
        self.e2_btn.grid(row=3,column=2)
        
        self.e3_text = Label(self.frame, width=15, text="Domains: ", anchor='w')
        self.e3_file = Label(self.frame, width=18, text="", anchor='w', bg = "white", padx=6, borderwidth=2, relief="sunken")
        self.e3_btn = Button(self.frame, width=5, height=2, bg='lightgrey', text='Select', command=self.domains)
        self.e3_text.grid(row=4,column=0)
        self.e3_file.grid(row=4,column=1)
        self.e3_btn.grid(row=4,column=2)
        
        self.e4_text = Label(self.frame, width=15, text="Microbial species: ", anchor='w')
        self.e4_file = Label(self.frame, width=18, text="", anchor='w', bg = "white", padx=6, borderwidth=2, relief="sunken")
        self.e4_btn = Button(self.frame, width=5, height=2, bg='lightgrey', text='Select', command=self.microbial)
        self.e4_text.grid(row=5,column=0)
        self.e4_file.grid(row=5,column=1)
        self.e4_btn.grid(row=5,column=2)

        self.lab5 = Label(self.frame, width=10, text="", anchor='w')
        self.lab5.grid(row=6,column=0)


        self.startBiosankey = tk.Button(self.frame, height=2, text = 'Start', width = 5, command = self.start_biosankey, bg="blue")
        self.startBiosankey.grid(row=6,column=2)


        self.f_expression=None
        self.f_domains=None
        self.f_degs=None
        self.f_microbial=None

        self.frame.pack()

    def expression(self):
        print("expression...")
        self.f_expression = askopenfilename()
        if(self.f_expression): 
            self.e1_btn.config(text='Reset', command=self.reset1)
            self.e1_file.config(text=basename(self.f_expression))

    def degs(self):
        print("degs...")
        self.f_degs = askdirectory()
        if(self.f_degs): 
            self.e2_btn.config(text='Reset', command=self.reset2)
            self.e2_file.config(text=basename(self.f_degs))

    def domains(self):
        print("domains...")
        self.f_domains = askopenfilename()
        if(self.f_domains): 
            self.e3_btn.config(text='Reset', command=self.reset3)
            self.e3_file.config(text=basename(self.f_domains))

    def microbial(self):
        print("microbial...")
        self.f_microbial = askopenfilename()
        if(self.f_microbial): 
            self.e4_btn.config(text='Reset', command=self.reset4)
            self.e4_file.config(text=basename(self.f_microbial))

    def reset1(self):
        self.e1_file.config(text="")
        self.e1_btn.configure(text='Select', command=self.expression)

    def reset2(self):
        self.e2_file.config(text="")
        self.e2_btn.configure(text='Select', command=self.degs)

    def reset3(self):
        self.e3_file.config(text="")
        self.e3_btn.configure(text='Select', command=self.domains)

    def reset4(self):
        self.e4_file.config(text="")
        self.e4_btn.configure(text='Select', command=self.microbial)

    def close_windows(self):
        self.master.destroy()

    def start_biosankey(self):

        print("Expression:%s" % self.f_expression)
        print("Domains:%s" % self.f_domains)
        print("Degs:%s" % self.f_degs)
        print("Microbial:%s" % self.f_microbial)

        print("Start...")

        import make_html
        make_html.parse_html(self.f_expression, self.f_microbial, self.f_degs, self.f_domains)

        print("Analysis has finished...")
        
def main(): 
    root = tk.Tk()
    root.title("BioSankey - version 0.1")
    app = BioSankey(root)
    root.configure(background='white')
    root.geometry('{}x{}'.format(500, 320))
    root.mainloop()

if __name__ == '__main__':
    main()

    
    
