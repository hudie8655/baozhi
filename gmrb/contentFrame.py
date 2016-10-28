# -*- coding: utf-8 -*-
__author__ = 'baijieying'
from tkinter import *
class contentFrame(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.contentText=Text(parent)
        self.contentText.config(font=('仿宋',24,'normal'))
        self.contentText.pack(expand=YES,fill='both')