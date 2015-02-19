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

    outFile = open(myFile,'w')
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
        #liFirst[i] = int(liFirst[i].replace("comments",""))
        #oneLine = "('"+title[i]+"','"+domain[i]+"','"+submitter[i]+"',"+str(liFirst[i])+",'"+datetime[i]+"')".decode('unicode_escape').encode('ascii','ignore')
        #oneLine = oneLine. replace("\r\n","")
        #insertSQL = "insert into crawlRD_redditpage (rdtitle,rddomain,rdsubmitter,rdlifirst,rddatetime)  values "+ oneLine

        #c.execute(insertSQL)
        #tline = tline + oneLine +",\n"

        i = i + 1

    conn.commit()
    conn.close()

    outFile.write(tline)
    outFile.close



#conn = sqlite3.connect('..\db.sqlite3')
#c = conn.cursor()

#OutName = r'.\output\reddit-out.csv'
#outFile = open('tt.csv','w')

#page = requests.get('http://localhost:8000/001/til.htm')
#tree = html.fromstring(page.text)

tree = openPage('http://localhost:8000/001/til.htm')
myItems = getItems(tree)
myDB = '..\db.sqlite3'
myFile = r'reddit-out.csv'

writeItems(myDB,myFile,myItems)



title = readPage(tree,'//a[@class="title may-blank "]/text()')
domain = readPage(tree,'//span[@class="domain"]/a/text()')
submitter = readPage(tree,'//p[@class="tagline"]/a/text()')
liFirst = readPage(tree,'//li[@class="first"]/a/text()')
FullName = readPage(tree,'//@data-fullname')
datetime = readPage(tree,'//@datetime')

nextprev = tree.xpath('//span[@class="nextprev"]/a/@href')

lenList = [len(title),len(domain),len(submitter),len(liFirst),len(FullName),len(datetime)]
minLen = min(lenList)


i = 0
tline = ''
while i < minLen:
    #print i+1,title[i],domain[i],submitter[i],liFirst[i],FullName[i],datetime[i],'\n'
    title[i] = title[i].replace("'","''")
    liFirst[i] = int(liFirst[i].replace("comments",""))
    oneLine = "('"+title[i]+"','"+domain[i]+"','"+submitter[i]+"',"+str(liFirst[i])+",'"+datetime[i]+"')".decode('unicode_escape').encode('ascii','ignore')
    #oneLine = oneLine.replace("'","")
    oneLine = oneLine. replace("\r\n","")
    #print oneLine
    #oneLine = re.sub('\W+',' ', oneLine )
    insertSQL = "insert into crawlRD_redditpage (rdtitle,rddomain,rdsubmitter,rdlifirst,rddatetime)  values "+ oneLine
    print(insertSQL)

    #c.execute(insertSQL)
    tline = tline + oneLine +",\n"

    i = i + 1


#conn.commit()
#conn.close()

#outFile.write(tline)
#outFile.close


#lin = nextprev[0].text
#code = tree.findtext('thing id-')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

print '\ntitle: ', title
print '\ndomain: ', domain
print '\nsubmitter: ', submitter
print '\ndatetime: ', datetime
print '\nliFirst: ', liFirst
print '\nFullName: ', FullName
print '\nnextprev: ', nextprev
print '\nlenList: ', lenList
print '\nminList: ', minLen
#print 'Prices: ', prices
