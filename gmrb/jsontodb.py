# -*- coding: utf-8 -*-
__author__ = 'baijieying'

import sqlite3
import json

with open('hongqi201620qi.json','r') as f:
    jsfile=json.load(f)
    conn = sqlite3.connect('D:\\python\\docHelper\\test.db')
    x=[(news['name'],news['content'],'红旗文稿',news['date'],news['ban']) for news in jsfile]
    #import pdb
    #pdb.set_trace()
    conn.executemany("INSERT INTO NEWS (TITLE,CONTENT,TYPE,DATE,BANCI)   VALUES (?,?,?,?,?)",x)
    conn.commit()
    conn.close()
    print('success %s' %(len(x)))


