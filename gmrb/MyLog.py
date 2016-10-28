# -*- coding: utf-8 -*-
#__author__ = 'baijieying'
class MyLog:
    file='log.txt'
    def log(self,s):
        with open(self.file,'a') as f:
            f.write(s)
