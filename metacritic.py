import requests 
from requests_html import HTMLSession
import pandas as pd

game = 'starfield'
url = 'https://www.metacritic.com/game/' + game + '/user-reviews/'
scroll = 250000
session = HTMLSession()
r = session.get(url)
r.html.render(scrolldown = scroll)

review_dict = {'username':[], 'date':[], 'score':[], 'review':[]}

usernames = r.html.find('div.c-pageProductReviews_row > div > div.c-siteReview > div.c-siteReview_main > div.c-siteReviewHeader > a.c-siteReviewHeader_username')
for username in usernames:
    review_dict['username'].append(username.text)
dates = r.html.find('div.c-pageProductReviews_row > div > div.c-siteReview > div.c-siteReview_main > div.c-siteReviewHeader > div.c-siteReviewHeader_reviewDate')
for date in dates:
    review_dict['date'].append(date.text)
scores = r.html.find('div.c-pageProductReviews_row > div > div.c-siteReview > div.c-siteReview_main > div.c-siteReviewHeader > div.c-siteReviewHeader_reviewScore > a > div > div > span')
for score in scores:
    review_dict['score'].append(score.text)
reviews = r.html.find('div.c-pageProductReviews_row > div > div.c-siteReview > div.c-siteReview_main > div:not(.c-siteReviewHeader) > div > span')
for review in reviews:
    review_dict['review'].append(review.text)

df = pd.DataFrame(review_dict)
print(df)
df.to_csv(game + '.csv')



# print(response)


    