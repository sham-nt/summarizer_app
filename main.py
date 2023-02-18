import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = input(">")

article = Article(url)

article.download()
article.parse()
article.nlp()

print(f"Title: {article.title}")
print(f"Authors: {article.authors}")
print(f"Publication Date: {article.publish_date}")
print(f"Summary: {article.summary}")