import requests
from bs4 import BeautifulSoup


def get_url(link_type, idx):
    return "https://github.com/{:}?page={:}&tab={:}".format(username, idx, link_type)


def get_friend_list(link_type):
    friend_list = []

    for i in range(1, 6):
        url = get_url(link_type, i)
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html5lib')
        id_result = soup.select('span.Link--secondary.pl-1')

        for id in id_result:
            friend_list.append(id.text)

        friend_list = [_ for _ in friend_list if _ != '']

    return friend_list


def get_only_list(following_list, follower_list):
    following_set = set(following_list)
    follower_set = set(follower_list)

    only_follower = follower_set - following_set
    only_following = following_set - follower_set

    return only_follower, only_following


if __name__ == '__main__':
    username = input("username: ")

    following_list = get_friend_list('following')
    follower_list = get_friend_list('followers')

    only_follower, only_following = get_only_list(following_list, follower_list)

    print("only follower: ", end=' ')
    for follower in only_follower:
        print(follower, end=' | ')

    print("\nonly following:", end=' ')
    for following in only_following:
        print(following, end=' | ')
