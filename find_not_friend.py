import requests
from bs4 import BeautifulSoup

username = input("username: ")

following_url = "https://github.com/{:}?tab=following".format(username)
follower_url = "https://github.com/{:}?tab=followers".format(username)

following_html = requests.get(following_url).text
follower_html = requests.get(follower_url).text

following_soup = BeautifulSoup(following_html, 'html5lib')
follower_soup = BeautifulSoup(follower_html, 'html5lib')

following_result = following_soup.select('turbo-frame a span.f4.Link--primary')
following_list = []

follower_result = follower_soup.select('turbo-frame a span.f4.Link--primary')
follower_list = []

for following in following_result:
    following_list.append(following.text)

for follower in follower_result:
    follower_list.append(follower.text)

following_list = [_ for _ in following_list if _ != '']
follower_list = [_ for _ in follower_list if _ != '']

following_set = set(following_list)
follower_set = set(follower_list)

only_following = following_set - follower_set
only_follower = follower_set - following_set

print("only following:", end=' ')
for following in only_following:
    print(following, end=' | ')

print("\nonly follower: ", end=' ')
for follower in only_follower:
    print(follower, end=' | ')
