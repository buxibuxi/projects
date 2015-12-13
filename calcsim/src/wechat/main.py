#encoding=utf-8
'''
Created on 2015年12月12日

@author: luobu
'''

from wechat import wecheat
from mynlp import mycorpus
import os
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8') 

import logging
logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                     datefmt='%a, %d %b %Y %H:%M:%S',
                     filename = '../../log/main.log',
                     level=logging.INFO)               

if __name__ == '__main__':
    docspath = '/Users/luobu/workspace/projiects/wechat/wechat/conf_done'
    corpus_path ='/Users/luobu/workspace/data/wechat/articles/2015-12-04'
    dic_path = '/Users/luobu/workspace/data/wechat/articles/'

    cheatcase = wecheat.WeCheat(docspath,corpus_path,dic_path)
    #cheatcase.save_basicinfo()
    cheatcase.calccheatdocs()
    