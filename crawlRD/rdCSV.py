__author__ = 'Anne'
import csv, sqlite3

con = sqlite3.connect("reddit.db")
con.text_factory = str
cur = con.cursor()
cur.execute("CREATE TABLE reddit (created_utc, score,domain,id,title,author,ups,downs,num_comments,"
            "permalink,selftext,link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,"
          "author_flair_css_class,is_self,name,url,distinguished);")

with open('arma.txt','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    #created_utc,score,domain,id,title,author,ups,downs,num_comments,permalink,selftext,
    # link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,author_flair_css_class,
    # is_self,name,url,distinguished
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['created_utc'],i['score'],i['domain'],i['id'],i['title'],i['author'],i['ups'],
              i['downs'],i['num_comments'],i['permalink'],i['selftext'],i['link_flair_text'],
              i['over_18'],i['thumbnail'],i['subreddit_id'],i['edited'],i['link_flair_css_class'],
              i['author_flair_css_class'],i['is_self'],i['name'],i['url'],i['distinguished']) for i in dr]

cur.executemany("INSERT INTO reddit (created_utc, score,domain,id,title,author,ups,downs,num_comments,permalink,"
                "selftext,link_flair_text,over_18,thumbnail,subreddit_id,edited,link_flair_css_class,"
                "author_flair_css_class,is_self,name,url,distinguished)"
                 "VALUES (?, ?,?,?,?, ?,?,?,?, ?,?,?,?, ?,?, ?,?,?,?, ?,?,?);", to_db)
con.commit()

