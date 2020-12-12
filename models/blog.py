import requests

DEFAULT_URL = 'https://api.npoint.io/43644ec4f0013682fc0d'


class Posts:
    def __init__(self, url=DEFAULT_URL):
        response = requests.get(url)
        self.posts = response.json()
        self.current_post = 0

    def get_all_posts(self):
        # self.current_post = len(self.posts)-1
        return self.posts

    def next_post(self):
        if len(self.posts) - 1 > self.current_post:
            self.current_post += 1
        else:
            self.current_post = 0

        return ''

    def get_currnt_post(self):
        return self.posts[self.current_post]


if __name__ == "__main__":
    posts = Posts()
    print(posts.current_post)
    print(posts.get_all_posts())
    print(posts.current_post)

    for post in posts.get_all_posts():
        print("Current : "+str(posts.current_post))
        print(post['id'])
        posts.next_post()

    for post in posts.get_all_posts():
        print("Current : "+str(posts.current_post))
        print(post['id'])
        posts.next_post()

    print(posts.current_post)
