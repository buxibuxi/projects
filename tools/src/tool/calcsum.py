'''
Created on 2015年12月8日

@author: luobu
'''
import csv

if __name__ == '__main__':
    fpath = '/Users/luobu/Downloads/1/1-10000-1.csv'
    with open(fpath,'rb') as csvfile:
        reader = csv.reader(csvfile)
        