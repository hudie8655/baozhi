# -*- coding: utf-8 -*-
__author__ = 'baijieying'

import sqlite3
import json

def origin():
    with open('xxsb1031.json','r') as f:
        jsfile=json.load(f)
        conn = sqlite3.connect('D:\\python\\docHelper\\test.db')
        x=[(news['name'],news['content'],'学习时报',news['date'],news['ban']) for news in jsfile]
        #import pdb
        #pdb.set_trace()
        conn.executemany("INSERT INTO NEWS (TITLE,CONTENT,TYPE,DATE,BANCI)   VALUES (?,?,?,?,?)",x)
        conn.commit()
        conn.close()
        print('success %s' %(len(x)))
        
def jjrbinline():
    jsfile=[]
    with open('bjrb1031.json','r') as f:
        for line in f:   
            try:
                jsfile.append(json.loads(line.strip('[],\n')))
            except Exception as e:
                print(line)
    import pdb
    pdb.set_trace()
    conn = sqlite3.connect('D:\\python\\docHelper\\test.db')
    x=[(news['name'],news['content'],'北京日报',news['date'],news['ban']) for news in jsfile]
    #import pdb
    #pdb.set_trace()
    conn.executemany("INSERT INTO NEWS (TITLE,CONTENT,TYPE,DATE,BANCI)   VALUES (?,?,?,?,?)",x)
    conn.commit()
    conn.close()
    print('success %s' %(len(x)))

if __name__=='__main__':
    origin()


