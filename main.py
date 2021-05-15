from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tags = soup.find_all(name="a", class_="storylink")
tag_list = [article_tag.getText() for article_tag in article_tags]
article_links = [article_tag.get("href") for article_tag in article_tags]

upvotes = []
article_upvotes = soup.find_all(name="td", class_="subtext")
for article in article_upvotes:
    has_votes = article.find(name="span", class_="score")
    if has_votes is None:
        upvotes.append(0)
    else:
        upvotes.append(int(has_votes.getText().split()[0]))

# upvotes = [int(article_upvote.getText().split(" ")[0]) for article_upvote in article_upvotes]

print(tag_list)
print(article_links)
print(upvotes)
highest_upvote = max(upvotes)
index_of_highest = upvotes.index(highest_upvote)
print(tag_list[index_of_highest])
print(article_links[index_of_highest])