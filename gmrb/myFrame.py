# -*- coding: utf-8 -*-
__author__ = 'baijieying'
from tkinter import *
import sqlite3


class myFrame(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)

        self.make_widgets()
        self.results=Listbox(self,{'font':('黑体',14,'normal')})

        self.results.pack(fill=BOTH,expand=YES,side=LEFT)
        self.pack(fill=BOTH,expand=YES,side=LEFT)

    def make_widgets(self):
        self.searchtext=Text(self,{'font':('宋体',14,'normal'),'height':1})
        self.searchtext.pack(side='top',anchor='n')
        submitb=Button(self,text='查询标题',command=self.search)
        submitb.pack(side=TOP,anchor=W)

        submitb=Button(self,text='查询内容',command=self.searchcontent)
        submitb.pack(side=TOP,anchor=E)


    def search(self):
        keywords=self.searchtext.get('0.0', END).split()
        sql='''SELECT Num,TITLE,TYPE ,DATE ,BANCI FROM NEWS WHERE title like '%'''+'%\' and title like \'%'.join(keywords)+'%\' order by date'

        conn = sqlite3.connect('test.db')
        cur=conn.execute(sql)
        self.results.delete(0,END)
        for row in cur:
            self.results.insert(0,str(row[0])+'\t'+'\t'.join(row[1:]))

    def searchcontent(self):
        keywords=self.searchtext.get('0.0', END).split()
        sql='''SELECT Num,TITLE,TYPE ,DATE ,BANCI FROM NEWS WHERE content like '%'''+'%\' and content like \'%'.join(keywords)+'%\''

        conn = sqlite3.connect('test.db')
        cur=conn.execute(sql)
        self.results.delete(0,END)
        for row in cur:
            self.results.insert(0,str(row[0])+'\t'+'\t'.join(row[1:]))





if __name__=='__main__':
    myFrame().mainloop()
