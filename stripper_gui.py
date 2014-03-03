#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from Tkinter import *
import tkFileDialog

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("NC Stripper")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)

        px = 10
        py = 10
        
        Label(self, text="Input File:").grid(row=0,column=0,padx=px,pady=py)
        Label(self, text="Output File:").grid(row=1,column=0,padx=px,pady=py)
        Label(self, text="Decimal Places:").grid(row=2,column=0,padx=px,pady=py)

        self.inEntry = Entry(self,width=40)
        self.inEntry.grid(row=0,column=1,padx=px,pady=py)
        self.outEntry = Entry(self,width=40)
        self.outEntry.grid(row=1,column=1,padx=px,pady=py)

        self.decimalEntry = Entry(self,width=3)
        self.decimalEntry.grid(row=2,column=1,padx=px,pady=py,sticky=W)
        
        self.buttonIn = Button(self, text="Browse", command=self.load_file, width=10)
        self.buttonIn.grid(row=0, column=2, sticky=W,padx=px,pady=py)
        self.buttonOut = Button(self, text="Browse", command=self.save_file, width=10)
        self.buttonOut.grid(row=1, column=2, sticky=W,padx=px,pady=py)

        self.buttonProcess = Button(self, text="Process", command=self.process, width=10)
        self.buttonProcess.grid(row=2, column=2, sticky=W,padx=px,pady=py)
        
    def load_file(self):
        fname = tkFileDialog.askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("NC files", "*.nc"),
                                           ("All files", "*.*") ))
        if fname:
            self.inEntry.delete(0,END)
            self.inEntry.insert(0,fname)
            return
    
    def save_file(self):
        fname = tkFileDialog.asksaveasfilename(filetypes=(("Text files", "*.txt"),
                                           ("NC files", "*.nc"),
                                           ("All files", "*.*") ))
        if fname:
            self.outEntry.delete(0,END)
            self.outEntry.insert(0,fname)
            return

    def process(self):
        osStr = "python stripper.py"
        osStr += " -i " + self.inEntry.get()
        osStr += " -o " + self.outEntry.get()
        osStr += " -a " + self.decimalEntry.get()

        os.system(osStr)
        
        return
    

if __name__ == "__main__":
    MyFrame().mainloop()
