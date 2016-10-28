# -*- coding: utf-8 -*-
__author__ = 'liyun'

from tkinter import *
from myFrame import  myFrame
from contentFrame import contentFrame
import sqlite3
class mainFrm(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.leftFrm=myFrame(self)
        self.leftFrm.pack(side=LEFT)
        self.contentFrm=contentFrame(self)
        self.contentFrm.pack(side=RIGHT,expand=YES,fill=Y)
        self.pack()
        self.leftFrm.results.bind('<Button-1>',self.handlelist)

    def handlelist(self,event):
        index=self.leftFrm.results.curselection()
        label=self.leftFrm.results.get(index).split('\t')[0]
        conn = sqlite3.connect('test.db')
        rows=conn.execute("SELECT CONTENT FROM NEWS WHERE Num=\'"+label+'\'')
        for row in rows:
            self.contentFrm.contentText.delete('0.0',END)
            self.contentFrm.contentText.insert('0.0',row[0])


if __name__=='__main__':
    mainFrm().mainloop()