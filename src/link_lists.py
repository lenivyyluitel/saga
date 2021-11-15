import requests
import json

class safe:
    def safe(self, limit, tags):
        url = requests.get(
            f'https://safebooru.org/index.php?&page=dapi&s=post&q=index&pid=1&limit={limit}&json=1&tags={tags}')
        a = url.json()
        image = (a[0]['image'])
        directory = (a[0]['directory'])
        link = (f'https://safebooru.org//images/{directory}/{image}')
        try:
            self.link = link
            return link
        except Exception:
            link = ("tag not found try using other booru")
            self.link = link
            return link

class kona:
    def kona(self, limit, tags):
        r = requests.get(f"https://konachan.com/post.json?tags={tags}&limit={limit}&pid=1")
        data = r.json()
        images = len(data)
        for i in range(images):
            link = (f"{data[i]['file_url']}")
        try:
            self.link = link
            return link
        except Exception:
            link = ("tag not found try using other booru")
            self.link = link
            return link
