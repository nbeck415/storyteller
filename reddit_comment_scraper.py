'''
Name: Liana Shiroma
Date: June 6, 2020 (Hack the Northeast)
File: reddit_comment_scraper.py
Purpose: go through the writing prompts subreddit to find the top posts (prompts) and comments (stories)
'''
import praw
import re

reddit = praw.Reddit(client_id="Z6o_wmbUHrWuPA",
                     client_secret="cmrd2vkiM607Oh5Dyi947O2uYvk",
                     user_agent= 'Northeast',)

subreddit = reddit.subreddit("writingprompts")
#comments_txt = open(r"reddit_comments_more.txt","a")

#for printing purposes, to know how far along the program is
i = 0
#go through each submission in the top 200 of all time reddit writing posts
for submission in subreddit.top(limit=1):
    i+=1
    
    #filter out off topic posts so we just get stories
    if('[OT]' in submission.title):
        continue
    
    #print(i, submission.title)  
    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()
    
    for comment in comments:
        if (comment.score > 500):
            text = comment.body
            #filter out urls and other junk
            text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text, flags=re.MULTILINE)
            text = re.sub('^', '', text, flags=re.MULTILINE)
            text = re.sub(r'\[(.*?)\]', '', text, flags=re.MULTILINE)
            split_s = text.split("------------", 1) 
            split_s = split_s[0].split("_____")
            split_s = split_s[0].split("***")
            split_s = split_s[0].split("---")
            filtered = split_s[0]
            #print('COMMENT START \n', filtered, '\n COMMENT END')
            #comments_txt.write(filtered)
            
#comments_txt.close()
print("all done!")