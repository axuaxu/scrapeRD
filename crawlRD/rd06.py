"""__author__ = 'AX'
   scrape from reddit TIL
   save to db table
   """
from lxml import html
import requests
import sqlite3
import re


def openPage(s):
    page = requests.get(s)
    tree = html.fromstring(page.text)
    return tree

def readPage(docTree,s):
    myList = docTree.xpath(s)
    return myList

def getItems(tree):
    myDict = {'title': readPage(tree,'//a[@class="title may-blank "]/text()'),
          'domain': readPage(tree,'//span[@class="domain"]/a/text()'),
          'submitter': readPage(tree,'//p[@class="tagline"]/a/text()'),
          'liFirst': readPage(tree,'//li[@class="first"]/a/text()'),
          'FullName': readPage(tree,'//@data-fullname'),
          'datetime': readPage(tree,'//@datetime')
           }
    return myDict

def writeItems(myDB,myFile,myDict):


    conn = sqlite3.connect(myDB)
    c = conn.cursor()
    i = 0
    tline = ''
    mlen=[]
    for k,v in myDict.items():
         mlen.append(len(v))
    minLen = min(mlen)

    while i < minLen:
        for k,v in myDict.items():
            print k, 'corresponds to', v
        myDict['title'][i] = myDict['title'][i].replace("'","")
        #title[i] = title[i].replace("'","''")
        sComments = myDict['liFirst'][i].split(' ')
        if len(sComments)==1:
            numComments =0
        else:
            numComments = int(sComments[0])
        oneLine = "('"+myDict['title'][i]+"','"+myDict['domain'][i]+"','"+myDict['submitter'][i]+"',"+str(numComments)+",'"+myDict['FullName'][i]+"','"+myDict['datetime'][i]+"')".decode('unicode_escape').encode('ascii','ignore')
        oneLine = oneLine. replace("\r\n","")
        insertSQL = "insert into crawlRD_redditpage (rdtitle,rddomain,rdsubmitter,rdlifirst,rdfullname,rddatetime)  values "+ oneLine

        c.execute(insertSQL)
        tline = tline + oneLine +",\n"

        i = i + 1

    conn.commit()
    conn.close()

    outFile.write(tline.encode('utf8'))



#tree = openPage('http://localhost:8000/001/til.htm')
#main program

myDB = '..\db.sqlite3'
myFile = r'reddit-out.csv'
outFile = open(myFile,'w')

preName = 'http://localhost:8000/001/wiki-'

for j in range(1,11):
    pageName = preName + str(j)+'.htm'
    print pageName
    tree = openPage(pageName)
    myItems = getItems(tree)
    writeItems(myDB,myFile,myItems)
    nextprev = tree.xpath('//span[@class="nextprev"]/a/@href')

outFile.close





